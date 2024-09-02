class Question:
    """
    A class to represent a quiz question.
    
    Attributes:
    ----------
    text : str
        The text of the quiz question.
    answer : str
        The correct answer to the quiz question.
    """

    def __init__(self, q_text, q_answer):
        """
        Initializes a Question object with the provided text and answer.

        Parameters:
        ----------
        q_text : str
            The text of the quiz question.
        q_answer : str
            The correct answer to the quiz question.
        """
        self.text = q_text
        self.answer = q_answer