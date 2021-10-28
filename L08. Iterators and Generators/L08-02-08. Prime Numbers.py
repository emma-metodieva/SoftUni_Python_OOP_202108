# L08-02. Iterators and Generators - Exercise
# 08. Prime Numbers

def get_primes(nums):
    nums_to_check = [n for n in nums if n > 1]
    for n in nums_to_check:
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
