import requests
from datetime import datetime
import smtplib
import time

# Your credentials and location details
MY_EMAIL = "your_email@example.com"  # Your email address
MY_PASSWORD = "your_password"        # Your email password
MY_LAT = 51.5074                     # Your latitude
MY_LONG = -0.1278                    # Your longitude

def is_iss_over_my_head():
    """
    Checks whether the ISS (International Space Station) is currently
    within a 5-degree range of your location's latitude and longitude.

    Returns:
        bool: True if ISS is overhead, False otherwise.
    """
    # Get the current location of the ISS from the open-notify API
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    # Extract the ISS's current latitude and longitude
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Check if the ISS is within +/- 5 degrees of your location
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    return False

def is_night():
    """
    Determines whether it is currently night time at your location.

    Returns:
        bool: True if it is night, False otherwise.
    """
    # Prepare parameters for the sunrise-sunset API
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    # Get sunrise and sunset times from the sunrise-sunset API
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    # Extract the hour of sunrise and sunset
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Get the current time
    time_now = datetime.now().hour

    # Determine if it's currently night time
    if time_now >= sunset or time_now <= sunrise:
        return True
    return False

# Main loop that checks every minute if the ISS is overhead and if it's night time
while True:
    time.sleep(60)  # Wait for 60 seconds before running the checks again
    if is_iss_over_my_head() and is_night():
        # Send an email notification if the ISS is overhead and it's night
        with smtplib.SMTP("smtp.example.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject: ISS is above you 👆🏻🛰️\n\nLook up!"
            )
