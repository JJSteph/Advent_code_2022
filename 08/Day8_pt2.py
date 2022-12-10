# 
# Advent of code 2022
# Day 7 pt 2
# 12/8/2022
#  

with open('./input.txt') as f:
    content = f.readlines()

# Remove \n in each item
content = [x.strip('\n') for x in content]

def main(content):

    highest_visible_score = 0
    
    for i, row in enumerate(content):
        for j, col in enumerate(content[i]):

            visible_score = []

            # Check above
            row_check = i
            col_check = j
            num_trees = 0
            while True:

                row_check -= 1

                if row_check < 0 or row_check >= len(content):
                    visible_score.append(num_trees)
                    break

                elif int(content[row_check][col_check]) < int(content[i][j]):
                    num_trees += 1

                elif int(content[row_check][col_check]) >= int(content[i][j]):
                    num_trees += 1
                    visible_score.append(num_trees)
                    break


            # Below
            row_check = i
            col_check = j
            num_trees = 0
            while True:

                row_check += 1

                if row_check < 0 or row_check >= len(content):
                    visible_score.append(num_trees)
                    break

                elif int(content[row_check][col_check]) < int(content[i][j]):
                    num_trees += 1

                elif int(content[row_check][col_check]) >= int(content[i][j]):
                    num_trees += 1
                    visible_score.append(num_trees)
                    break

            # Left
            row_check = i
            col_check = j
            num_trees = 0
            while True:

                col_check -= 1

                if col_check < 0 or col_check >= len(content[0]):
                    visible_score.append(num_trees)
                    break

                elif int(content[row_check][col_check]) < int(content[i][j]):
                    num_trees += 1

                elif int(content[row_check][col_check]) >= int(content[i][j]):
                    num_trees += 1
                    visible_score.append(num_trees)
                    break

            # Right
            row_check = i
            col_check = j
            num_trees = 0
            while True:

                col_check += 1

                if col_check < 0 or col_check >= len(content[0]):
                    visible_score.append(num_trees)
                    break

                elif int(content[row_check][col_check]) < int(content[i][j]):
                    num_trees += 1

                elif int(content[row_check][col_check]) >= int(content[i][j]):
                    num_trees += 1
                    visible_score.append(num_trees)
                    break
        
            visible_score_prod = 1
            for val in visible_score:
                visible_score_prod *= val

            if visible_score_prod > highest_visible_score:
                highest_visible_score = visible_score_prod

    print(f'The highest score is: {highest_visible_score}')

if __name__ == '__main__':
    main(content)