# read names from a file and output them with 'Hello' prepended
# and a full stop appended.
with open('sample_input.txt') as sample_input:
    lines = sample_input.readlines()
    for line in lines:
        if line != '.':
            # print(repr(line)) # uncomment to see the newline character('\n')
            # use rstrip to remove '\n'
            print('Hello ' + line.rstrip() + '.')
