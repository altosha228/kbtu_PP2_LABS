from config import load_config
import psycopg2

def insert_many_persons(persons_list):
    

    sql = "INSERT INTO persons(person_name) VALUES(%s) RETURNING *"
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.executemany(sql, persons_list)

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == "__main__":
  insert_many_persons()