from flask import current_app as app
from app.conexion.Conexion import Conexion

class MedicoDao:

    def getMedicos(self):
        medicoSQL = """
        SELECT id, nombre, apellido, especialidad
        FROM medicos
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(medicoSQL)
            medicos = cur.fetchall()

            # Transformar los datos en una lista de diccionarios con los nuevos campos
            return [{'id': medico[0], 'nombre': medico[1], 'apellido': medico[2], 'especialidad': medico[3]} for medico in medicos]

        except Exception as e:
            app.logger.error(f"Error al obtener todos los medicos: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getMedicoById(self, id):
        medicoSQL = """
        SELECT id, nombre, apellido, especialidad
        FROM medicos WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(medicoSQL, (id,))
            medicoEncontrado = cur.fetchone()
            if medicoEncontrado:
                return {
                    "id": medicoEncontrado[0],
                    "nombre": medicoEncontrado[1],
                    "apellido": medicoEncontrado[2],
                    "especialidad": medicoEncontrado[3]
                }
            else:
                return None
        except Exception as e:
            app.logger.error(f"Error al obtener medico por ID: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarMedico(self, nombre, apellido, especialidad):
        insertMedicoSQL = """
        INSERT INTO medicos(nombre, apellido, especialidad) VALUES(%s, %s, %s) RETURNING id
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(insertMedicoSQL, (nombre, apellido, especialidad))
            medico_id = cur.fetchone()[0]
            con.commit()
            return medico_id

        except Exception as e:
            app.logger.error(f"Error al insertar medico: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def updateMedico(self, id, nombre, apellido, especialidad):
        updateMedicoSQL = """
        UPDATE medicos
        SET nombre=%s, apellido=%s, especialidad=%s
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateMedicoSQL, (nombre, apellido, especialidad, id))
            filas_afectadas = cur.rowcount
            con.commit()
            return filas_afectadas > 0

        except Exception as e:
            app.logger.error(f"Error al actualizar medico: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deleteMedico(self, id):
        deleteMedicoSQL = """
        DELETE FROM medicos
        WHERE id=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(deleteMedicoSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0

        except Exception as e:
            app.logger.error(f"Error al eliminar medico: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()