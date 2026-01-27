#import psycopg2
import mysql.connector
cnx = mysql.connector.connect(
        host='127.0.0.1',  # Hostname (e.g., 'localhost' or an IP address)
        user='root',
        password='Naveen_2026@',
        database='Rivier_students_faculty'
    )
print("Connection established successfully!")


cursor = cnx.cursor()
cursor.execute("SELECT * FROM faculty_demographics")


results = cursor.fetchall()
for row in results:
    print(row)

if 'cursor' in locals() and cursor is not None:
    cursor.close()
if 'cnx' in locals() and cnx.is_connected():
    cnx.close()
    print("Connection closed.")


