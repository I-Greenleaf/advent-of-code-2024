import re

input = open("d3_input.txt", "r")
input_string = input.read()

# Part A:

# Stores all mul(#,#) instuctions in a list
instructions = re.findall(r"mul\(\d+,\d+\)", input_string) 

# Converts an instruction into ['#', '#'] format
instructions = [inst[4:-1] for inst in instructions]
instructions = [inst.split(",") for inst in instructions]

# Multiplies instruction and adds all products together
sum = 0
for inst in instructions:
    sum += int(inst[0]) * int(inst[1])
        
print(f"Part A: \nSum: {sum}")


# Part B:

# Starts off multiplying instructions
do_mul = True

# Stores all "mul(#,#), "do()"s, and "don't()s" instructions in a list
instructions = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", input_string)


sum = 0
for inst in instructions:
    # Checks if instruction is a multiplier and if allowed to multiply
    if inst[0:3] == "mul" and do_mul:
        isnt = inst[4:-1].split(',')
        sum += int(isnt[0]) * int(isnt[1])

    elif inst == "do()":
        do_mul = True
        
    elif inst == "don't()":
        do_mul = False    
        
print(f"\nPart B: \nSum: {sum}")
