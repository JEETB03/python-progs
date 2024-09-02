from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    """
    A class to manage the quiz user interface.

    Attributes:
    ----------
    quiz : QuizBrain
        The QuizBrain object managing the quiz logic.
    window : Tk
        The main window of the Tkinter application.
    score_label : Label
        A label to display the user's current score.
    canvas : Canvas
        A canvas to display the question text.
    question_text : int
        The ID of the text item on the canvas.
    true_button : Button
        The button for answering 'True'.
    false_button : Button
        The button for answering 'False'.
    """

    def __init__(self, quiz_brain: QuizBrain):
        """
        Initializes the QuizInterface with the provided QuizBrain object.

        Parameters:
        ----------
        quiz_brain : QuizBrain
            The QuizBrain object to be used for managing quiz logic.
        """
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Questions Bitch!", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")

        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """
        Fetches and displays the next question in the quiz. Disables buttons if the quiz is over.
        """
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        """
        Handles the event when the 'True' button is pressed.
        """
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        """
        Handles the event when the 'False' button is pressed.
        """
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        """
        Provides feedback to the user based on whether their answer was correct.

        Parameters:
        ----------
        is_right : bool
            True if the user's answer was correct, False otherwise.
        """
        if is_right:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)