import psycopg2
from config import load_config

def deletePerson(conn, name):
    command = """DELETE FROM persons WHERE person_name = %s"""
    with conn.cursor() as cur:
        cur.execute(command, (name,))  
        

if __name__ == "__main__":
    config = load_config()
    with psycopg2.connect(**config) as conn:
        name = input("Delete who? ")
        deletePerson(conn, name)
        conn.commit()
