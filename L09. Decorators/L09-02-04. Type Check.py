# L09-02. Decorators - Exercise
# 04. Type Check

def type_check(data_type):
    def decorator(function):
        def wrapper(data):
            if isinstance(data, data_type):
                return function(data)
            return "Bad Type"
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
