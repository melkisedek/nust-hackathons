import math
from itertools import combinations

# prime checking function by [socratica](https://youtu.be/2p3kwF04xcA)
def is_prime(n):
    """Return 'True' if 'n' is a prime number.
    False otherwise."""

    if n == 1:
        return False  # 1 is not prime

    # If's even and not 2, then it's not prime
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))

    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True


with open('sample_input.txt') as sample_input:
    lines = sample_input.readlines()
    for line in lines:
        n, k = line.strip().split()  # using tuple unpacking to assign n and k
        n, k = int(n), int(k)        # convert input strings to integers

        # Find all prime factors of n
        prime_factors = []
        # Add 1 to n, range(a, b) always ends at b-1
        for number in range(1, n+1):
            if is_prime(number):
                prime_factors.append(number)

        # Find all combinations of the prime factors k in each set/group
        # We use combinations because order doesn't matter
        # e.g 2*3*5 = 3*5*2 = 5*3*2 ...ect.
        factor_combinations = combinations(prime_factors, k)
        summing_sets = 0   # number of set that sum up to a total equal to n

        # sum all the combinations
        all_combination_sums = map(sum, factor_combinations)
        for a_combination_sum in all_combination_sums:
            if a_combination_sum == n:
                summing_sets += 1
        print(summing_sets)
