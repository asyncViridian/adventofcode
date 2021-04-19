### PART 1
# read the input
f = open('input/day23.txt', 'r')
input = [x.strip() for x in f]
f.close()
# parse the input into cups
cups = [int(e) for e in input[0]]
# find the lowest and highest labels
cups_lowest = min(cups)
cups_highest = max(cups)
# now perform our moves!
def move(cups, current_i):
    # rotate current to be the beginning of the list
    cups = cups[current_i:]+cups[:current_i]
    current_i = 0
    selected = cups[current_i+1:current_i+4]
    cups = cups[:current_i+1]+cups[current_i+4:]
    dest_label = cups[current_i]-1
    while ((dest_label < cups_lowest) or (dest_label in selected)):
        if dest_label < cups_lowest:
            dest_label = cups_highest
        else:
            dest_label -= 1
    dest_i = cups.index(dest_label)
    return cups[:dest_i+1]+selected+cups[dest_i+1:]
for i in range(100):
    cups = move(cups, 0 if i==0 else 1)
# move 1 to the beginning
one_i = cups.index(1)
cups = cups[one_i:]+cups[:one_i]
# print out the contents after the 1
print(''.join([str(e) for e in cups[1:]]))

### PART 2
