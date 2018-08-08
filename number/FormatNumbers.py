num = 132489893342325

print("{:,}".format(num))
print("Integer number : {} ".format(123))
print("Integer number : {:d} ".format(123))
print("Integer number : {:5d} ".format(123))
print("Integer number : {:05d} ".format(123))

print('\nFloat Number : {}'.format(123.4567))
print('Float Number : {:f}'.format(123.4567))
print('Float Number : {:8.3f}'.format(123.4567))
print('Float Number : {:08.3f}'.format(123.4567))
print('Float Number : {:08.3f}'.format(123.45))
print('Float Number : {:08.3f}'.format(789456123.456))

# if total number is < 8 position then 0 will be placed in MSB's
# if total number is > 8 positions then integral digits will be consider.
# The Extra digits we can take only 0.

print("\nBinary number : {0:b} ".format(153))
print("Octal number : {0:o} ".format(153))
print("Hexa number : {0:X} ".format(154))

# We can take only int values in binary, octal and hexa-decimal.

print('\n{:05d}'.format(12))
print('{:5}'.format('rat'))
print('Right Alignment :{:>5}'.format('rat'))
print('Left Alignment :{:<5}'.format('rat'))
print('Center Alignment :{:^5}'.format('rat'))
print('Center Alignment :{:*^5}'.format('rat'))

print('\n{:.3}'.format('pythonsoftware'))
print('Right Alignment and Truncation :{:>5.3}'.format('pythonsoftware'))
print('Left Alignment and Truncation :{:<5.3}'.format('pythonsoftware'))
print('Center Alignment and Truncation :{:^5.3}'.format('pythonsoftware'))
print('Center Alignment and Truncation :{:*^5.3}'.format('pythonsoftware'))

a, b, c = 10, 20, 30
print('\nFirst = %i Second = %i and Third = %i' % (a, b, c))

name = 'Ashwin'
salary = 32000
addr = 'Pune'
print('\nHello {0}, Your Salary is {1} and You are living in {2}'.format(name, salary, addr))
print('Hello {}, Your Salary is {} and You are living in {}'.format(name, salary, addr))
print('Hello {z}, Your Salary is {x} and You are living in {y}'.format(z=name, x=salary, y=addr))

# Dynamic String Formatting
print('\nDynamic String Formatting')
st = '{:{fill}{align}{width}}'
print(st.format('Python', fill='*', align='<', width='10'))
print(st.format('Python', fill='*', align='>', width='10'))
print(st.format('Python', fill='*', align='^', width='10'))
print(st.format('Python', fill='*', align='^', width='5'))

# Dynamic Float Formatting
print('\nDynamic Float Formatting')
st = '{:{align}{width}.{precision}}'
print(st.format(123.678, align='<', width='10', precision=2))
print(st.format(123.678, align='>', width='10', precision=2))
print(st.format(123.678, align='^', width='10', precision=2))
print(st.format(123.678, align='^', width='5', precision=2))

# Dynamic Date Time Formatting
print('\nDynamic Date Time Formatting')
import datetime
date = datetime.datetime.now()
print('Its now: {:%d/%m/%Y  %H:%M:%S}'.format(date))

# Dynamic Complex number Formatting
print('\nDynamic Complex number Formatting')
complexNo = 1 + 2j
print('Real number : {0.real} and Imaginary : {0.imag}'.format(complexNo))
