# L08-01. Iterators and Generators - Lab
# 03. Vowels

class vowels:
    def __init__(self, string):
        self.string = string
        self.vowels = 'ayouei'
        self.string_vowels = [ch for ch in self.string if ch.lower() in self.vowels]
        self.start = 0
        self.end = len(self.string_vowels) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        idx = self.start
        self.start += 1
        return self.string_vowels[idx]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
