
#Part 1
total = 0
total2 = 0
with open('Day_4_AOC.txt') as file:
    for lines in file:
        elf1, elf2 = [(x) for x in lines.split(',')]

        start1, stop1 = map(int,elf1.split('-'))
        start2, stop2 = map(int,elf2.split('-'))
        elf1_list = list(range(start1, (stop1)+1))
        elf2_list = list(range(start2, (stop2)+1))

        if all([item in elf2_list for item in elf1_list]) or all([item in elf1_list for item in elf2_list]):
#            To be read in a Lana voice....
#            print('YUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUP')
            total+=1

#Part 2
        if any([item in elf2_list for item in elf1_list]) or any([item in elf1_list for item in elf2_list]):
#            To be read in a Lana voice....
#            print('YUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUP')
            total2+=1

print(total)
print(total2)


# I could not get this to work...I really wanted to do it in one hop
#        elf1_list = [*range(elf1.split('-'))]
#        elf2_list = [*range(elf2.split('-'))]

# today I learned that range is exclusive >.<
# also, the first time I ran it, I only check if 1 was in 2, not if 2 was in 1.
