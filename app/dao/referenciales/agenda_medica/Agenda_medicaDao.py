# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class Agenda_medicaDao:

    def getAgenda_medicas(self):
        agenda_medicaSQL = """
        SELECT 
            a.id_agenda_medica, p.nombre, p.apellido,e.descripcion, d.descripcion, t.descripcion, a.hora_inicio, a.hora_fin, s.nombre
            FROM agenda_medicas a, personas p, especialidades e, dias d, turnos t, sala_atenciones s
            where a.id_persona=p.id_persona and a.id_especialidad=e.id_especialidad and a.id_dia=d.id_dia and a.id_turno=t.id_turno and a.id_sala_atencion=s.id_sala_atencion
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(agenda_medicaSQL)
            agenda_medicas = cur.fetchall()
            return [
                {'id_agenda_medica': agenda_medica[0], 'nombre': agenda_medica[1], 'apellido': agenda_medica[2],'especialidad': agenda_medica[3], 'dia': agenda_medica[4],'turno': agenda_medica[5],'hora_inicio': agenda_medica[6], 'hora_fin': agenda_medica[7], 'sala': agenda_medica[8]}
                for agenda_medica in agenda_medicas
            ]
        except Exception as e:
            app.logger.error(f"Error al obtener todas las agendas médicas: {str(e)}")
            return []
        finally:
            cur.close()
            con.close()

    def getAgenda_medicaById(self, id_agenda_medica):
        agenda_medicaSQL = """
        SELECT a.id_agenda_medica, p.nombre, p.apellido, e.descripcion, d.descripcion, t.descripcion, a.hora_inicio, a.hora_fin, s.nombre, p.id_persona, e.id_especialidad, d.id_dia, t.id_turno, s.id_sala_atencion
            FROM agenda_medicas a, personas p, especialidades e, dias d, turnos t, sala_atenciones s 
            WHERE a.id_persona=p.id_persona and a.id_especialidad=e.id_especialidad and a.id_dia=d.id_dia and a.id_turno=t.id_turno and a.id_sala_atencion=s.id_sala_atencion and a.id_agenda_medica=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(agenda_medicaSQL, (id_agenda_medica,))
            agenda_medicaEncontrada = cur.fetchone()
            if agenda_medicaEncontrada:
                return {
                    "id_agenda_medica": agenda_medicaEncontrada[0],
                    "nombre": agenda_medicaEncontrada[1],
                    "apellido": agenda_medicaEncontrada[2],
                    "especialidad": agenda_medicaEncontrada[4],
                    "dia": agenda_medicaEncontrada[5],
                    "turno": agenda_medicaEncontrada[6],
                    "hora_inicio": agenda_medicaEncontrada[7],
                    "hora_fin": agenda_medicaEncontrada[8],
                    "sala": agenda_medicaEncontrada[9],
                    "id_persona": agenda_medicaEncontrada[10],
                    "id_especialidad": agenda_medicaEncontrada[11],
                    "id_dia": agenda_medicaEncontrada[12],
                    "id_turno": agenda_medicaEncontrada[13],
                    "id_sala_atencion": agenda_medicaEncontrada[14]
                    
                }
            else:
                return None
        except Exception as e:
            app.logger.error(f"Error al obtener agenda médica: {str(e)}")
            return None
        finally:
            cur.close()
            con.close()

    def guardarAgenda_medica(self, hora_inicio, hora_fin):
        insertAgenda_medicaSQL = """
        INSERT INTO Agenda_medica(hora_inicio, hora_fin) 
        VALUES(%s, %s) RETURNING id_agenda_medica
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(insertAgenda_medicaSQL, (hora_inicio, hora_fin))
            agenda_medica_id = cur.fetchone()[0]
            con.commit()
            return agenda_medica_id
        except Exception as e:
            app.logger.error(f"Error al insertar agenda médica: {str(e)}")
            con.rollback()
            return False
        finally:
            cur.close()
            con.close()

    def updateAgenda_medica(self, id_agenda_medica, hora_inicio, hora_fin):
        updateAgenda_medicaSQL = """
        UPDATE Agenda_medica
        SET hora_inicio=%s, hora_fin=%s
        WHERE id_agenda_medica=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(updateAgenda_medicaSQL, (hora_inicio, hora_fin, id_agenda_medica))
            filas_afectadas = cur.rowcount
            con.commit()
            return filas_afectadas > 0
        except Exception as e:
            app.logger.error(f"Error al actualizar agenda médica: {str(e)}")
            con.rollback()
            return False
        finally:
            cur.close()
            con.close()

    def deleteAgenda_medica(self, id_agenda_medica):
        deleteAgenda_medicaSQL = """
        DELETE FROM Agenda_medica
        WHERE id_agenda_medica=%s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(deleteAgenda_medicaSQL, (id_agenda_medica,))
            rows_affected = cur.rowcount
            con.commit()
            return rows_affected > 0
        except Exception as e:
            app.logger.error(f"Error al eliminar agenda médica: {str(e)}")
            con.rollback()
            return False
        finally:
            cur.close()
            con.close()
