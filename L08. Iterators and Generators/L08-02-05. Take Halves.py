# L08-02. Iterators and Generators - Exercise
# 05. Take Halves

import itertools


def solution():
    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        return list(itertools.islice(seq, n))

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(10, halves()))
