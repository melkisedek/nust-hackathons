# The Rabbit Sequence

## Problem Description

You have probably already learned about the Fibonacci sequence; 
that is the series of numbers that runs

    1, 1, 2, 3, 5, 8, 13, 21, ...

In other words, the Fibonacci sequence is define by fib(n) where 

    fib(n) = 1 (if n=1 or n=2) or
    fib(n) = fib(n - 1) + fib(n - 2) (if n > 2)
Let's take a look at where Fibonacci actually came up with this sequence.

The original problem that he was considering was a mathematical model for the rabbit population in a given area under ideal conditions.
Fibonacci assumed that each pair of rabbits could produce a new pair every month,
except for the first month of their life 
(i.e, rabbits are mature enough to produce offspring from the second month onwards).
If you place a single pair of rabbits in a field, 
then the number of rabbits each month will follow the Fibonacci sequence.

- Start: One pair of rabbits placed in the field
- Month 1: Rabbits mature. Total pairs: 1
- Month 2: New pair of rabbits born. Total pairs: 2
- Month 3: New pair matures. Another pair born to the original pair. Total pairs: 3
- Month 4: One pair matures. Two new pairs born to first two pairs. Total pairs: 5
- And so on...

If we now, instead of just looking at the number of pairs, look at the ages of the pairs.
Let's call pairs in their first month 'new', denoted by '0'; and pairs after their first month 'mature', denoted by '1'. 
Thus we can develop a new sequence:
- In the zeroeth month, we have a single, new pair, giving us simply '0'.
- In the first month, this rabbit matures, giving us '1'.
- In the second month, a new rabbit is born, giving us '10'
- In the third month, the mature pairs each produce a new pair, and the new pair from the previous month matures, giving us '101'
- In the forth month, the mature pairs each produce a new pair, and the new pair from the previous month matures, giving us '10110'
- And so on ...

You may see the naive way to generate this sequence: to generate any particular month's sequence, 
take that of the previous month and replace any '1' with a '10' and any'0' with a '1'.
There is, however, a more interesting way to do it: any month's sequence (after months 0 and 1) can be defined as the sequence from the month before concatenated with the sequence from two months before.

Write a program that will recursively generate the "rabbit sequence" from any given month, using the method just mentioned.

## Input

You are given a number that represents the month.
Example, given five (5) as the input, then the rabbit sequence in the fith month is '10110101'.

## Output

You need to output the rabbit sequence in 0s and 1s, see below.

## Sample Input
    5

## Sample Output
    10110101