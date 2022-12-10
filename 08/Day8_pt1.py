# 
# Advent of code 2022
# Day 7 pt 1
# 12/8/2022
#  

with open('./input.txt') as f:
    content = f.readlines()

# Remove \n in each item
content = [x.strip('\n') for x in content]

def main(content):

    # Make copy
    visible_trees = content.copy()
    
    for i, row in enumerate(content):
        for j, col in enumerate(content[i]):

            blocked_sides = 0

            # Check above
            row_check = i
            col_check = j
            while True:

                row_check -= 1

                if row_check < 0 or row_check >= len(content):
                    break

                if int(content[row_check][col_check]) >= int(content[i][j]):
                    blocked_sides += 1
                    break

            # Below
            row_check = i
            col_check = j
            while True:

                row_check += 1

                if row_check < 0 or row_check >= len(content):
                    break

                if int(content[row_check][col_check]) >= int(content[i][j]):
                    blocked_sides += 1
                    break

            # Left
            row_check = i
            col_check = j
            while True:

                col_check -= 1

                if col_check < 0 or col_check >= len(content[0]):
                    break

                if int(content[row_check][col_check]) >= int(content[i][j]):
                    blocked_sides += 1
                    break

            # Right
            row_check = i
            col_check = j
            while True:

                col_check += 1

                if col_check < 0 or col_check >= len(content[0]):
                    break

                if int(content[row_check][col_check]) >= int(content[i][j]):
                    blocked_sides += 1
                    break

            if blocked_sides == 4:
                visible_trees[i] = visible_trees[i][:j] + ' ' + visible_trees[i][j + 1:]

    # Count remaining visible trees
    num_visible_trees = 0

    for i, row in enumerate(visible_trees):
        for j, col in enumerate(visible_trees[i]):
            if visible_trees[i][j] != ' ':
                num_visible_trees += 1

    print(f'The number of visit trees is: {num_visible_trees}')

if __name__ == '__main__':
    main(content)