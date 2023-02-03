names = ["omar","farook"]

for name in names:
    print(name)

def sum(x,y):
    result = [x+y, x-y, x*y, x/y]
    return result



value = sum(20,2)
print(value)

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 10
print("The factorial of", num, "is", factorial(num))