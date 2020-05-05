from cs50 import get_int

# ask until you get a number between 1 and 8
while True:
    height = get_int("Height: ")
    if height in range(1,9):
        break
# logic for printing the hashes
for i in range(height):
    for j in range(height):
        if (j+i) < (height-1):
            print(" ", end="")
        else:
            print("#", end="")
    print()
