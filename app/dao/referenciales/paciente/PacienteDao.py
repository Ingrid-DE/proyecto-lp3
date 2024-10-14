from flask import current_app as app
from app.conexion.Conexion import Conexion

class PacienteDao:

    def getPacientes(self):
        pacienteSQL = """
        SELECT id, nombre, edad, peso, altura
        FROM pacientes
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(pacienteSQL)
            pacientes = cur.fetchall()

            # Transformar los datos en una lista de diccionarios con los nuevos campos
            return [{'id': paciente[0], 'nombre': paciente[1], 'edad': paciente[2], 'peso': paciente[3], 'altura': paciente[4]} for paciente in pacientes]

        except Exception as e:
            app.logger.error(f"Error al obtener todos los pacientes: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getPacienteById(self, id):
        pacienteSQL = """
        SELECT id, nombre, edad, peso, altura
        FROM pacientes WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(pacienteSQL, (id,))
            pacienteEncontrado = cur.fetchone()
            if pacienteEncontrado:
                return {
                    "id": pacienteEncontrado[0],
                    "nombre": pacienteEncontrado[1],
                    "edad": pacienteEncontrado[2],
                    "peso": pacienteEncontrado[3],
                    "altura": pacienteEncontrado[4]
                }
            else:
                return None
        except Exception as e:
            app.logger.error(f"Error al obtener paciente por ID: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarPaciente(self, nombre, edad, peso, altura):
        insertPacienteSQL = """
        INSERT INTO pacientes(nombre, edad, peso, altura) 
        VALUES(%s, %s, %s, %s) RETURNING id
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(insertPacienteSQL, (nombre, edad, peso, altura))
            paciente_id = cur.fetchone()[0]
            con.commit()
            return paciente_id

        except Exception as e:
            app.logger.error(f"Error al insertar paciente: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def updatePaciente(self, id, nombre, edad, peso, altura):
        updatePacienteSQL = """
        UPDATE pacientes
        SET nombre=%s, edad=%s, peso=%s, altura=%s
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updatePacienteSQL, (nombre, edad, peso, altura, id))
            filas_afectadas = cur.rowcount
            con.commit()
            return filas_afectadas > 0

        except Exception as e:
            app.logger.error(f"Error al actualizar paciente: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deletePaciente(self, id):
        deletePacienteSQL = """
        DELETE FROM pacientes
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(deletePacienteSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0

        except Exception as e:
            app.logger.error(f"Error al eliminar paciente: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()