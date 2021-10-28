# L05-01. Class and Static Methods - Lab
# 03. Integer

from math import floor


class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if isinstance(float_value, float):
            return cls(floor(float_value))
        return "value is not a float"

    @classmethod
    def from_roman(cls, value):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(value)):
            if i > 0 and roman[value[i]] > roman[value[i - 1]]:
                result += roman[value[i]] - 2 * roman[value[i - 1]]
            else:
                result += roman[value[i]]
        return cls(result)

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str):
            return cls(int(value))
        return "wrong type"


first_num = Integer(10)
second_num = Integer.from_roman("IV")

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
