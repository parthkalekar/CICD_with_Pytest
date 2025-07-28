def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1 * num2

def div(num1,num2):
    if num2==0:
        raise ValueError("cannot divide by 0")
    else:
        return num1/num2
    
def power(num1,num2):
    return num1**num2

def sqrt(num):
    if num < 0:
        raise ValueError("cannot take square root of negative number")
    return num**0.5


