def winnerwinner(him, you):
    print('winner')
    print(him, you)
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

def blacksocks(him,outcome):
    print('blacksocks')
    print(him,outcome)
    if outcome == 'X': #lose
        if him == 'A':
            return winnerwinner(him, 'Z')
        if him == 'B':
            return winnerwinner(him, 'X')
        else:
            return winnerwinner(him, 'Y')
    if outcome == 'Y': # Draw
        if him == 'A':
            return winnerwinner(him, 'X')
        if him == 'B':
            return winnerwinner(him, 'Y')
        else:
            return winnerwinner(him,'Z')
    else: #win
        if him == "A":
            return winnerwinner(him,'Y')
        if him == "B":
            return winnerwinner(him,'Z')
        else:
            return winnerwinner(him, 'X')

#testing
#print(winnerwinner('A','Y'))
#print(winnerwinner('B','X'))
#print(winnerwinner('C','Z'))


# part 1
total = 0
with open('Day_2_AOC.txt') as file:
    for lines in file:
        him, me = [(x) for x in lines.split()]
#        print(him,me)
        total+=(winnerwinner(him, me))
#        print(total)
print(total)

#testing
#print(blacksocks('A','Y'))
#print(blacksocks('B','X'))
#print(blacksocks('C','Z'))
#print('--------------------------------------------------------')

#Part 2
total=0
with open('Day_2_AOC.txt') as file:
    for lines in file:
        him, outcome = [(x) for x in lines.split()]
        total += (blacksocks(him, outcome))
print(total)