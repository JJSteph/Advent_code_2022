# 
# Advent of code 2022
# Day 1 pt 1
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

    max_cals = 0

    current_cals = 0

    for i, val in enumerate(content):

        if val == None or (i + 1) == len(content):
            if current_cals > max_cals:
                max_cals = current_cals
            current_cals = 0
            continue

        else:
            current_cals += val

    print(f'The most cals is: {max_cals}')

if __name__ == '__main__':
    main(content)