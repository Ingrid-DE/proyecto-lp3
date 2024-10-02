# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class PacienteDao:

    def getPaciente(self):              

        pacienteSQL = """
        SELECT id, descripcion
        FROM pacientes
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(pacienteSQL)
            pacientes = cur.fetchall() # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': paciente[0], 'descripcion': paciente[1]} for paciente in pacientes]

        except Exception as e:
            app.logger.error(f"Error al obtener todas las pacientes: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getPacienteById(self, id):

        pacienteSQL = """
        SELECT id, descripcion
        FROM pacientes WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(pacienteSQL, (id,))
            pacienteEncontrada = cur.fetchone() # Obtener una sola fila
            if pacienteEncontrada:
                return {
                        "id": pacienteEncontrada[0],
                        "descripcion": pacienteEncontrada[1]
                    }  # Retornar los datos de la ciudad
            else:
                return None # Retornar None si no se encuentra la ciudad
        except Exception as e:
            app.logger.error(f"Error al obtener paciente: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarPaciente(self, descripcion):

        insertPacienteSQL = """
   INSERT INTO pacientes(descripcion) VALUES(%s) RETURNING id        
   """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertPacienteSQL, (descripcion,))
            paciente_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return paciente_id
        
        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar paciente: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False

          # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updatePaciente(self, id, descripcion):

        updatePacienteSQL = """
        UPDATE pacientes
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updatePacienteSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas            con.commit()
            con.commit()
        
            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar paciente: {str(e)}")
            con.rollback()
            return False 
               
        finally:
            cur.close()
            con.close()

    def deletePaciente(self, id):

        updatePacienteSQL = """
        DELETE FROM pacientes
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(updatePacienteSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila        
        except Exception as e:
            app.logger.error(f"Error al eliminar ciudad: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

