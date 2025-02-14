import psycopg2
from psycopg2 import Error
from ..cfg import connection_info

class DB:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                host= connection_info["host"],
                dbname= connection_info["dbname"],
                user= connection_info["user"],
                password= connection_info["password"],
                port= connection_info["port"]
            )

            self.cur = self.conn.cursor()
        except Error as e:
            print(f"Error connecting to PostgreSQL: {e}")
            raise


    def create_table(self):
        #create the table
        try:
            #delete table if exist
            self.cur.execute("""DROP TABLE IF EXISTS job_elements;""")

            #create table
            self.cur.execute("""CREATE TABLE IF NOT EXISTS job_elements (
                id INT PRIMARY KEY,
                job_title VARCHAR(255),
                job_place VARCHAR(255),
                job_link VARCHAR(255)
            );
            """)
            self.conn.commit()
        except Error as e:
            print(f"Error creating table: {e}")
            self.conn.rollback()
            raise

    def write_db(self, id, job_title, job_place, job_link):
        #writing given job info to table
        try:
            write_query = self.cur.mogrify("""INSERT INTO job_elements (id, job_title, job_place, job_link) VALUES
                (%s, %s, %s, %s);
            """, (id, job_title, job_place, job_link))

            self.cur.execute(write_query)
            self.conn.commit()
        except Error as e:
            print(f"Error inserting data: {e}")
            self.conn.rollback()
            raise

    def close(self):
        try:
            if self.cur:
                self.cur.close()
            if self.conn:
                self.conn.close()
        except Error as e:
            print(f"Error closing database connection: {e}")
            raise
