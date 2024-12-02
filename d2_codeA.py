input = open("d2_input.txt", "r")

good_reports = 0

for report in input:
    # Takes string of numbers and converts it to array of ints
    # Needed to compare values
    levels = [int(i) for i in report.split()]
    
    breakOut = False

    for i in range(len(levels)):
        # Can't do any comparisons to previous level for first level so needs to skip comparing for the first level
        if i != 0:
            # Checks if there is a jump greater than two or levels are the same
            difference = abs(levels[i] - levels[i-1])
            if difference == 0 or difference > 3:
                breakOut = True
                break

            # Gets intial direction
            elif i == 1:
                direction = levels[i] > levels[i-1]

            else:
                # Checks for if numbers go from increasing to decreasing and vice versa
                temp_direction = levels[i] > levels[i-1]

                if direction != temp_direction:
                    breakOut = True
                    break
            

    if not breakOut:
        good_reports += 1

print(f"Part A: \nSafe Reports: {good_reports}")
        