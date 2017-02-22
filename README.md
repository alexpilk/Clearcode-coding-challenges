# Clearcode coding challenges 
Clearcode coding challenges 
(submission by Oleksii Pilkevych).

Please note that the results of Task 1 are different from the ones in the examples from the task description.

In the task description the following examples were specified:
* `battle([21,-3,20])` => "evens win" // 10101-11 vs 10100, 3-2 vs 3
* `battle([7,-3,-14,6])` => "evens win" // 111-11 vs -1110+110, 3-2 vs -1+1
* `battle([17,-3, 32, -24])` => "tie" // 10111-11 vs 100000-11000, 4-2 vs 5-3

Whereas the script returns:
* `battle([21,-3,20])` => "evens win" // 10101-11 vs 10100, 3-2 vs 3
* `battle([7,-3,-14,6])` => "odds win" // 111-11 vs -1110+110, 3-2 vs -1+1
* `battle([17,-3, 32, -24])` => "evens win" // 10001-11 vs 100000-11000, 2-2 vs 5-3

This is because there are errors in the examples.
In the example for the 2nd battle it says that "evens win" instead of "odds win".
And in the 3rd battle 17 is represented as 10111 in binary instead of 10001.

# Solutions explained
## Task 1:
Function `battle()` accepts a list of soldiers. Then for every soldier in the battlefield it:
* checks whether the soldier is even or odd (using % 2)
* converts soldier number to binary
* for each bit corresponding to the soldier's type it increments the score (or decrements it, the sign is computed by multiplying the value by `soldier / abs(soldier)`, which equals 1 if soldier is greater than 0 and if soldier is less than 0 it equals -1)

## Task 2:
Explanation for the recursive approach:
* the file with the terrain descriptions is opened and sliced into three-dimensional list terrains[]. terrains[] is a list of terrains which are lists of rows which are lists of cells (energies). Also, every value is converted from string to integer.
* variable min_energy is created and set to maximum energy that can be consumed in the first terrain on the list
* for each terrain function Walker() is started from point [0,0] with energy equal to point [0,0]
* first of all Walker() checks if current energy consumption exceeds minimum energy (this speeds up the program since you don't need to finish checking a path if you know it already exceeds minimum energy)
* then it checks if current position is the last cell in the row/column. If so - it checks all the remaining cells in the column/row respectively. If energy is smaller than min_energy it changes min_energy and returns.
* lastly, two Walker() functions are called from the adjacent cells on the right and at the bottom, which makes the function recursive
