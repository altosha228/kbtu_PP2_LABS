from config import load_config
import psycopg2

def insert_telephones_persons(conn, person_id, telephone_id):
  command = """INSERT INTO telephones_persons(person_id, telephone_id) VALUES(%s, %s);"""
  

  try:
    with conn.cursor() as cur:
        cur.execute(command, (person_id, telephone_id,))
        rows = cur.fetchone()
  except (psycopg2.DatabaseError, Exception) as error:
    print(error)




# if __name__ == "__main__":
  # insert_person(input("Enter a name of a person you want to add: "))