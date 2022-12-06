# 
# Advent of code 2022
# Day 5 pt 1
# 12/5/2022
#  

import re

with open('./input.txt') as f:
    content = f.readlines()

def main(content):
    
    # Find how many stacks

    for i, row in enumerate(content):

        if re.search('(\d+\s+)+\d{1}', row) != None:
            numbers = re.search('(\d+\s+)+\d{1}', row).group(0)
            max_rows = i
            break

    numbers.split()
    num_columns = int(max(numbers))


    # Assign initial state of stacks

    stack = [[] for x in range(num_columns)]

    for i, row in enumerate(content):
        
        crate = ''

        if i == max_rows:
            break
        
        for j, letter in enumerate(row):
            if letter == ' ' or letter == '\n':
                if crate != '':
                    # Determine stack number
                    stack_col = j // 4 

                    # Expanding list if needed
                    if (max_rows - i - 1) >= len(stack[stack_col]):
                        stack[stack_col] = ['' for _ in range(max_rows - i)]

                    # Assign crate to stack
                    stack[stack_col][max_rows - i - 1] = crate
                    
                    crate = ''

            else:
                crate += letter


    # Parse instructions
    # And move crates
    for i, row in enumerate(content):

        if re.search('^move', row) != None:

            move_num = int(re.search('(?<=move )\\d+(?= from)', row).group(0))
            move_from = int(re.search('(?<=from )\\d+(?= to)', row).group(0)) - 1
            move_to = int(re.search('(?<=to )\\d+', row).group(0)) - 1

            for _ in range(move_num):

                moving = stack[move_from].pop()
                stack[move_to].append(moving)

    # Printing top of stack
    top_stack = ''
    for col in stack:
        top_stack += col[-1]

    # Remove brackets
    top_stack = re.sub("(\[|\])","", top_stack)

    print(top_stack)



if __name__ == '__main__':
    main(content)