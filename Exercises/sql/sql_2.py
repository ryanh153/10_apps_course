import psycopg2


def create_table():
    con = psycopg2.connect("dbname='learn_postgres' user='postgres' password='postgres' host='localhost' port='5432'")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    con.commit()
    con.close()


def insert_data(item, quantity, price):
    con = psycopg2.connect("dbname='learn_postgres' user='postgres' password='postgres' host='localhost' port='5432'")
    cursor = con.cursor()
    cursor.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    con.commit()
    con.close()


def view():
    con = psycopg2.connect("dbname='learn_postgres' user='postgres' password='postgres' host='localhost' port='5432'")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    con.close()
    return rows


def delete_item(item):
    con = psycopg2.connect("dbname='learn_postgres' user='postgres' password='postgres' host='localhost' port='5432'")
    cursor = con.cursor()
    cursor.execute("DELETE FROM store WHERE item=%s", (item,))
    con.commit()
    con.close()


def update(item, quantity, price):
    con = psycopg2.connect("dbname='learn_postgres' user='postgres' password='postgres' host='localhost' port='5432'")
    cursor = con.cursor()
    cursor.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    con.commit()
    con.close()


update('glass', 100, 5.0)
print(view())