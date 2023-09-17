def factorial(number_parameter):
    if number_parameter == 1:
        return 1
    else:
        return number_parameter * factorial(number_parameter - 1)
print(factorial(4))
