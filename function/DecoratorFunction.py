def dec(func):

    def inner(time):
        t = abs(time)
        if t >= 12 and t < 16:
            print('Good Afternoon')
        elif t >= 16 and t < 19:
            print('Good Evening')
        elif t >= 19 and t < 24:
            print('Good night')
        else:
            func(time)

    return inner


@dec
def wish(time):
    print("Good Morning... it's time is {}".format(time))

    
tm = round(eval(input('Enter time in 24hrs format : ')))
wish(tm)
