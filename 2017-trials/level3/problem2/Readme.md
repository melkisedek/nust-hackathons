# Maze Escape

## Problem Description

Write a program that inputs a maze in the format demostrated in the sample run 
below, where a `0` indecates a passageway and a `1` indicates a wall. The 
program must determine whether a path exists from a given point to another 
given point, where the points are indicated by a column index and a row index, 
these indices starting from 0 at the top left corner.


## Input

You are given the height and width of the maze followed by the structure of 
the maze as described above. You are also given the starting and ending point, 
the program should terminate when `-1-1` is entered as the start or end point. 

Example, Consider the maze below:

    +--+--+--+--+--+
    |           |  |
    +--+--+  +--+--+
    |  |  |a |  |c |
    +  +--+--+--+  |
    |     |  |  |  |
    +--+  +--+--+  +
    |  |b |  |     |
    +--+--+--+--+--+

A path exists from point `a` to point `b`, by going `North`, `West`, `West`, 
`South`, `South`, `East`, and `South`. You cannot, however find a path from 
point `a` to point `c`.

## Output

You need to output the path to be followed in escaping the maze if it exists 
otherwise indicate that the maze cannot be escaped.

## Sample Input

    Enter the width: 5
    Enter the height: 4
    Row 0: 0 0 0 0 1
    Row 1: 0 1 0 1 0
    Row 2: 0 0 1 1 0
    Row 3: 1 0 1 0 0
    Start at: 2 1
    Exit at: 1 3

    Start at: 2 1
    Exit at: 4 1

    Start at: -1-1

## Sample Output

    You can escape the maze with the following moves:
    N W W S S E S

    You cannot escape the maze.

    Goodbye!!!

## Clarification
A maze construction description is entered first as a series of `1` and `0` digits. 
The program then takes in different start and end point descriptions. The program 
determines whether solutions exist for the start and end points entered.

