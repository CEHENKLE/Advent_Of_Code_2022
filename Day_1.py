# leaving my lovely debugging print statements for posterity ;)

my_file = open("Day_1_AOC.txt", "r")
elves_file = my_file.readlines()
elves_list =[]
elf_total = 0
for elf in elves_file:
#    print('I am the elf')
#    print(elf)
    if elf not in ['\n', '\r', '\r\n']:
        elf_total += int(elf)
#        print('I am the elf total')
#        print(elf_total)
    else:
        elves_list.append(elf_total)
        elf_total = 0

# par
print('the biggest elf is....')
print(max(elves_list))

# part 2

sorted_list = sorted(elves_list, reverse=True)

#print(sorted_list)

sum = sorted_list[0]+sorted_list[1]+sorted_list[2]

print(sum)