
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