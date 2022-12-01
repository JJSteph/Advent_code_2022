# 
# Advent of code 2022
# Day 1 pt 2
# 12/1/2022
#  

with open('./input.txt') as f:
    content = f.readlines()

# Remove \n in each item
content = [x.strip() for x in content]

# Convert to number
for i, val in enumerate(content):
    try:
        content[i] = int(val)
    except:
        content[i] = None

def main(content):

    top_three_cals = [0,0,0]

    current_cals = 0

    for i, val in enumerate(content):

        if val == None or (i + 1) == len(content):
            if current_cals > min(top_three_cals):
                to_remove = top_three_cals.index(min(top_three_cals))
                top_three_cals.pop(to_remove)
                top_three_cals.append(current_cals)
            
            current_cals = 0
            continue

        else:
            current_cals += val

    print(f'The sum of the top three cals is: {sum(top_three_cals)}')

if __name__ == '__main__':
    main(content)