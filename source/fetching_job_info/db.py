import psycopg2
from ..cfg import connection_info

class DB:
    def __init__(self):
        self.conn = psycopg2.connect(
            host= connection_info["host"],
            dbname= connection_info["dbname"],
            user= connection_info["user"],
            password= connection_info["password"],
            port= connection_info["port"]
        )

        self.cur = self.conn.cursor()

        self.cur.execute("""SELECT truncate_if_exists('job_elements');""")
        self.conn.commit()

    def create_table(self):
        #create the table
        self.cur.execute("""CREATE TABLE IF NOT EXISTS job_elements (
            id INT PRIMARY KEY,
            job_title VARCHAR(255),
            job_place VARCHAR(255),
            job_link VARCHAR(255)
        );
        """)
        self.conn.commit()

    def write_db(self, id, job_title, job_place, job_link):
        #writing given job info to table
        write_query = self.cur.mogrify("""INSERT INTO job_elements (id, job_title, job_place, job_link) VALUES
            (%s, %s, %s, %s);
        """, (id, job_title, job_place, job_link))

        self.cur.execute(write_query)
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()
