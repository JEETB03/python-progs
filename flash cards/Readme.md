The "French Flash Cards" application is a simple educational tool built using Python's Tkinter library. It allows users to learn French vocabulary by displaying a French word on a flashcard. After 3 seconds, the card automatically flips to reveal the English translation. Users can indicate whether they know the word or not, and the program will adapt by removing known words from the learning list.

Key Features:
Flashcard Display:

Displays a French word on the card.
Flips the card to show the English translation after 3 seconds.
Word Management:

Keeps track of words that the user knows and removes them from the learning list.
Saves progress by updating a CSV file with the words left to learn.
Error Handling:

Handles file not found errors gracefully by falling back to the original word list if the progress file is missing.
Core Functions:
next_card(): Handles the selection of the next word to display and schedules the card flip.
flip_card(): Flips the flashcard to reveal the English translation.
known_word(): Removes the current word from the learning list and saves the progress.
User Interface:
Canvas: The central component displaying the flashcards.
Buttons:
"I don't know" button to move to the next card.
"I know" button to remove the current card from the learning list.
Error Handling:
The application checks for the existence of a progress file (words_to_learn.csv). If the file does not exist, it initializes the learning process using the original data set.