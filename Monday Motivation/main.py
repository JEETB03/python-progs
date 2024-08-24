import smtplib
import datetime as dt
import random

# ---------------------------------------------------------------- VARIABLES SETUP ---------------------------------------------------------------- #

my_email = "[Sender Address]"              # Your sender email address, remove the braces, it should only be a string
password = "[sender's 2FA password]"       # Your 2FA Password from sender Gmail. Check the README file for details, remove the braces, it should only be a string
now = dt.datetime.now()                    # Captures the current date and time
weekday = now.weekday()                    # Captures the weekday of the current date (0 = Monday, 6 = Sunday)

# ---------------------------------------------------------------- MAIL SETUP -------------------------------------------------------------------- #

if weekday == 0:  # Check if today is Monday (weekday = 0)
    
    # Open the quotes file and read all lines
    with open("./quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()  # Read all quotes into a list
        quote = random.choice(all_quotes)    # Select a random quote from the list

    # Set up the SMTP connection to send the email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=my_email, password=password)  # Log in to the email account
        connection.sendmail(
            from_addr=my_email,
            to_addrs=["reciever@email.com"],  # Replace with the recipient's email address, remove the braces, it should only be a string
            msg=f"Subject:Monday Motivation!\n\n{quote}\nHave a nice day!"  # Format the email
        )

