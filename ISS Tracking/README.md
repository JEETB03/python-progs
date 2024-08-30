# ISS Tracker and Notifier

## Overview
This Python script tracks the International Space Station (ISS) and sends an email notification when the ISS is above your location and it is night time. The script periodically checks the ISS's position and compares it to your location's latitude and longitude. If the ISS is within a 5-degree range and it is night, you will receive an email alert.

## How It Works
1. **ISS Position Check**: The script uses the open-notify API to get the current position of the ISS.
2. **Night Time Check**: It uses the sunrise-sunset API to determine whether it is currently night at your location.
3. **Email Notification**: If both conditions are met (ISS overhead and night time), the script sends you an email notification.

## Requirements
- Python 3.x
- `requests` library
- `smtplib` library (comes with Python's standard library)

## Installation
1. Clone this repository or download the script file.
2. Install the required Python libraries:
    ```bash
    pip install requests
    ```

## Setup
1. Replace the placeholder values in the script with your actual information:
    - `MY_EMAIL`: Your email address.
    - `MY_PASSWORD`: Your email password.
    - `MY_LAT`: Your latitude.
    - `MY_LONG`: Your longitude.
    - SMTP server details (e.g., `smtp.example.com`).

2. Save the script and run it:
    ```bash
    python iss_tracker.py
    ```

## Running the Script
- The script runs in an infinite loop, checking every 60 seconds whether the ISS is overhead and if it's night time.
- If the conditions are met, an email notification will be sent to your email address.

## Notes
- Ensure that your email provider allows access to less secure apps or configure app-specific passwords if needed.
- You can modify the check interval by changing the `time.sleep(60)` line.

## Troubleshooting
- If you don't receive emails, check your SMTP settings and ensure that your email provider allows the script to send emails.
- Verify your latitude and longitude are correctly set.


