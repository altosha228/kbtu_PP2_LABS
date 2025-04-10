import psycopg2
from config import load_config


def create_tables():
  commands = (
    """
      CREATE TABLE telephones(
        telephone_id  SERIAL          PRIMARY KEY,     
        telephone     VARCHAR(20)     NOT NULL
      )
    """,
    """
      CREATE TABLE persons(
        person_id     SERIAL          PRIMARY KEY,
        person_name   VARCHAR(255)    NOT NULL
      )
    """,
    """
      CREATE TABLE telephones_persons(
        person_id     INTEGER     NOT NULL,
        telephone_id  INTEGER     NOT NULL,
        PRIMARY KEY (person_id, telephone_id),
        FOREIGN KEY (person_id) 
                    REFERENCES persons(person_id)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE,
        FOREIGN KEY (telephone_id) 
                    REFERENCES telephones(telephone_id)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE
      )
    """
  )
  try:
    config = load_config()
    with psycopg2.connect(**config) as conn:
      with conn.cursor() as cur:
        for command in commands:
          cur.execute(command)
  except (psycopg2.DatabaseError, Exception) as error:
    print(error)


if __name__ == '__main__':
  create_tables()