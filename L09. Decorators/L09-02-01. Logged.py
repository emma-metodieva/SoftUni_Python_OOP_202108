# L09-02. Decorators - Exercise
# 01. Logged

def logged(function):
    def wrapper(*args):
        call = f"you called {function.__name__}{args}"
        result = f"it returned {function(*args)}"
        return f"{call}\n" \
               f"{result}"
    return wrapper


# @logged
# def func(*args):
#     return 3 + len(args)
#
#
# print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
