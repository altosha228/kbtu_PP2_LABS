import psycopg2

def checkPerson(conn, person_name):
    command = """SELECT person_id FROM persons WHERE person_name = %s;"""
    with conn.cursor() as cur:
        cur.execute(command, (person_name,))
        payload = cur.fetchone()  # Не забудь добавить скобки для вызова метода!
        
        if payload:
            return payload[0]  # Возвращаем person_id
        else:
            return -1  # Возвращаем -1, если такого человека нет в базе
