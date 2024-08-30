# Kanye Says... - Tkinter Quote App

## Overview
"Kanye Says..." is a simple Tkinter-based Python application that fetches and displays random quotes from the Kanye REST API. Each time the user clicks the Kanye button, a new quote is retrieved and displayed in the application window.

## How It Works
- The app uses the `requests` library to fetch quotes from the [Kanye REST API](https://api.kanye.rest).
- The fetched quote is displayed on a Tkinter canvas with a background image and styled text.

## Requirements
- Python 3.x
- `requests` library
- Tkinter (comes with Python's standard library)

## Installation
1. Clone this repository or download the script file.
2. Install the required Python libraries:
    ```bash
    pip install requests
    ```

## Setup
1. Ensure you have the required image files:
    - `background.png`: Background image for the canvas.
    - `kanye.png`: Image used for the button.

2. Place these images in the same directory as the script.

3. Run the script:
    ```bash
    python kanye_says.py
    ```

## Usage
- When you run the application, a window will appear with a background image and a placeholder text.
- Click the Kanye button to fetch and display a new quote from the Kanye REST API.

## Customization
- **Background Image**: Replace `background.png` with any other image to change the background.
- **Button Image**: Replace `kanye.png` with any image of your choice for the button.
- **Font and Colors**: Modify the `font` and `fill` parameters in the `canvas.create_text` method to change the appearance of the text.

## Troubleshooting
- **Network Issues**: Ensure you have a stable internet connection, as the app fetches quotes from an online API.
- **File Not Found**: Ensure that `background.png` and `kanye.png` are in the correct directory and have the correct filenames.

