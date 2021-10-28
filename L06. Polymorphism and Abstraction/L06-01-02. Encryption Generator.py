# L06-01. Polymorphism and Abstraction - Lab
# 02. Encryption Generator

class EncryptionGenerator:
    def __init__(self, text):
        self.text = text

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError("You must add a number.")

        encrypted_text = ""
        for char in self.text:
            encrypted_ord = ord(char) + int(other)
            if encrypted_ord < 32:
                encrypted_ord = 127 - (32 - encrypted_ord)
            elif encrypted_ord > 126:
                encrypted_ord = 31 + (encrypted_ord - 126)
            encrypted_text += chr(encrypted_ord)
        return encrypted_text


some_text = EncryptionGenerator('I Love Python!')
print(some_text + 1)
print(some_text + (-1))

example = EncryptionGenerator('Super-Secret Message')
print(example + 20)
print(example + (-52))
