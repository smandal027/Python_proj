class InvalidInput(Exception):
    def __init__(self):
        self.__err_msg = 'User has entered invalid input ->'

    def display_err_msg(self):
        return self.__err_msg
try:
    num=int(input('Enter a number->'))
    if num <= 0:
        raise InvalidInput
    else:
        a, b = 0, 1
    while a < num:
        print(a, end=',')
        a, b = b, a+b
    print()
except InvalidInput as ivi:
    print(ivi.display_err_msg(),num)



