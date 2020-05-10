import sys
import csv
from cs50 import SQL

# open file as db
db = SQL("sqlite:///students.db")

# if csv file not provided as command-line arg for the program, exit the program
if len(sys.argv) != 2:
    sys.exit("Please provide valid command-line arguments")

# open the csv file provided as a command line arg
with open(sys.argv[1], newline='') as students:

    # create dictreader
    reader = csv.DictReader(students, delimiter=",")
    # iterate over each row(student) and insert into the student table (which has already been created inside the students database)
    for student in reader:

        # split the name from csv file into first, middle(if any) and last name
        name = student['name']
        splitName = name.split()
        if len(splitName) != 3:
            first = splitName[0]
            middle = None
            last = splitName[1]
        else:
            first = splitName[0]
            middle = splitName[1]
            last = splitName[2]

        house = student['house']
        birth = student['birth']

        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)",
                   first, middle, last, house, birth)
