#!C:\Users\sarath\AppData\Local\Programs\Python\Python312\python.exe
import cgi
import mysql.connector

print("Content-type: text/html\n\n")

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
username = form.getvalue("username")
email = form.getvalue("email")

# HTML header
print("<html>")
print("<head>")
print("<title>Success Page</title>")
print("</head>")
print("<body>")

try:
    # Connect to the database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",         # Change this to your database username
        password="",         # Change this to your database password
        database="cgi"    # Change this to your database name
    )
    
    cursor = conn.cursor()

    # Insert data into the database
    cursor.execute("INSERT INTO users (username, email) VALUES (%s, %s)", (username, email))
    conn.commit()

    # Format the username with <strong> and <span> for larger text
    print("<p><strong><span style='font-size: 20px;'>{}</span></strong> Congratulations !!</p>".format(username))
    # Display a congratulatory message with the submitted username in larger text.

    # Print the second line on a new line
    print("<p>You have successfully sent data from an HTML form to a CGI Python script and stored it in the database.</p>")
    # Display a message indicating that the form data was successfully processed and stored in the database.

except mysql.connector.Error as err:
    print(f"<p>Error: {err}</p>")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()

# Close the HTML tags
print("</body>")
print("</html>")
