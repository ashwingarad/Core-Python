class NegativeNumberException(RuntimeError):
    pass

try:
    n = int(input('Enter number : '))
    if n < 0:
        raise NegativeNumberException('Negative number not allowed')    
    else:
        print(10 / n)
except NegativeNumberException as ne:
    print(ne)
except ArithmeticError as a:
    print(a)
