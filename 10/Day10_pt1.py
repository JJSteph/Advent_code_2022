# 
# Advent of code 2022
# Day 10 pt 1
# 12/16/2022
#  

import re

with open('./input.txt') as f:
    content = f.readlines()

# Remove \n in each item
content = [x.strip('\n') for x in content]

def main(content):
    
    cycles = 0
    x_register = 1

    times = [x for x in range(20, 260, 40)]

    signal_str = [None for x in range(len(times))]

    for value in content:

        if re.search('^noop', value) != None:
            cycles += 1
            if cycles in times:
                signal_str[times.index(cycles)] = cycles * x_register
                continue

        elif re.search('^addx', value) != None:
            for i in range(2):
                cycles += 1
                if cycles in times:
                    signal_str[times.index(cycles)] = cycles * x_register
                    continue

            to_add = int(re.search('\-?\d+', value).group(0))
            x_register += to_add

    print(f'Sum of sig str: {sum(signal_str)}')

if __name__ == '__main__':
    main(content)