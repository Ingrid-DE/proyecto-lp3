# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class MedicoDao:

    def getMedicos(self):

        medicoSQL = """
        SELECT id, descripcion
        FROM medicos
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(medicoSQL)
            medicos = cur.fetchall() # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': medico[0], 'descripcion': medico[1]} for medico in medicos]

        except Exception as e:
            app.logger.error(f"Error al obtener todas las medicos: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getMedicoById(self, id):

        medicoSQL = """
        SELECT id, descripcion
        FROM medicos WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(medicoSQL, (id,))
            medicoEncontrada = cur.fetchone() # Obtener una sola fila
            if medicoEncontrada:
                return {
                        "id": medicoEncontrada[0],
                        "descripcion": medicoEncontrada[1]
                    }  # Retornar los datos de la medico
            else:
                return None # Retornar None si no se encuentra la medico
        except Exception as e:
            app.logger.error(f"Error al obtener medico: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarMedicos(self, descripcion):

        inserteMedicoSQL = """
   INSERT INTO medicos(descripcion) VALUES(%s) RETURNING id        
   """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertMedicoSQL, (descripcion,))
            medico_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return medico_id
        
        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar medico: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False

          # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updateMedico(self, id, descripcion):

        updateMedicoSQL = """
        UPDATE medicos
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updamedicoSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas            con.commit()
            con.commit()
        
            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar medico: {str(e)}")
            con.rollback()
            return False 
               
        finally:
            cur.close()
            con.close()

    def deleteMedico(self, id):

        updateMedicoSQL = """
        DELETE FROM medicos
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updateMedicoSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila        
        except Exception as e:
            app.logger.error(f"Error al eliminar medico: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

