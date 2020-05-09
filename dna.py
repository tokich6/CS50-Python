import csv
import sys
import re

# provide 2 command line arguments - a CSV file, second is a text file
if len(sys.argv) != 3:
    sys.exit("Please provide valid command-line arguments")


# create a list containing the csv file headings (all but the first)
def createList():
    with open(sys.argv[1], newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        csv_headings = next(reader)
        csv_headings.pop(0)
    return csv_headings


list = createList()


# open and read the text file, containg the sequences

f = open(sys.argv[2])
contents = f.read()


# define a function to count max number of consecutive STR sequences(sub_str) - (regular expression used)

def maxRepeating(str, sub_str):
    groups = re.findall(rf'(?:{sub_str})+', str)
    largest = max(groups, key=len)
    # divide the length of the group by the length of the sub_str to get the max number of time repeated consecutively
    return (len(largest) // len(sub_str))


# create a dictionary from the list and assign all values to 0 initially

dic = dict.fromkeys(list, 0)


# populate the dic values with the max_number of str consecutive sequences
for key in dic:
    dic[key] = maxRepeating(contents, key)


# open and read the csv file database as a dictionary

with open(sys.argv[1], newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    for people in map(dict, reader):
        match = 0
        # compare each person's dna sequences in the database to the str sequence
        for dna in dic:
            if dic[dna] == int(people[dna]):
                match += 1
        if match == len(dic):
            sys.exit(people['name'])
    print("No match")
