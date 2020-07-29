def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y==0:
        raise ValueError('Divide by zero error')
    return x/y

# result=add(20,50)
# print(result)