from cs50 import get_float

# prompt for change owed, keep prompting if a negative number
while True:
    change = get_float("Change owed: ")
    if change > 0:
        break

# round cents in hundreds
cents = round(change * 100)

# initialize coins variable, to keep track of number of coins to be returned
coins = 0

# keep substacting from cents until none left while adding to coins
while True:
    if cents >= 25:
        cents -= 25
        coins += 1
    elif cents >= 10:
        cents -= 10
        coins += 1
    elif cents >= 5:
        cents -= 5
        coins += 1
    elif cents >= 1:
        cents -= 1
        coins += 1
    elif cents == 0:
        break
# print the number of coins needed to be returned
print(coins)

