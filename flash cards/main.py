from tkinter import *
import pandas
import random

# -------------------------------------------------------------- CONSTANTS ----------------------------------------------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"  # Background color for the window and canvas
current_card = {}  # Dictionary to store the current word being displayed
to_learn = {}  # Dictionary to store the words to learn

# Attempt to load the words to learn, or fall back to the original list if not found
try:
    data = pandas.read_csv("./data/words_to_learn.csv")  # Reading the CSV file containing words to learn
    to_learn = data.to_dict(orient="records")  # Converting the CSV data into a list of dictionaries
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")  # If the words_to_learn.csv is not present
    to_learn = original_data.to_dict(orient="records")

# ----------------------------------------------------------- CARD TRANSITIONS ------------------------------------------------------------------ #

def next_card():
    """
    Selects the next random word from 'to_learn' and updates the card with the French word.
    Cancels the previous 'flip' timer and sets a new one to flip the card after 3 seconds.
    """
    global current_card, flip
    window.after_cancel(flip)  # Cancel the previously scheduled flip action
    current_card = random.choice(to_learn)  # Choose a random word from the list
    canvas.itemconfig(card_title, text="French", fill="black")  # Set the title to 'French'
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")  # Display the French word
    canvas.itemconfig(card_background, image=card_front)  # Set the card's background to the front image
    flip = window.after(3000, func=flip_card)  # Schedule the card to flip after 3 seconds

def flip_card():
    """
    Flips the card to show the English translation of the current French word.
    Updates the card's background to the back image and changes the text to English.
    """
    canvas.itemconfig(card_title, text="English", fill="white")  # Change the title to 'English'
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")  # Display the English translation
    canvas.itemconfig(card_background, image=card_back)  # Set the card's background to the back image

def known_word():
    """
    Removes the current word from 'to_learn' when the user indicates they know it.
    Updates the CSV file with the remaining words.
    Proceeds to the next card.
    """
    to_learn.remove(current_card)  # Remove the known word from the list
    data = pandas.DataFrame(to_learn)  # Convert the updated list back to a DataFrame
    data.to_csv("data/words_to_learn.csv", index=False)  # Save the remaining words back to the CSV file without index
    next_card()  # Proceed to the next card

# -------------------------------------------------------------- UI SETUP ----------------------------------------------------------------------- #
window = Tk()
window.title("French Flash Cards")  # Set the window title
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  # Configure padding and background color

canvas = Canvas(width=800, height=526)  # Create a canvas to display the flashcards
card_front = PhotoImage(file="./images/card_front.png")  # Load the front image of the card
card_back = PhotoImage(file="./images/card_back.png")  # Load the back image of the card
card_background = canvas.create_image(400, 263, image=card_front)  # Set the initial card image to the front
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))  # Placeholder for the card title (language)
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))  # Placeholder for the word to be displayed
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)  # Remove the border highlight and set the background color
canvas.grid(row=0, column=0, columnspan=2)  # Position the canvas on the grid

cross_img = PhotoImage(file="./images/wrong.png")  # Load the image for the 'wrong' button
unknown_button = Button(image=cross_img, bd=0, bg=BACKGROUND_COLOR, command=next_card)  # Create the button for 'I don't know' action
unknown_button.grid(row=1, column=0)  # Position the button on the grid

right_img = PhotoImage(file="./images/right.png")  # Load the image for the 'right' button
known_button = Button(image=right_img, bd=0, bg=BACKGROUND_COLOR, command=known_word)  # Create the button for 'I know' action
known_button.grid(row=1, column=1)  # Position the button on the grid

flip = window.after(3000, func=flip_card)  # Schedule the first card flip after 3 seconds

next_card()  # Display the first card

window.mainloop()  # Start the Tkinter event loop
