# from datetime import datetime
# import pandas as pd
# import random
# import smtplib

# # Define your email credentials here


from datetime import datetime
import pandas
import random
import smtplib

# Define your email credentials here
MY_EMAIL = "youremail@email.com"
MY_PASSWORD = "your 2FA password"

# Get today's date as a tuple (month, day)
today = datetime.now()
today_tuple = (today.month, today.day)

# Load the birthday data from a CSV file into a pandas DataFrame
data = pandas.read_csv("birthdays.csv")

# Convert the DataFrame into a dictionary where the key is a tuple (month, day)
# and the value is the row data corresponding to that birthday
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# Check if today matches any birthday in the dictionary
if today_tuple in birthdays_dict:
    # Get the data of the birthday person
    birthday_person = birthdays_dict[today_tuple]
    
    # Randomly choose one of the letter templates
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    
    # Open the selected letter template and replace the placeholder with the person's name
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    # Send the customized birthday email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Secure the connection
        connection.login(MY_EMAIL, MY_PASSWORD)  # Login to your email account
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],  # Send the email to the birthday person
            msg=f"Subject:Happy Birthday!\n\n{contents}"  # Email subject and body
        )
