# 17-22 def, return, lambda, global, nonlocal, yield

def add(a, b):
    return a + b

print(add(2, 3))

square = lambda x: x * x
print(square(4))

x = 10
def show():
    global x
    x = 20
show()
print(x)

def outer():
    y = 5
    def inner():
        nonlocal y
        y = 10
    inner()
    print(y)
outer()

def generator():
    yield 1
    yield 2

for v in generator():
    print(v)
