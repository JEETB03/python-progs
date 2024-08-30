from tkinter import *
import requests

def get_quote():
    """
    Fetches a random quote from the Kanye REST API and updates
    the displayed quote on the canvas.

    This function sends a GET request to the Kanye REST API to retrieve
    a random quote. The quote is then displayed on the canvas widget.
    """
    quotes = requests.get(url="https://api.kanye.rest")
    quotes.raise_for_status()  # Raise an error for bad responses
    quote = quotes.json()['quote']
    canvas.itemconfig(quote_text, text=quote)  # Update the text on the canvas

# Set up the main application window
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)  # Add padding around the window

# Create a canvas to hold the background image and quote text
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)  # Position the background image
quote_text = canvas.create_text(
    150, 207, 
    text="Kanye Quote Goes HERE", 
    width=250, 
    font=("Arial", 30, "bold"), 
    fill="white"
)
canvas.grid(row=0, column=0)  # Place the canvas in the grid

# Create a button with Kanye's image that fetches a new quote when clicked
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)  # Place the button in the grid

# Start the Tkinter event loop to run the application
window.mainloop()
