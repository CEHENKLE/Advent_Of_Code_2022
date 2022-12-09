def winnerwinner(him, you):
    if (him == 'A'):
        if you == 'X':
            return 4 # Rock (1) plus Draw (3)
        if you == 'Y':
            return 8 # Paper (2) plus Win (6)
        else:
            return 3 # Scissor (3) plus lose (0)
    if (him == 'B'):
        if you =='X':
            return 1 # Rock (1) plus lose (0)
        if you == 'Y':
            return 5 # Paper (2) plus Draw (3))
        else:
            return 9 # Scissors (3) plus win (6)
    if (him == 'C'):
        if you == 'X':
            return 7 # Rock (1) plus win (6)
        if you == 'Y':
            return 2 # Paper (2) plus lose (0)
        else:
            return 6 # Scissors (3) plus draw (3)

#testing
#print(winnerwinner('A','Y'))
#print(winnerwinner('B','X'))
#print(winnerwinner('C','Z'))

total = 0
with open('Day_2_AOC.txt') as file:
    for lines in file:
        him, me = [(x) for x in lines.split()]
        print(him,me)
        total+=(winnerwinner(him, me))
        print(total)
print(total)