# 
# Advent of code 2022
# Day 10 pt 2
# 12/17/2022
#  

import re

with open('./input.txt') as f:
    content = f.readlines()

# Remove \n in each item
content = [x.strip('\n') for x in content]

# Create crt
crt = [['.' for y in range(40)] for x in range(6)]

def main(content):
    
    cycles = 0
    x_register = 1
    sprite = update_sprite(1)

    for value in content:

        cycles_to_advance = None

        if re.search('^noop', value) != None:
            cycles_to_advance = 1
        elif re.search('^addx', value) != None:
            cycles_to_advance = 2
            to_add = int(re.search('\-?\d+', value).group(0))
            x_register += to_add

        # Advancing cycles
        for _ in range(cycles_to_advance):

            col = cycles % len(crt[0])
            row = cycles // len(crt[0])

            if sprite[col] == '#':
                crt[row][col] = '#'

            cycles += 1

        # Update sprite
        sprite = update_sprite(x_register)

    # Printing final CRT
    for i in range(len(crt)):
        print(crt[i])

def update_sprite(middle):

    sprite = ['.' for x in range(40)]

    for i in [middle - 1, middle, middle + 1]:

        if (i + 1) > len(sprite) or i < 0:
            continue
        else:
            sprite[i] = '#'

    return(sprite)

if __name__ == '__main__':
    main(content)