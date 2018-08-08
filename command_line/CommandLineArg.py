import sys

print("Name of script : ", sys.argv[0])
print("number of arguments : ", len(sys.argv))
print("Argument list : ", str(sys.argv))

arguments = sys.argv[1:]
print(arguments)