import psycopg2

class Conexion:

    """Metodo constructor
    """
    def __init__(self):
        
        self.con = psycopg2.connect(dbname="lp3-db", user="postgres", password= "19092003", host="localhost", port=5432)

    """getConexion
        retorna la instancia de la base de datos
    """
    def getConexion(self):
        return self.con