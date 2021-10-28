# L09-02. Decorators - Exercise
# 06. HTML Tags

def tags(tag):
    def decorator(function):
        def wrapper(*args):
            string = function(*args)
            return f"<{tag}>{string}</{tag}>"
        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))

