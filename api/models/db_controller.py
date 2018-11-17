"""
This module establishes connection with DataBase
"""
from urllib.parse import urlparse
import psycopg2
import psycopg2.extras as walimike

class Dbcontroller:
    """
    class handles database connection
    """

    def __init__(self, database_url):
        parsed_url = urlparse(database_url)
        dbname = parsed_url.path[1:]
        user = parsed_url.username
        host = parsed_url.hostname
        password = parsed_url.password
        port = parsed_url.port
        self.conn = psycopg2.connect(
            database=dbname,
            user=user,
            password=password,
            host=host,
            port=port)
        self.conn.autocommit = True
        self.cursor = self.conn.cursor(cursor_factory=walimike.RealDictCursor)

    def create_tables(self):
        """
        method creates tables
        """
        user_table = "CREATE TABLE IF NOT EXISTS users(usrId serial PRIMARY KEY,\
          username varchar(50), email varchar(100), password varchar(20),\
          role varchar(15))"

        parcels_table = "CREATE TABLE IF NOT EXISTS parcels(parcelId serial PRIMARY KEY,\
          parcel_name varchar(100), price integer, parcel_status varchar(20),\
          usrId INTEGER REFERENCES users(usrId))"
          #FOREIGN KEY (user_id) REFERENCES users(user_id) )""",

        self.cursor.execute(user_table)
        self.cursor.execute(parcels_table)

    def drop_tables(self):
        """
        method drops tables
        """
        drop_user_table = "DROP TABLE users cascade"
        drop_parcel_table = "DROP TABLE parcels cascade"
        self.cursor.execute(drop_user_table)
        self.cursor.execute(drop_parcel_table)

    def fetch_all_entries(self,table_name):
        """ Fetches all entries from the database"""
        try:
            query = ("SELECT * FROM %s;") %(table_name)
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return rows
        except (Exception, psycopg2.DatabaseError)as Error:
            raise Error
