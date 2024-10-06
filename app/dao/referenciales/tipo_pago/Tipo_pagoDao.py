# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class Tipo_pagoDao:

    def getTipo_pago(self):

        tipo_pagoSQL = """
        SELECT id, descripcion
        FROM tipo_pagos
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(tipo_pagoSQL)
            tipo_pagos = cur.fetchall() # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': tipo_pago[0], 'descripcion': tipo_pago[1]} for tipo_pago in tipo_pagos]

        except Exception as e:
            app.logger.error(f"Error al obtener todos lo tipo_pago: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getTipo_pagoById(self, id):

        tipo_pagoSQL = """
        SELECT id, descripcion
        FROM tipo_pagos WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(tipo_pagoSQL, (id,))
            tipo_pagoEncontrada = cur.fetchone() # Obtener una sola fila
            if tipo_pagoEncontrada:
                return {
                        "id": tipo_pagoEncontrada[0],
                        "descripcion": tipo_pagoEncontrada[1]
                    }  # Retornar los datos de la medico
            else:
                return None # Retornar None si no se encuentra la medico
        except Exception as e:
            app.logger.error(f"Error al obtener el tipo_pago: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarTipo_pago(self, descripcion):

        insertTipo_pagoSQL = """
   INSERT INTO tipo_pagos(descripcion) VALUES(%s) RETURNING id        
   """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertTipo_pagoSQL, (descripcion,))
            tipo_pago_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return tipo_pago_id
        
        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar tipo_pago: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False

          # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updateTipo_pago(self, id, descripcion):

        updateTipo_pagoSQL = """
        UPDATE tipo_pagos
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateTipo_pagoSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas            con.commit()
            con.commit()
        
            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar tipo_pago: {str(e)}")
            con.rollback()
            return False 
               
        finally:
            cur.close()
            con.close()

    def deleteTipo_pago(self, id):

        updateTipo_pagoSQL = """
        DELETE FROM tipo_pagos
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateTipo_pagoSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila        
        except Exception as e:
            app.logger.error(f"Error al eliminar tipo_pago: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

