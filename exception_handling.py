def divide(x, y):
    try:
        result = x / y
        print(f'The result is {result}')
    except ZeroDivisionError:
        print("You can't divide by zero!")

divide(10, 2)
divide(5, 0)
 