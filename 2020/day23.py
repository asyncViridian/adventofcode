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
def move_part1(cups, current_i):
    # rotate current to be the beginning of the list
    cups = cups[current_i:]+cups[:current_i]
    current_i = 0
    # take out the selected cups
    selected = cups[current_i+1:current_i+4]
    cups = cups[:current_i+1]+cups[current_i+4:]
    # figure out where the selected cups will be inserted
    dest_label = cups[current_i]-1
    while ((dest_label < cups_lowest) or (dest_label in selected)):
        if dest_label < cups_lowest:
            dest_label = cups_highest
        else:
            dest_label -= 1
    dest_i = cups.index(dest_label)
    # insert the selected cups
    return cups[:dest_i+1]+selected+cups[dest_i+1:]
for i in range(100):
    cups = move_part1(cups, 0 if i==0 else 1)
# move 1 to the beginning
one_i = cups.index(1)
cups = cups[one_i:]+cups[:one_i]
# print out the contents after the 1
print(''.join([str(e) for e in cups[1:]]))

### PART 2
# lol my super simple soln for part 1 isn't going to run fast now!
cups = [int(e) for e in input[0]]
# add in the extra million cups
cups_highest = max(cups)
cups = cups + [e+cups_highest+1 for e in range(1000000-len(cups))]
# re-parse the input into a cups index dict, mapping from cup to what comes after it
# (this is basically a linked list)
cups = dict([(cups[i], cups[i+1]) for i in range(len(cups)-1)]+[(cups[-1], cups[0])])
current = int(input[0][0])
# find the lowest and highest labels
cups_lowest = min(cups)
cups_highest = max(cups)
# now perform our moves!
def move_part2(cups, current):
    # identify the selected cups
    selected_1 = cups[current]
    selected_2 = cups[selected_1]
    selected_3 = cups[selected_2]
    selected_values = [selected_1, selected_2, selected_3]
    # figure out where the selected cups will be inserted after
    dest = current - 1
    while ((dest < cups_lowest) or (dest in selected_values)):
        if dest < cups_lowest:
            dest = cups_highest
        else:
            dest -= 1
    dest_after = cups[dest]
    # take out the selected cups
    cups[current] = cups[selected_3]
    # reinsert the selected cups
    cups[dest] = selected_1
    cups[selected_3] = dest_after
    return cups[current]
for i in range(10000000):
    current = move_part2(cups, current)
# figure out which two cups are immediately clockwise
clockwise_1 = cups[1]
clockwise_2 = cups[clockwise_1]
print(clockwise_1*clockwise_2)
