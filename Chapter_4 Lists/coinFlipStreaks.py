import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    values = []
    for i in range(100):
        string = 'heads' if random.randint(0, 1) == 0 else 'tails'
        values.append(string)

    # Code that checks if there is a streak of 6 heads or tails in a row.
    streak = 0
    for j in range(len(values) - 1):
        if values[j] == values[j + 1]:
            streak += 1
        else:
            streak = 0
        
        if streak == 6:
            numberOfStreaks += 1
            streak = 0
        
print('Chance of streak: %s%%' % (numberOfStreaks / 100))