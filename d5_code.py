input = open("d5_input.txt", 'r')
lines = input.readlines()

# Value for key is a list of page numbers that come after the key page number 
pageDict = {}

# Puts all the instructions in the dictionary
i = 0
while lines[i] != '\n':
    numOne = lines[i][0:2]
    numTwo = lines[i][3:5]
    if numOne not in pageDict:
        pageDict[numOne] = []
    if numTwo not in pageDict[numOne]:
        pageDict[numOne].append(numTwo)

    i += 1

i += 1 # Go to the next line, where the updates are



sum = 0
while i < len(lines): # Goes through all updates
    badLine = False
    
    # Grabs all number in a update(line) and stores it in a list
    j = 0
    numbers = []
    while j < len(lines[i][0:-1]): # Grabs each number in update
        numbers.append(lines[i][j:j+2])     # selected number
        j += 3
    
    # Reverse the numbers so that we can take the last(now first)
    #   number and see if any of the previous numbers are in its value array
    #   If a number later in the new list is in the value array,
    #   that means that there was an instruction for a later(ealier) number to be before an earlier(later) number
    # This means that it is a bad update and we do not conisder the update for our final calculated value
    numbers.reverse()

    for j in range(len(numbers)):
        k = j + 1
        while k < len(numbers):
            try:
                if pageDict[numbers[j]] and numbers[k] in pageDict[numbers[j]]:
                    badLine = True
                    break
            except:
                pass
            
            k += 1
        if badLine:
            break
    
    # The final calculated number is the sum of the middle number in all of the good updates
    if not badLine:
        sum += int(numbers[len(numbers)//2])
    
    i += 1

print(f"Part A:\n Sum:", sum)


# Part B:


