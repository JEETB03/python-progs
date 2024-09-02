import html

class QuizBrain:
    """
    A class to manage the quiz logic.

    Attributes:
    ----------
    question_number : int
        The current question number.
    score : int
        The current score of the user.
    question_list : list
        The list of questions in the quiz.
    current_question : Question
        The current question being asked.
    """

    def __init__(self, q_list):
        """
        Initializes the QuizBrain with a list of questions.

        Parameters:
        ----------
        q_list : list
            A list of Question objects to be used in the quiz.
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """
        Checks if there are still questions remaining in the quiz.

        Returns:
        -------
        bool
            True if there are questions remaining, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Retrieves the next question and returns it in a formatted string.

        Returns:
        -------
        str
            The formatted question text.
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)  # Un-escapes any HTML entities in the question text.
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        """
        Checks the user's answer against the correct answer and updates the score.

        Parameters:
        ----------
        user_answer : str
            The user's answer to the question.

        Returns:
        -------
        bool
            True if the user's answer is correct, False otherwise.
        """
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False