c = 0  # global variable


def add():
    global c
    c = c + 2  # increment by 2
    print("Inside add:", c)


add()
print("In main:", c)


def outer():
    x = 20
    def inner():
        global x
        x = 25
    
    print("Before calling inner: ", x)
    inner()
    print("After calling inner: ", x)


outer()
print("x in main : ", x)
