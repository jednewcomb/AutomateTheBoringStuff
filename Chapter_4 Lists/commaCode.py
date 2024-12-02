def addComma(item):
    returnString = ''
    if item != []:
        for i in range(len(item) - 1):
            returnString += item[i] + ', '
        returnString += 'and ' + item[-1]        
    else:
        returnString += "Empty list passed"
    return returnString

print(addComma([]))


# A common Python technique is to use range(len(someList)) with a for loop to iterate over the indexes of a list. For example,
# enter the following into the interactive shell:

#>>> supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
#>>> for i in range(len(supplies)):
#...     print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# Index 0 in supplies is: pens
# Index 1 in supplies is: staplers
# Index 2 in supplies is: flamethrowers
# Index 3 in supplies is: binders