# 
# Advent of code 2022
# Day 6 pt 2
# 12/6/2022
#  

with open('./input.txt') as f:
    content = f.readlines()

# Extract char from list
content = content[0]

def main(content):

    # list of chars
    marker = []

    for i, letter in enumerate(content):
        if len(marker) == 14:
            # Check if unique
            unique_marker = set(marker)
            if len(unique_marker) == len(marker):
                break

            else:
                marker.pop(0)
                marker.append(letter)
        else:
            marker.append(letter)

    print(f'Number of letters: {i}')

if __name__ == '__main__':
    main(content)