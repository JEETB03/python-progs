
# Quizzler - A Trivia Quiz Application

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Customizing the Quiz](#customizing-the-quiz)
- [Project Structure](#project-structure)
- [Modules Description](#modules-description)
  - [`main.py`](#mainpy)
  - [`question_model.py`](#question_modelpy)
  - [`quiz_brain.py`](#quiz_brainpy)
  - [`ui.py`](#uipy)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

## Overview

Quizzler is a Python-based trivia quiz application that offers a simple and engaging way to test your knowledge on various topics. The application fetches trivia questions from the [Open Trivia Database API](https://opentdb.com/) and presents them in a graphical user interface (GUI) built with Tkinter.

The quiz consists of True/False questions that are randomly selected from a database of over 150 questions. As you answer each question, the application provides immediate feedback and keeps track of your score.

## Features

- **Dynamic Question Fetching**: The application fetches questions in real-time from the Open Trivia Database API, ensuring a wide variety of topics and difficulty levels.
- **User-Friendly Interface**: Built with Tkinter, the GUI is intuitive and easy to navigate.
- **Immediate Feedback**: After each question, the app provides immediate feedback, letting you know if your answer was correct or not.
- **Score Tracking**: Your score is continuously updated and displayed throughout the quiz.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.x**: Python is required to run the application. You can download it from the [official website](https://www.python.org/).
- **Tkinter**: Tkinter is usually included with Python installations. If not, you can install it separately.

### Installation

1. **Clone the Repository**:

   First, clone the repository to your local machine using Git:

   ```bash
   git clone https://github.com/yourusername/quizzler.git
   cd quizzler
   ```

2. **Install Required Libraries**:

   Install the required Python libraries using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

   > **Note**: If the `requirements.txt` file is not provided, you can manually install the required libraries like `requests` and any other dependencies.

## Usage

### Running the Application

To start the quiz, run the `main.py` file:

```bash
python main.py
```

The application will open a new window displaying the quiz interface. You can start answering questions right away.

### Customizing the Quiz

You can customize various aspects of the quiz by modifying the API request parameters in the `data.py` file. For example, you can change the number of questions, their type (multiple choice or boolean), and difficulty level. 

Example:

```python
parameters = {
    "amount": 20,        # Number of questions
    "type": "multiple",  # Type of questions (multiple choice)
    "difficulty": "medium"  # Difficulty level
}
```

## Project Structure

The project is organized into the following files and directories:

```bash
quizzler/
│
├── main.py
├── question_model.py
├── quiz_brain.py
├── ui.py
├── data.py
├── images/
│   ├── true.png
│   └── false.png
└── README.md
```

## Modules Description

### `main.py`

The entry point of the application. It initializes the `QuizBrain` and `QuizInterface` objects, and starts the quiz.

### `question_model.py`

Defines the `Question` class, which represents a single question in the quiz. This class has two attributes: `text` (the question text) and `answer` (the correct answer).

### `quiz_brain.py`

Manages the quiz logic, including tracking the current question number, the score, and checking if the user's answer is correct. This module also handles the fetching of the next question.

### `ui.py`

Contains the `QuizInterface` class, which manages the GUI using Tkinter. It handles displaying the questions, capturing user input, and providing feedback.

## API Reference

Quizzler uses the [Open Trivia Database API](https://opentdb.com/api_config.php) to fetch trivia questions. Below is a brief explanation of the parameters used in the API request:

- **amount**: Number of questions to fetch (e.g., 10, 20, 50).
- **type**: Type of questions ("boolean" for True/False, "multiple" for multiple choice).
- **difficulty**: Difficulty level of the questions ("easy", "medium", "hard").

Example API request:

```python
parameters = {
    "amount": 10,
    "type": "boolean",
    "difficulty": "easy"
}
```

## Contributing

Contributions are welcome! If you'd like to contribute to Quizzler, please follow these steps:

1. **Fork the repository**.
2. **Create a new branch** for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. **Commit your changes**:
   ```bash
   git commit -m 'Add some feature'
   ```
4. **Push to the branch**:
   ```bash
   git push origin feature-name
   ```
5. **Submit a pull request**.

