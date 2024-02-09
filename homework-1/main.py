"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
import csv

conn = psycopg2.connect(host="localhost", database="north", user="postgres", password="mapasova72670290")
with conn:
    with conn.cursor() as cur:
        with open('..\\homework-1\\north_data\\customers_data.csv') as file_customers:
            csv_reader = csv.DictReader(file_customers)
            for row in csv_reader:
                cur.execute("INSERT INTO customers VALUES(%s, %s, %s)", (row["customer_id"], row['company_name'], row['contact_name']))
            cur.execute("SELECT * FROM customers")
            rows = cur.fetchall()
            for row in rows:
                print(row)


        with open('..\\homework-1\\north_data\\employees_data.csv') as file_employees:
            csv_reader = csv.DictReader(file_employees)
            for row in csv_reader:
                cur.execute("INSERT INTO employees VALUES(%s, %s, %s, %s, %s, %s)",
                            (row["employee_id"], row["first_name"], row["last_name"], row["title"], row["birth_date"], row["notes"]))
            cur.execute("SELECT * FROM employees")
            rows = cur.fetchall()
            for row in rows:
                print(row)



        with open('..\\homework-1\\north_data\\orders_data.csv') as file_orders:
            csv_reader = csv.DictReader(file_orders)
            for row in csv_reader:
                cur.execute("INSERT INTO orders VALUES(%s, %s, %s, %s, %s)",
                            (row["order_id"], row["customer_id"], row["employee_id"], row["order_date"], row["ship_city"]))
            cur.execute("SELECT * FROM orders")
            rows = cur.fetchall()
            for row in rows:
                print(row)