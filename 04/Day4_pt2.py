# 
# Advent of code 2022
# Day 4 pt 2
# 12/3/2022
#  

import re

with open('./input.txt') as f:
    content = f.readlines()

# Remove \n in each item
content = [x.strip() for x in content]

content = [x.split(',') for x in content]

def main(content):
    
    total_count = 0

    for pairs in content:

        first_pair_min = int(re.search('^\d+', pairs[0]).group(0))
        first_pair_max = int(re.search('\d+$', pairs[0]).group(0))

        second_pair_min = int(re.search('^\d+', pairs[1]).group(0))
        second_pair_max = int(re.search('\d+$', pairs[1]).group(0))

        if (second_pair_min <= first_pair_min and second_pair_max >= first_pair_min) or \
           (second_pair_min <= first_pair_max and second_pair_max >= first_pair_max) or \
           (first_pair_min <= second_pair_min and first_pair_max >= second_pair_min) or \
           (first_pair_min <= second_pair_max and first_pair_max >= second_pair_max):
           total_count += 1

    print(f'The total number is: {total_count}')

if __name__ == '__main__':
    main(content)