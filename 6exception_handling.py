# 28-33 try, except, else, finally, raise, assert
try:
    x = int("abc")
except ValueError:
    print("Conversion error")
else:
    print("Success")
finally:
    print("Done")

raise ValueError("Custom error")

x = 5
assert x > 0, "x must be positive"
