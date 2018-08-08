def calc(a, b):
    sum = a + b
    div = a / b
    mul = a * b
    sub = a - b
    return sum, div, mul, sub

    
a, b, c, d = calc(10, 20)
print('sum = {} div = {} mul = {} sub = {}'.format(a, b, c, d))

t = calc(20, 10)
for x in t:
    print(x)    
