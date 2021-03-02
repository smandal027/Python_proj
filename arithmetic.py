def arithm_add(x,y):
    print('Addition ->', x + y)

def arithm_subtract(x, y):
    print('Subtraction ->', x - y)

def arithm_mult(x, y):
    print('Multiply ->', x * y)
try:
    def arithm_div(x, y):
        print('Divide ->', x / y)
except ZeroDivisionError as ze:
    print('ZE Occurred ->', ze)