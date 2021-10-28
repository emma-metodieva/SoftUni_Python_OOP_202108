# L08-02. Iterators and Generators - Exercise
# 04. Sequence Repeat

class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.idx = 0
        self.count = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > self.number:
            raise StopIteration
        temp = self.idx
        self.idx += 1
        if self.idx == len(self.sequence):
            self.idx = 0
        self.count += 1
        return self.sequence[temp]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
