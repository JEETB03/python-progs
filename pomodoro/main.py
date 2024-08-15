from tkinter import *               # Importing all classes and functions from tkinter module.
import math                        # Importing math module for mathematical operations.

# ---------------------------- CONSTANTS ------------------------------- #

# Define color constants for the UI
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Initialize variables
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    """
    Reset the timer by canceling the current countdown, resetting the timer display, 
    and setting the title and check marks to their initial states.
    """
    window.after_cancel(timer)  # Cancel the scheduled timer callback
    canvas.itemconfig(timer_text, text="00:00")  # Reset timer display to "00:00"
    title_label.config(text="Timer")  # Set the title label back to "Timer"
    check_marks.config(text="")  # Clear the check marks
    global reps
    reps = 0  # Reset the repetition counter

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    """
    Start the timer with the appropriate duration based on the current repetition count.
    It determines whether to start a work session, short break, or long break.
    """
    global reps
    reps += 1  # Increment the repetition count
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec)  # Start a long break
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)  # Start a short break
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)  # Start a work session
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    """
    Countdown timer function that updates the timer display every second.
    When the countdown reaches zero, it restarts the timer and updates check marks.
    
    :param count: Remaining time in seconds for the countdown.
    """
    count_min = math.floor(count / 60)  # Calculate minutes
    count_sec = count % 60  # Calculate seconds
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"  # Format seconds with leading zero if necessary
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  # Update timer display
    
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # Schedule the countdown to update every second
    else:
        start_timer()  # Restart the timer when countdown reaches zero
        mark = ""
        work_session = math.floor(reps / 2)  # Calculate the number of completed work sessions
        for _ in range(work_session):
            mark += "✔️"  # Add a check mark for each completed work session
        check_marks.config(text=mark)  # Update the check marks display

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()  # Create the main application window
window.title("Pomodoro Timer 🍅")  # Set the window title
window.config(padx=100, pady=50, bg=YELLOW)  # Configure window padding and background color

# Create and place the title label
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# Create and place the canvas with the tomato image and timer text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="pomodoro/tomato.png")  # Load the tomato image
canvas.create_image(100, 112, image=tomato_image)  # Place the image on the canvas
timer_text = canvas.create_text(100, 130, text="00:00", fill="White", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Create and place the start button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Create and place the reset button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Create and place the check marks label
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


# Start the Tkinter event loop
window.mainloop()