import psycopg2 as pg;

class DATABASE:
    def __init__( self, database, user, password):
        self.conn = pg.connect(
            database=database,
            user=user,
            password=password
        )
        self.cur = self.conn.cursor()
    
    def fetch(self, query):
        self.cur.execute(query)
        return self.cur.fetchall()
    
    def execute(self, query):
        self.cur.execute(query)
        self.conn.commit()
        
    def close(self):
        self.cur.close()
        self.conn.close()
    
    
        
        
        
        