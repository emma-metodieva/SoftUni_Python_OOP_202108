# L09-01. Decorators - Lab
# 02. Vowel Filter

def vowel_filter(function):
    def wrapper():
        letters = function()
        vowels = [ch for ch in letters if ch.lower() in "ayouei"]
        return vowels
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
