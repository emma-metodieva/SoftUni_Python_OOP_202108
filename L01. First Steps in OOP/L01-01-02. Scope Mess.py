# L01-01. First Steps in OOP - Lab
# 02. Scope Mess

x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x  # alter row 4
        x = "nonlocal"
        print("inner:", x)  # row 3

    def change_global():
        global x  # alter row 5
        x = "global: changed!"

    print("outer:", x)  # row 2
    inner()  # row 3
    print("outer:", x) # row 4
    change_global()  # alter row 5


print(x)  # row 1
outer()
print(x)  # row 5
