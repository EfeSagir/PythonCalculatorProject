stack = []

def summation(num1,num2):
    return num1 + num2

def substraction(num1,num2):
    return (num1 - num2)

def multiplication(num1,num2):
    return num1 * num2

def division(num1,num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("Denominator Can't Be 0!")
        return None

