# Note: This program will not give the correct output when 
# given irregular adjectives such as 'bad','good' or those that
# require the last letter to be repeated such as 'fat'.
with open('sample_input.txt') as sample_input:
    lines = sample_input.readlines() # read all lines in the file
    for line in lines:
        line = line.strip() # remove newline character '\n'
        # line ends in 'est', don't modify
        if line[-3:] == 'est':
            print(line)
        # line ends in 'er', replace 'er' with 'est
        elif line[-2:] == 'er':
            line = line[:-2] + 'est' # observe the position of the ':'
            print(line)
        # line ends in 'e', add 'r'
        elif line[-1:] == 'e':
            line = line+'r'
            print(line)
        else:
        # add 'er'
            print(line+'er')
