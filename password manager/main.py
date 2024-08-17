from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ------------------------------------------------------------- PASSWORD GENERATOR -------------------------------------------------------------- #
def generate_password():
    """
    Generates a random password with a mix of letters, numbers, and symbols. 
    The password is then inserted into the password entry field and copied to the clipboard.
    """
    # List of possible characters for the password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Randomly choose the number of each type of character
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # Generate random characters from each category
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    # Combine all selected characters
    password_list = password_letters + password_symbols + password_numbers

    # Shuffle the combined list to ensure randomness
    random.shuffle(password_list)

    # Join the list into a string
    password = "".join(password_list)

    # Insert the generated password into the password entry field
    password_entry.insert(0, password)
    
    # Copy the generated password to the clipboard
    pyperclip.copy(password)

# --------------------------------------------------------------- SAVE PASSWORD ----------------------------------------------------------------- #
def save():
    """
    Saves the website, username/email, and password to a text file.
    Prompts the user for confirmation before saving. 
    Clears the website and password fields after saving.
    """
    # Retrieve the data from the input fields
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    
    # Check if any field is empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        # Confirm the details with the user
        is_yes = messagebox.askyesno(title=website, message=f"These are the details you entered: \nUsername: {user}\nPassword: {password}\nAre you sure to save this information?")
        
        # If the user confirms, save the details to the file
        if is_yes:
            with open("password manager/data.txt", "a") as data_file:
                data_file.write(f"{website} | {user} | {password}\n")
                
                # Clear the website and password fields
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ------------------------------------------------------------------ UI SETUP ------------------------------------------------------------------- #

# Initialize the main window
window = Tk()
window.title("Jeet's Password Manager")
window.config(padx=50, pady=50)

# Create and place the canvas with the logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="encrypted.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3)

# Define and place labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e")
user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0, sticky="e")
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e")

# Define and place entry fields
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()  # Focus cursor on the website entry field

user_entry = Entry(width=35)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, "jeet@email.com")  # Pre-populate with a default email

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="w")

# Define and place buttons
generate_pass_button = Button(text="Generate Password", width=14, command=generate_password)
generate_pass_button.grid(row=3, column=2, sticky="w")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=10)

# Start the main loop
window.mainloop()
