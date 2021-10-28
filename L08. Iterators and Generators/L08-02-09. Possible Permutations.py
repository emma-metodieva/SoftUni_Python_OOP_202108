# L08-02. Iterators and Generators - Exercise
# 09. Possible Permutations

def all_permutations(seq):
    if len(seq) <= 1:
        return [seq]

    res = []
    for e in seq:
        temp = seq[:]
        temp.remove(e)
        res.extend([[e] + r for r in all_permutations(temp)])
    return res


def possible_permutations(seq):
    perms = all_permutations(seq)
    for perm in perms:
        yield perm


[print(n) for n in possible_permutations([1, 2, 3])]
