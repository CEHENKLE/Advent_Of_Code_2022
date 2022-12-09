import string
from itertools import zip_longest

# Part 1
values = dict(zip(string.ascii_letters, range(1,53)))
print(values)
total = 0
difftotal=0
with open('Day_3_AOC.txt') as file:
    for line in file:
        n = len(line)
        sack1 = slice(0,n//2)
        sack2 = slice(n//2,n)
#        print(line[sack1])
#        print(line[sack2])
        for char in line[sack1]:
            if char in line[sack2]:
                total += values[char]
                break
print(total)

# Part 2
def grouper(iterable_obj, count, fillvalue=None):
    args = [iter(iterable_obj)] * count
    return zip_longest(*args, fillvalue=fillvalue)

my_file = open("Day_3_AOC.txt", "r")
data = my_file.read()
data_into_list = data.split("\n")

grouped_list = list(grouper(data_into_list, 3, ""))

#print(grouped_list)
total_part_2 = 0
for listed in grouped_list:
    print(values[(set(listed[0]) & set(listed[1]) & set(listed[2])).pop()])
    total_part_2 += values[(set(listed[0]) & set(listed[1]) & set(listed[2])).pop()]
print(total_part_2)

# Random Thought
#        difftotal = values[(set(line[sack1]) & set(line[sack2])).pop()]

