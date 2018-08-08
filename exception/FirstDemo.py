try:
    n = 10/0
except Exception as e :
    print(e)  
finally:
    print('Finally block')