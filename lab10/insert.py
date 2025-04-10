from utils.insert_person import insert_person
from utils.insert_person_telephones_relation import insert_telephones_persons
from utils.insert_telephone import insert_telephone
from utils.check_if_person_exists import checkPerson
from update_telephone import updatePersonTelephone
from config import load_config
import psycopg2







def insert_func(conn, person_name, telephone):
  person_id = checkPerson(conn, person_name)

  if(person_id == -1):
    person_id = insert_person(conn, person_name)
    telephone_id = insert_telephone(conn, telephone)
    insert_telephones_persons(conn, person_id, telephone_id)
  else:
    updatePersonTelephone(conn, telephone, person_name)
    


  

if __name__ == "__main__":
  person_name = input("Enter name of a person you want to add: ")
  telephone = input("Enter telephone of a person you want to add: ")
  config = load_config()
  with psycopg2.connect(**config) as conn:
    insert_func(conn, person_name, telephone)
    conn.commit()


