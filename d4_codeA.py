input = open("d4_input.txt", 'r')

arr = []

# removes new line char
for line in input:
    arr.append(line[0:-1])

WIDTH_X = len(arr[0])
WIDTH_Y = len(arr)


def checkAround(x, y):
    count = 0
    for i in range(-1,2): # 2 exclusive
        for j in range(-1,2):
            if x+i >= 0 and x+i < WIDTH_X and y+j >= 0 and y+j < WIDTH_Y:   # Stops from searching outside arr
                if arr[x+i][y+j] == 'M':
                    if checkNexts(x+i, y+j, i, j):
                        count += 1
    return count

# Sees if the next to letters after 'M' are 'A' and 'S' in the same direction 'M' was to 'X'
def checkNexts(x, y, i, j):
    if x+i >= 0 and x+i < WIDTH_X and y+j >= 0 and y+j < WIDTH_Y: # Stops from searching outside arr
        if arr[x+i][y+j] == 'A':
            # Doubles as to check the letter after 'A'
            if x+i*2 >= 0 and x+i*2 < WIDTH_X and y+j*2 >= 0 and y+j*2 < WIDTH_Y: 
                if arr[x+i*2][y+j*2] == 'S':
                    return True
    return False



x=0
total_count = 0
while x < len(arr):
    y=0
    while y < len(arr[x]):
        if arr[x][y] == 'X':
            total_count += checkAround(x,y)

        y += 1
    x += 1

print(f"Part A:\n \"XMAS\"s:",total_count)
