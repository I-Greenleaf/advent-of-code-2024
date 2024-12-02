input = open("d2_input.txt", "r")

good_reports = 0

def check_report(levels, remove_index=None, bads=0):
    breakOut = False

    if bads > 1:
        breakOut = True

    else:
        if remove_index is not None:
            levels.pop(remove_index)

        i = 1
        while i < len(levels):
            difference = abs(levels[i] - levels[i-1])

            if difference == 0 or difference > 3:
                bads += 1
                if check_report(levels.copy(), i-1, bads): # .copy() used so pointer doesn't get passed
                    levels.pop(i-1)
                elif check_report(levels.copy(), i, bads):                    
                    levels.pop(i)
                else:
                    breakOut = True
                    break
                if i == 2: # Double checks the direction in case the first or second level was removed
                    direction = levels[i-1] > levels[i-2]
                i -= 1
            

            # Gets intial direction
            elif i == 1:
                direction = levels[i] > levels[i-1]

            else:
                # Checks for if numbers go from increasing to decreasing and vice versa
                temp_direction = levels[i] > levels[i-1]

                if direction != temp_direction:
                    bads += 1
                    # Double checks direction in case direction has changed due to early element getting removed
                    if i == 2 and check_report(levels.copy(), i-2, bads): 
                        direction = levels[i] > levels[i-1]
                        levels.pop(i-2)
                    elif check_report(levels.copy(), i-1, bads):
                        levels.pop(i-1)
                    elif check_report(levels.copy(), i, bads):                        
                        levels.pop(i)

                    else:
                        breakOut = True
                        break
                    i -= 1

            i += 1

    return not breakOut # True means it is good



for report in input:
    L = [int(i) for i in report.split()]
    bads = 0
    if check_report(L):
        good_reports += 1

print(f"Part B: \nSafe Reports: {good_reports}")
