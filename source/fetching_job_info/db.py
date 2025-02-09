import psycopg2

class DB:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="127.0.0.1",  # use the service name from docker-compose
            dbname="postgres",
            user="postgres",
            password="postgres",
            port=5432
        )

        self.cur = self.conn.cursor()

    def create_table(self):
        #create table
        self.cur.execute("""CREATE TABLE IF NOT EXISTS job_elements (
            id INT PRIMARY KEY,
            job_title VARCHAR(255),
            job_place VARCHAR(255),
            job_link VARCHAR(255)
        );
        """)
        self.conn.commit()

    #cur.execute("""INSERT INTO job_elements (id, job_title, job_place) VALUES 
    #    (1, 'abc', 'def'),
    #    (2, 'ghi', 'jkl');
    #""")

    #cur.execute("""SELECT * FROM job_elements""")
    #for row in cur.fetchall():
    #    print(row)

    def write_db(self, id, job_title, job_place, job_link):
        write_query = self.cur.mogrify("""INSERT INTO job_elements (id, job_title, job_place, job_link) VALUES
            (%s, %s, %s, %s);
        """, (id, job_title, job_place, job_link))

        self.cur.execute(write_query)
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()
