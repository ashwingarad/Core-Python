def outer():
	print('Outer function call')    

	def inner():
		print('Inner function call')    

	print('Outer Function return inner function')	
	return inner

f1 = outer()
print(f1)
f1()
