def collatz(number):
    if (number % 2): # number is odd
        print(3 * number + 1)
        return 3 * number + 1
    else: # number is even
        print(number // 2)
        return number // 2
    
while True:
    try:
        integer = int(input())
        retNumber = collatz(integer)
        if retNumber == 1:
            break
    except ValueError:
        print('You must input an integer value!!!')

