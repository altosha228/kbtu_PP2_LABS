import psycopg2
from config import load_config

def updatePersonTelephone(conn, newTelephone, name):
    command = """
    UPDATE telephones
    SET telephone = %s
    FROM telephones_persons tp
    JOIN persons p ON p.person_id = tp.person_id
    WHERE telephones.telephone_id = tp.telephone_id AND p.person_name = %s;
    """
    with conn.cursor() as cur:
        cur.execute(command, (newTelephone, name))




if __name__ == "__main__":
    config = load_config()
    with psycopg2.connect(**config) as conn:
        name = input("Whose telephone you want to change?: ")
        telephone = input("Enter new telephone: ")
        updatePersonTelephone(conn, telephone, name)
        conn.commit()