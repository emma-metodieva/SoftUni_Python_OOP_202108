# L08-01. Iterators and Generators - Lab
# 06. Reverse String

def reverse_text(string):
    idx = len(string) - 1
    while idx >= 0:
        yield string[idx]
        idx -= 1


for char in reverse_text("step"):
    print(char, end='')
