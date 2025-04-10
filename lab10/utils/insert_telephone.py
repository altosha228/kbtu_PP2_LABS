from config import load_config
import psycopg2

def insert_telephone(conn, telephone):
  command = """INSERT INTO telephones(telephone) VALUES(%s) RETURNING telephone_id;"""
  telephone_id = None

  try:
    with conn.cursor() as cur:
        cur.execute(command, (telephone,))
        rows = cur.fetchone()
        if rows:
          telephone_id = rows[0]
  except (psycopg2.DatabaseError, Exception) as error:
    print(error)
  finally:
    return telephone_id




# if __name__ == "__main__":
  # insert_person(input("Enter a name of a person you want to add: "))