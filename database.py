import psycopg2
from const import PASS


# Making the variable to login   
HOST = "localhost"
DATA = "test0"
PORT = "2401" 
USER = "postgres"
 

class Data():
    def connect(self):
        # Making the connection with the database 
        connect = psycopg2.connect(
            host=HOST,
            database=DATA,
            port=PORT,
            user=USER,
            password=PASS
        )   
        return connect

    def execute(self, query):
        # Establish the connection 
        conn = self.connect()
        
        #Connecting the cursor 
        cursor = conn.cursor()
        
        #Executing the statement
        cursor.execute(query)
        
        #Committing the transaction
        conn.commit()
        
        #Closing conection 
        cursor.close()
        conn.close()