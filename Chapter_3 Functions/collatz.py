def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(number * 3 + 1)
        return number * 3 + 1

print('Enter number:')
while True:
    try:
        userInput = input()
        while(userInput != 1):
            userInput = collatz(int(userInput))
        break
    except ValueError:
        print('You must enter an integer')