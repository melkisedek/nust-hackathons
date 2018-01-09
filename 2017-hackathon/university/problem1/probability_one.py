import math

with open('sample_input.txt') as sample_input:
    lines = sample_input.readlines()
    count = 1
    for line in lines:
        n0 = line.strip()  # remove newline character, step 1
        n0 = int(n0)       # convert n0 to an integer
        odd_or_even = ''   # a string to tell if a number is odd or even

        # Stop looping, 0 or smaller number encountered
        if n0 <= 0:
            break    # stop the for loop

        # Number is above threshold 1,000,000
        if n0 > 1000000:
            break

        n1 = 3 * n0

        if n1 % 2 == 0:
            odd_or_even = 'even'
            n2 = n1 / 2
        else:
            odd_or_even = 'odd'
            n2 = (n1 + 1) / 2

        n3 = 3 * n2
        n4 = n3 / 9
        
        # math.floor() ignores decimal places
        print(count, odd_or_even, math.floor(n4))
        count += 1   # increase the count by 1
