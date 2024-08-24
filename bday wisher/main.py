import pywhatkit as kit
import pandas as pd
from datetime import datetime

def send_birthday_wishes():
    """
    Reads a CSV file containing birthday information and sends birthday wishes via WhatsApp
    to contacts whose birthday is today.

    The CSV file should contain the following columns:
    - Name: The name of the person
    - Date: The birthday of the person in the format 'MM-DD'
    - Phone: The phone number of the person, including the country code in the format '+CountryCodePhoneNumber'

    If the phone number does not include a country code, the function will attempt to prepend a '+' sign.
    """
    # Load the birthday data from a CSV file
    birthdays_df = pd.read_csv('birthdays_whatsapp.csv')

    # Get today's date in 'MM-DD' format
    today = datetime.today().strftime('%m-%d')

    # Iterate over the rows in the DataFrame
    for index, row in birthdays_df.iterrows():
        name = row['Name']
        birthday = row['Date']
        phone_number = str(row['Phone'])  # Ensure phone number is treated as a string

        # Ensure the phone number has the country code
        if not phone_number.startswith('+'):
            phone_number = f"+{phone_number}"  # Prepend default country code if missing

        # Check if today is the person's birthday
        if birthday == today:
            # Create a birthday message
            message = f"""Happy Birthday, {name}! 🎉🎂\nMay your day be filled with love, joy, and all the things that make you smile. On this special day, I want to celebrate the incredible person you are—someone who brings light into the lives of everyone around you.\n

Wishing you a year ahead full of new adventures, unforgettable moments, and success in everything you pursue. Here's to another year of being amazing! 🎂✨\n

Cheers to you, and may all your dreams come true! 🥂"""

            # Send the birthday message via WhatsApp
            kit.sendwhatmsg_instantly(phone_number, message)
            print(f"Birthday message sent to {name} on {phone_number}")

if __name__ == "__main__":
    send_birthday_wishes()
