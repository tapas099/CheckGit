def add_this(a:int,b:int)->int:
    return a+b

print(add_this(2,3))
print(add_this('Good','Morning'))

# type hints. If we check in terminal with mypy we will see the difference but in console it will run fine.
# Run with Flake8 to know the Python coding standard error.