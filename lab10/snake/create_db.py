import psycopg2
from config import load_config


def create_tables():
  command = """CREATE TABLE userscore(
                  user_id       SERIAL            PRIMARY KEY,
                  username      VARCHAR(30)       NOT NULL,
                  highscore     INTEGER           NOT NULL,
                  level         INTEGER           NOT NULL
               );"""
  try:
    config = load_config()
    with psycopg2.connect(**config) as conn:
      with conn.cursor() as cur:
        cur.execute(command)
          
  except (psycopg2.DatabaseError, Exception) as error:
    print(error)


if __name__ == '__main__':
  create_tables()