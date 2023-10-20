import pandas as pd

# Read the NATO phonetic alphabet data from a CSV file
df = pd.read_csv("nato_phonetic_alphabet.csv")

# Prompt the user for input and convert it to uppercase
input_text = input("Enter a word: ").upper()

# Create a list of phonetic codes for each letter in the input word
phonetic_codes = [df[df['letter'] == letter]["code"].values[0] for letter in input_text]

# Print the phonetic codes
print(phonetic_codes)
