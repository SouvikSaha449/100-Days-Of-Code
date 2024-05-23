import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {rows.letter: rows.code for (index, rows) in nato_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = input("Enter a word: ").upper()
name_list = list(name)
output_list = [new_dict[character] for character in name_list]
print(output_list)




