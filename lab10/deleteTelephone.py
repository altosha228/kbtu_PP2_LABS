import psycopg2
from config import load_config

def deleteTelephone(conn, telephone):
    command = """DELETE FROM telephones WHERE telephone = %s"""
    with conn.cursor() as cur:
        cur.execute(command, (telephone))  
        

if __name__ == "__main__":
    config = load_config()
    with psycopg2.connect(**config) as conn:
        telephone = input("Delete which number? ")
        deleteTelephone(conn, telephone)
        conn.commit()
