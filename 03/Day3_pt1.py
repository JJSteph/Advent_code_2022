# 
# Advent of code 2022
# Day 3 pt 1
# 12/3/2022
#  

with open('./input.txt') as f:
    content = f.readlines()

# Remove \n in each item
content = [x.strip() for x in content]


def main(content):

    total_sum = 0

    for items in content:

        if len(items) % 2 != 0:
            SystemError("Item not of even length")

        half = int((len(items) / 2))

        first_half = items[:half]
        second_half = items[half:]
        
        matching_item = match(first_half, second_half)

        total_sum += priority(matching_item)

    print(f'The total sum is: {total_sum}')

# Converts chars into priority
def priority(letter):

    if ord(letter) >= 97 and ord(letter) <= 122:
        result = ord(letter) - 96
    elif ord(letter) >= 65 and ord(letter) <= 90:
        result = ord(letter) - 38

    return(result)

# Finds match in both
def match(first, second):

    for first_letter in first:
        for second_letter in second:
            if first_letter == second_letter:
                return(first_letter)

if __name__ == '__main__':
    main(content)