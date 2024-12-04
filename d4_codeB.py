input = open("d4_input.txt", 'r')

arr = []

# removes new line char
for line in input:
    arr.append(line[0:-1])

# Defines bounds of quasi 2D array
WIDTH_X = len(arr[0])
WIDTH_Y = len(arr)


def checkAround(x, y):
    for i in range(-1,2,2): # Increases by 2 in order to check the 4 corners around 'A'
        for j in range(-1,2,2):
            # Stops from searching outside arr
            if x+i >= 0 and x+i < WIDTH_X and y+j >= 0 and y+j < WIDTH_Y:
                if arr[x+i][y+j] == 'M':
                    # Ensures diagonal is not outside of range
                    if x-i >= 0 and x-i < WIDTH_X and y-j >= 0 and y-j < WIDTH_Y:
                        if checkDiagonal(x, y, i, j): # Checks if diagonal of 'M' is 'S'
                            # Checks for 'M' below other 'M'
                            if arr[x-i][y+j] == 'M':
                                if checkDiagonal(x, y, 0-i, j):
                                    # print("    YES AT",x,y)
                                    return 1
                            
                            # Checks for 'M' to the right of other 'M'
                            elif arr[x+i][y-j] == 'M':
                                if checkDiagonal(x, y, i, 0-j):
                                    # print("    YES AT",x,y)
                                    return 1
                            else:
                                # print("    No M beside")
                                return 0
                        else:
                            # print("    Diagonal not S")
                            return 0
                    else:
                        # print("    Failed Range")
                        # print("   ", x-i >= 0, x-i < WIDTH_X, y-j >= 0, y-j < WIDTH_Y)
                        return 0
    return False

# Checks is the diagonal of 'M' is an 'S'
def checkDiagonal(x, y, i, j):
    # x,y give postition of 'A'
    # i,j give offset of 'M'
    if arr[x-i][y-j] == 'S':
        return True
    else:
        return False


x=0
total_count = 0
while x < len(arr):
    y=0
    while y < len(arr[x]):
        if arr[x][y] == 'A':
            # print("A at",x,y)
            total_count += checkAround(x,y)

        y += 1
    x += 1

print(f"Part B:\n \"X-MAS\"s:",total_count)
