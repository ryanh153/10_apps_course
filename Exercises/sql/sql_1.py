import mysql.connector

con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cursor = con.cursor()
word = "rain"
query = cursor.execute(f"SELECT * FROM Dictionary WHERE Definition LIKE 'Precipitation%'")
results = cursor.fetchall()

for result in results:
    print(result)