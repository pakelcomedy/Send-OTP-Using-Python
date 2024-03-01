import smtplib
import mysql.connector
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Database credentials
db_config = {
    'host': 'localhost',
    'port': 3307,  # Check if this port is correct for your MySQL server
    'user': 'root',
    'password': '',
    'database': 'project_laundryku'
}

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

try:
    # Connect to the database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Query to retrieve recipient email address from the user table
    query = "SELECT email FROM user WHERE id_pegawai = %s"
    user_id = 1  # Assuming the user's ID is 1
    cursor.execute(query, (user_id,))
    recipient_email = cursor.fetchone()[0]  # Assuming the query returns exactly one result

    # Your Gmail credentials
    my_email = "visimaladesktop@gmail.com"
    password = "cqos cciu knat feyp"  # Consider using more secure methods for handling passwords

    # Read HTML content from file
    html_body = read_file("index.html")  # Ensure "index.html" file exists and contains valid HTML content

    # Constructing the email message
    subject = "Reset Password"
    message = MIMEMultipart()
    message['From'] = my_email
    message['To'] = recipient_email
    message['Subject'] = subject

    # Attach HTML content
    html_content = MIMEText(html_body, 'html')
    message.attach(html_content)

    # Sending the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(user=my_email, password=password)
        smtp_server.sendmail(from_addr=my_email, to_addrs=recipient_email, msg=message.as_string())

    print("Email sent successfully!")

except mysql.connector.Error as error:
    print("Error while connecting to MySQL:", error)

except Exception as e:
    print("An error occurred:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
