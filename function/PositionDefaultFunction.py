def fn (a, b, c = 1):
    return a * b + c

print (fn(1, 2))                # returns 3, positional and default.
print (fn(1, 2, 3))             # returns 5, positional.
print (fn(c = 5, b = 2, a = 2)) # returns 9, named.
print (fn(b = 2, a = 2))        # returns 5, named and default.
print (fn(5, c = 2, b = 1))     # returns 7, positional and named.
print (fn(8, b = 0))            # returns 1, positional, named and default.
