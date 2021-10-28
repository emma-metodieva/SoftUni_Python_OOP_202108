# L09-02. Decorators - Exercise
# 03. Bold, Italic, Underline

def make_bold(function):
    def wrapper(*args):
        string = function(*args)
        return f"<b>{string}</b>"
    return wrapper


def make_italic(function):
    def wrapper(*args):
        string = function(*args)
        return f"<i>{string}</i>"
    return wrapper


def make_underline(function):
    def wrapper(*args):
        string = function(*args)
        return f"<u>{string}</u>"
    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
