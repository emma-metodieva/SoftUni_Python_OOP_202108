# L08-02. Iterators and Generators - Exercise
# 01. Take Skip

class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = 1
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.count:
            raise StopIteration
        temp = self.num
        self.num += self.step
        self.start += 1
        return temp


# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)

