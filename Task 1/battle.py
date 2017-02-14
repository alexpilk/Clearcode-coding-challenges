def battle(battlefield):
    print("_________________________________")
    print("Battle {0} begins!".format(battlefield))
    score = [0,0]
    for soldier in battlefield:
        soldier_type = soldier % 2 # 0 means even, 1 means odd
        if soldier_type == 1: print('Odd {0:b}'.format(soldier)) 
        else: print('Even {0:b}'.format(soldier))
        for bit in '{0:b}'.format(soldier):
            if bit == str(soldier_type):
                score[soldier_type] += 1 * soldier / abs(soldier) 
    
    print("Evens: {0[0]}, Odds: {0[1]}".format(score))
    if score[1] > score[0]: 
        return "Odds win" 
    elif score[0] > score[1]:
        return "Evens win"
    else:
        return "Tie"

print(battle([21,-3,20]))
print(battle([7,-3,-14,6]))
print(battle([17,-3, 32, -24]))

# Example of a tie
print(battle([23,-3, 32, -24]))

# Please note that the results of this script are different from the ones in 
# the examples in the task description.

# In the description the following examples were specified:
# battle([21,-3,20]) => "evens win" // 10101-11 vs 10100, 3-2 vs 3
# battle([7,-3,-14,6]) => "evens win" // 111-11 vs -1110+110, 3-2 vs -1+1
# battle([17,-3, 32, -24]) => "tie" // 10111-11 vs 100000-11000, 4-2 vs 5-3

# Whereas the script returns:
# battle([21,-3,20]) => "evens win" // 10101-11 vs 10100, 3-2 vs 3
# battle([7,-3,-14,6]) => "odds win" // 111-11 vs -1110+110, 3-2 vs -1+1
# battle([17,-3, 32, -24]) => "evens win" // 10001-11 vs 100000-11000, 2-2 vs 5-3

# This is because there are errors in the examples.
# In the example for the 2nd battle it says that "evens win" instead of "odds win"
# And in the 3rd battle 17 is represented as 10111 in binary instead of 10001
