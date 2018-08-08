def calc(x):
    z = 10

    def twice():
        nonlocal z
        z *= 20

    twice()
    twice()
    twice()
    return z + 10


# Prints 80010
print(calc(10))
