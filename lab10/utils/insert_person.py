from config import load_config
import psycopg2

def insert_person(conn, person_name):
  command = """INSERT INTO persons(person_name) VALUES(%s) RETURNING person_id;"""
  person_id = None

  try:
    with conn.cursor() as cur:
        cur.execute(command, (person_name,))
        rows = cur.fetchone()
        if rows:
          person_id = rows[0]
  except (psycopg2.DatabaseError, Exception) as error:
    print(error)
  finally:
    return person_id




# if __name__ == "__main__":
  # insert_person(input("Enter a name of a person you want to add: "))