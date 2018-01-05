from functools import lru_cache


# use least-recently-used cache optimization
@lru_cache(maxsize = 1000)
def fibonacci(n):
    """Returns the (fibonacci) rabbit sequence with the first pair as `1` and
    the second pair as `10`. All subsequent pairs are concaternations."""

    # Check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive inter")
    if n < 0:
        raise ValueError("n must be a positive int")

    # Compute the Nth term
    if n == 0:
        return '0'  # 0
    elif n == 1:
        return '1' # 1
    elif n == 2:
        return '10' # 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


with open('sample_input.txt') as sample_input:
    lines = sample_input.readlines()
    for line in lines:
        try:
            month = int(line.rstrip())
            if month == 0:
                print('The {0}th Rabbit Sequence is :'.format(month))
            if month == 1:
                print('The {0}st Rabbit Sequence is :'.format(month))
            if month == 2:
                print('The {0}nd Rabbit Sequence is :'.format(month))
            if month == 3:
                print('The {0}rd Rabbit Sequence is :'.format(month))
            if month >= 4:
                print('The {0}th Rabbit Sequence is :'.format(month))

            print(fibonacci(month))

        except ValueError as error:
            print(error)
