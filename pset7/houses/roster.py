import sys
from cs50 import SQL

# open file as db
db = SQL("sqlite:///students.db")

# if house not provided as command-line arg for the program, exit the program
if len(sys.argv) != 2:
    sys.exit("Please provide valid command-line arguments")

# save the arg provided as a variable
house = sys.argv[1]

# query database for all students in that particular house, sorted by last name (db.execute SELECT returns a list of dict, saved as a roster)
roster = db.execute("SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last", (house,))

# iterate over roster and print each student full name and birth on their own line (formatted as, e.g., Harry James Potter, born 1980 or Luna Lovegood, born 1981).
for student in roster:

    if student['middle'] == 'None':
        print(f"{student['first']} {student['last']}, born {student['birth']}")
    else:
        print(f"{student['first']} {student['middle']} {student['last']}, born {student['birth']}")
