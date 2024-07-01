#!C:\Users\sarath\AppData\Local\Programs\Python\Python312\python.exe

import cgi
import mysql.connector

print("Content-type: text/html\n\n")

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
user_id = form.getvalue("id")
username = form.getvalue("username")
email = form.getvalue("email")

# HTML header
print("<html>")
print("<head>")
print("<title>Update Record</title>")
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

    # Update the record in the database
    cursor.execute("UPDATE users SET username=%s, email=%s WHERE id=%s", (username, email, user_id))
    conn.commit()

    # Display a success message
    print("<p>Record updated successfully.</p>")

except mysql.connector.Error as err:
    print(f"<p>Error: {err}</p>")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()

# Close the HTML tags
print("</body>")
print("</html>")
