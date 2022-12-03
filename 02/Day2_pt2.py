# 
# Advent of code 2022
# Day 2 pt 2
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

        # Descision of whether to win/tie/lose
        if pair[1] == 'X': # Lose
            total_score += 0
            if pair[0] == 'A':
                pair[1] = 'Z'
            elif pair[0] == 'C':
                pair[1] = 'Y'
            elif pair[0] == 'B':
                pair[1] = 'X'

        elif pair[1] == 'Y': # Tie
            total_score += 3
            if pair[0] == 'A':
                pair[1] = 'X'
            elif pair[0] == 'B':
                pair[1] = 'Y'
            elif pair[0] == 'C':
                pair[1] = 'Z'

        elif pair[1] == 'Z': # Win
            total_score += 6
            if pair[0] == 'C':
                pair[1] = 'X'
            elif pair[0] == 'A':
                pair[1] = 'Y'
            elif pair[0] == 'B':
                pair[1] = 'Z'

        if pair[1] == 'X':
            total_score += 1
        elif pair[1] == 'Y':
            total_score += 2
        elif pair[1] == 'Z':
            total_score += 3

    print(f'The total score is: {total_score}')

if __name__ == '__main__':
    main(content)