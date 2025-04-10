import csv
import psycopg2
from config import load_config
from insert import insert_func


# Функция для импорта данных из CSV
def import_from_csv(conn, csv_file):
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # Пропускаем заголовок
        for row in csvreader:
            person_name, telephone = row
            insert_func(conn, person_name, telephone)


config = load_config()
with psycopg2.connect(**config) as conn:
  import_from_csv(conn, input("Enter csv file path: "))  #  data\insert_data.csv
  conn.commit()