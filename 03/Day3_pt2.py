# 
# Advent of code 2022
# Day 3 pt 2
# 12/3/2022
#  

with open('./input.txt') as f:
    content = f.readlines()

# Remove \n in each item
content = [x.strip() for x in content]

def main(content):

    total_sum = 0

    total_items = []

    for i, items in enumerate(content, 1):

        total_items.append(items)

        # Calculate every three lines
        if i % 3 == 0:
            matching_item = match(total_items, 3)
            total_sum += priority(matching_item)
            total_items = []
                

    print(f'The total sum is: {total_sum}')

# Converts chars into priority
def priority(letter):

    if ord(letter) >= 97 and ord(letter) <= 122:
        result = ord(letter) - 96
    elif ord(letter) >= 65 and ord(letter) <= 90:
        result = ord(letter) - 38

    return(result)

# Finds char that occurs n number of times (counting once per string)
def match(list_string, num):

    letters = []
    count = []

    for string in list_string:

        # Get unique letters in each string
        string = set(string)

        for letter in string:

            # Only adding once per string
            if letter not in letters:
                letters.append(letter)
                count.append(1)
            else:
                count[letters.index(letter)] += 1

    return(letters[count.index(num)])

if __name__ == '__main__':
    main(content)