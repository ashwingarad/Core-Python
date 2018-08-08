def outer(num1):

    def inner_increment(num1):  # hidden from outer code
        return num1 + 1

    num2 = inner_increment(num1)
    print(num1, num2)


outer(10)
