from cs50 import get_string

# promt user for text
text = get_string("Text: ")

# count number of letters, words & sentences
letters = 0
words = 1
sentences = 0

for x in text:
    if x.lower() >= 'a' and x.lower() <= 'z':
        letters += 1
    elif x == ' ':
        words += 1
    elif x == '.' or x == '!' or x == '?':
        sentences += 1


# L is average number of letters per 100 words in the text
L = letters / words * 100

# S is the average number of sentences per 100 words in the text
S = sentences / words * 100

# Recall that the Coleman-Liau index is computed as 0.0588 * L - 0.296 * S - 15.8
index = round(0.0588 * L - 0.296 * S - 15.8)

# output the grade according to the below conditions
if index >= 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {index}")
