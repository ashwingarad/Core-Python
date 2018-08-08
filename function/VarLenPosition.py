def sum (*n, name):
    s = 0
    for x in n:
        s += x
        
    print('Addition performed by {} and sum is {}'.format(name, s))


sum(10, name="Ashwin")
sum(70, 60, 50, name="Ashwin")
