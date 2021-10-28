# L09-02. Decorators - Exercise
# 02. Even Parameters

def even_parameters(function):
    def wrapper(*args):
        nums = [p for p in args if isinstance(p, int) and p % 2 == 0]
        if len(args) == len(nums):
            return function(*args)
        return "Please use only even numbers!"
    return wrapper


@even_parameters
def func():
    return "hi"


print(func())


@even_parameters
def add(a, b):
    return a + b


print(add(3, 5))
print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
