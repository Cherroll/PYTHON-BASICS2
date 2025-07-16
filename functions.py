'''
def greet(name):
    print(f"Hello,{name}")
    
greet("Mpho")

def add(a,b):
    return a+b

result=add(8,9)
print(result)
'''
def factorial(n):
    if n ==0:
        return 1
    else:
        return n*factorial(n-1)
    
def greet(name,greeting="hello"):
    print(f"{greeting},{name}")
    
greet("Bob","Goodmorning")