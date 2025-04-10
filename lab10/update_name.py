import psycopg2
from config import load_config

def updatePersonName(conn, newName, name):
    command = """UPDATE persons SET person_name = %s WHERE person_name = %s"""
    with conn.cursor() as cur:
        cur.execute(command, (newName, name))



if __name__ == "__main__":
    config = load_config()
    with psycopg2.connect(**config) as conn:
        name = input("Whose name you want to change?: ")
        newName = input("Enter new name: ")
        updatePersonName(conn, newName, name)
        conn.commit()
