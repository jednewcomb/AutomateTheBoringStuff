import time, sys

#good example of using a boolean to accomplish a task cleanly
def printSpacesStars(number):
    print(' ' * number, end = '')
    print('********')

indent = 0
indentIncreasing = True

while True:
    try:
        if indentIncreasing:
            printSpacesStars(indent)
            indent += 1
            time.sleep(0.01)

            if indent >= 20:
                indentIncreasing = False

        else:
            printSpacesStars(indent)
            indent -= 1
            time.sleep(0.01)

            if indent <= 0:
                indentIncreasing = True
    except KeyboardInterrupt:
        sys.exit()