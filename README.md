# OTP Email Sender

This Python script sends an email containing a one-time passcode (OTP) to a recipient fetched from a MySQL database.

## Requirements

- Python 3.x
- MySQL Server
- Gmail account for sending emails (with less secure app access enabled or using App Passwords)

## Installation

1. Clone this repository:

    ```
    git clone https://github.com/your_username/otp-email-sender.git
    ```

2. Install the required Python packages:

    ```
    pip install mysql-connector-python
    ```

3. Ensure you have a valid Gmail account to use as the sender's email address. If you're using a Gmail account, make sure to enable less secure app access or create an App Password.

## Configuration

1. Open the script `otp_email_sender.py` in a text editor.

2. Update the `db_config` dictionary with your MySQL database credentials:

    ```python
    db_config = {
        'host': 'localhost',
        'port': 3307,  # Change port if necessary
        'user': 'root',
        'password': '',
        'database': 'project_laundryku'
    }
    ```

3. Replace `my_email` and `password` variables with your Gmail account credentials:

    ```python
    my_email = "your_email@gmail.com"
    password = "your_password"
    ```

4. Ensure that you have an HTML file named `index.html` in the same directory as the script. This file should contain the HTML template for the email body. Replace `<div class="otp"></div>` with a placeholder for the OTP code.

## Usage

Run the script `otp_email_sender.py`:

```
python otp_email_sender.py
```

The script will connect to the MySQL database, fetch the recipient's email address and OTP, construct an email with the OTP embedded in the HTML content, and send it using your Gmail account.

## Notes

- Make sure your MySQL server is running and accessible.
- Ensure that the MySQL query in the script retrieves the correct information.
- Handle exceptions and errors appropriately for robustness.
- Consider using environment variables or secure methods for storing sensitive information like passwords.