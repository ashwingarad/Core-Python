sum = lambda a, b:a + b

l = int(input('Enter 1st number : '))
m = int(input('Enter 2nd number : '))
print('Sum of {} and {} is {}'.format(l, m, sum(l, m)))


big = lambda a, b: a if a>b else b

a = int(input('Enter 1st number : '))
b = int(input('Enter 2nd number : '))
print('Biggest number of {} and {} is : {}'.format(a, b, big(a, b)))
