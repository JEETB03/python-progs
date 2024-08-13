import pandas

data = pandas.read_csv("NATO-alphabet-start/nato_phonetic_alphabet.csv")
# 

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ")
word = word.upper()
phonetic_code = [nato_dict[letter] for letter in word]
print(phonetic_code)  # Output: ['ALFA', 'BRAVO']

