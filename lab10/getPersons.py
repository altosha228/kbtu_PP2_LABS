import psycopg2
from config import load_config


def get_country_code_by_name(country_name):
    match country_name.lower():
        case "united states" | "canada":
            return "+1"
        case "united kingdom":
            return "+44"
        case "france":
            return "+33"
        case "russia" | "kazakhstan":
            return "+7"
        case "germany":
            return "+49"
        case "japan":
            return "+81"
        case _:
            return "Unknown country"


def getPersonsOfSpecificCountry(conn, country):
    numCode = get_country_code_by_name(country)
    if numCode == "Unknown country":
        print("Unknown country: " + country)
        return
    command = """SELECT p.person_name, t.telephone FROM persons p
                 JOIN telephones_persons tp ON tp.person_id = p.person_id
                 JOIN telephones t ON t.telephone_id = tp.telephone_id
                 WHERE t.telephone LIKE %s"""
    with conn.cursor() as cur:
        cur.execute(command, (numCode + '%',))  
        rows = cur.fetchall()
        if rows:
            for row in rows:
                print(f"Name: {row[0]}, Telephone: {row[1]}")
        else:
            print("No persons found for the specified country.")


if __name__ == "__main__":
    country = input("What country?: ")
    config = load_config()
    with psycopg2.connect(**config) as conn:
        getPersonsOfSpecificCountry(conn, country)
