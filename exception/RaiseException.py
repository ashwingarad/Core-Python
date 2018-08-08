try:
    no = int(input('Enter number : '))
    if no <= 0:
        raise ZeroDivisionError('That is not a positive number!')
except ZeroDivisionError as z:
    print(z)

