class Calc:

    def addition(self, a, b=0, c=0):
        return a + b + c

#     def addition(self, *n):
#         sum = 0
#         for x in n:
#             sum += x
#         return sum


c = Calc()
print(c.addition(10, 30))
print(c.addition(40, 30, 20))

