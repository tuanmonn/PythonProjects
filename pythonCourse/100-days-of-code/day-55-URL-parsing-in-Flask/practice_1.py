# Create a logging_decorator() which is going to log the name of the function that was called, the arguments it was given and finally the returned output.

# my answer
# decorator function
def logging_decorator(function):
    def wrapper(*args, **kwargs):
        result = function(args[0],args[1],args[2])
        function_name = function.__name__
        print(f'You called {function_name}{args[0],args[1],args[2]}\nIt returned: {result}')
    return wrapper

@logging_decorator
def a_function(num1,num2,num3):
    return num1+num2+num3

a_function(1,2,3)

# class answer
# def logging_decorator(function):
#     def wrapper(*args, **kwargs):
#         result = function(args[0],args[1],args[2])
#         print(f'You called {function.__name__}{args}\nIt returned: {result}')
#     return wrapper
#
# @logging_decorator
# def a_function(num1,num2,num3):
#     return num1+num2+num3
#
# a_function(1,2,3)