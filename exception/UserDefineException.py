class TooYoungException(RuntimeError):

    def __init__(self, msg):
        self.msg = msg

        
class TooOldException(RuntimeError):

    def __init__(self, msg):
        self.msg = msg

        
while True:
    try:
        no = int(input("Enter a number: "))
        if no < 18:
            raise TooYoungException("Age should be greater than 18")
        elif no > 60:
            raise TooOldException("Age should be less than 60")
        break
    except TooYoungException as ty:
        print(ty, end = '\n\n')

    except TooOldException as to:
        print(to, end = '\n\n')
