# L08-02. Iterators and Generators - Exercise
# 02. Dictionary Iterator

class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.pairs = [(k, self.dictionary[k]) for k in self.dictionary]
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.dictionary):
            raise StopIteration
        temp = self.idx
        self.idx += 1
        return self.pairs[temp]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

# my_dict = {1: "1", 2: "2"}
# pairs = [(k, my_dict[k]) for k in my_dict]
# print(pairs[0])
