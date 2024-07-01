#!C:\Users\sarath\AppData\Local\Programs\Python\Python312\python.exe

import mysql.connector

print("Content-type: text/html\n\n")

# HTML header
print("<html>")
print("<head>")
print("<title>Read Records</title>")
print("</head>")
print("<body>")

try:
    # Connect to the database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",         # Change this to your database username
        password="",         # Change this to your database password
        database="cgi"       # Database name is cgi
    )
    
    cursor = conn.cursor()

    # Fetch all records from the database
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    # Display records
    print("<h2>Users</h2>")
    for row in rows:
        print(f"<p>ID: {row[0]}, Username: {row[1]}, Email: {row[2]}</p>")

except mysql.connector.Error as err:
    print(f"<p>Error: {err}</p>")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()

# Close the HTML tags
print("</body>")
print("</html>")
