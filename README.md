# Clearcode coding challenges 
Clearcode coding challenges 
(submission by Oleksii Pilkevych)

Please note that the results of Task 1 are different from the ones in the examples from the task description.

In the task description the following examples were specified:
battle([21,-3,20]) => "evens win" // 10101-11 vs 10100, 3-2 vs 3
battle([7,-3,-14,6]) => "evens win" // 111-11 vs -1110+110, 3-2 vs -1+1
battle([17,-3, 32, -24]) => "tie" // 10111-11 vs 100000-11000, 4-2 vs 5-3

Whereas the script returns:
battle([21,-3,20]) => "evens win" // 10101-11 vs 10100, 3-2 vs 3
battle([7,-3,-14,6]) => "odds win" // 111-11 vs -1110+110, 3-2 vs -1+1
battle([17,-3, 32, -24]) => "evens win" // 10001-11 vs 100000-11000, 2-2 vs 5-3

This is because there are errors in the examples.
In the example for the 2nd battle it says that "evens win" instead of "odds win"
And in the 3rd battle 17 is represented as 10111 in binary instead of 10001
