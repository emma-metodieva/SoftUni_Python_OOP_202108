# L08-02. Iterators and Generators - Exercise
# 07. Reader

def read_next(*args):
    for iterable in args:
        for element in iterable:
            yield element


for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')
