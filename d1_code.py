import pandas as pd

input = open("d1_input.txt", "r")
# File is seperated by three spaces, not commas
# engine parameter set to avoid warning
input = pd.read_csv(input, sep='   ', header=None, engine='python') 


# Part A solution:

left = input[0].sort_values()
right = input[1].sort_values()

# Finds the differnce between the lowest values in the two series, then the next lowest and so on through the whole series
# Sums these up to find the total difference
total_diff = 0
for i in range(len(left)): # left and right have same length
    # .iloc[i] gets the sorted index location
    # Where just [i] would get the number at that place in the series
    diff = abs(left.iloc[i] - right.iloc[i]) 
    total_diff += diff

print(f"Part A: \nDifference: {total_diff}")


# Part B Solution:

# Counts how many times a number appears in the right series
right_counts = right.value_counts()

sim_score = 0
for num in left:
    # try case used for when there is a value in left that doesn't exist in right
    try:
        sim_score += num * right_counts[num]
    except:
        pass

print(f"\nPart B: \nSimilarity Score: {sim_score}")
