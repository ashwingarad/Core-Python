import random

print('random() : ', random.random())
print('uniform() : ', random.uniform(10, 50))
print('randrange() : ', random.randrange(10, 100, 6))
print('randint() : ', random.randint(20,50))

random.seed()
print ("random number with default seed", random.random())
random.seed(52)
print ("random number with int seed", random.random())
random.seed("hello", 1)
print ("random number with string seed", random.random())

l = [10, 20, 30, 40, 50, 60]
print('List before shuffle : ', l)
random.shuffle(l)
print('List After shuffle : ', l)

print('choice()', random.choice(l))
