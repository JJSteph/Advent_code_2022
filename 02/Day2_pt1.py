# 
# Advent of code 2022
# Day 2 pt 1
# 12/2/2022
#  

with open('./input.txt') as f:
    content = f.readlines()

# Remove \n in each item
content = [x.strip() for x in content]

# Split by space

content = [x.split(' ') for x in content]

def main(content):

    total_score = 0

    for pair in content:

        if pair[1] == 'X':
            total_score += 1
        elif pair[1] == 'Y':
            total_score += 2
        elif pair[1] == 'Z':
            total_score += 3

        if (pair[0] == 'A' and pair[1] == 'Z') or \
           (pair[0] == 'C' and pair[1] == 'Y') or \
           (pair[0] == 'B' and pair[1] == 'X'): # Lost
            total_score += 0
        elif (pair[0] == 'A' and pair[1] == 'X') or \
             (pair[0] == 'B' and pair[1] == 'Y') or \
             (pair[0] == 'C' and pair[1] == 'Z'): # Tie
            total_score += 3
        elif (pair[0] == 'C' and pair[1] == 'X') or \
             (pair[0] == 'A' and pair[1] == 'Y') or \
             (pair[0] == 'B' and pair[1] == 'Z'): # Won
            total_score += 6


    print(f'The total score is: {total_score}')

if __name__ == '__main__':
    main(content)