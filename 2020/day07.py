### PART 1
# read the input
f = open('input/day07.txt', 'r')
input = [x.strip() for x in f]
f.close()
# parse the input into multiply mapped rulesets
ruleset = {}
for line in input:
    line = line.split(' contain ')
    # get the part of the rule that defines what is doing the containing
    line_container = ' '.join(line[0].split()[:2])
    if line[1].strip() != 'no other bags.':
        # if these bags must hold other bags...
        line_contents = line[1].split(', ')
        line_contents = [c.split()[:-1] for c in line_contents]
        ruleset[line_container] = dict(zip(
            [' '.join(c[1:]) for c in line_contents],
            [int(c[0]) for c in line_contents],
        ))
    else:
        # if these bags must not hold other bags...
        ruleset[line_container] = {}
# Calculate how many bag types can eventually contain at least one 'shiny gold' bag
can_hold = []
need_to_check = ['shiny gold']
need_to_check_next = []
while len(need_to_check) > 0:
    for checking_type in need_to_check:
        # see which bags can hold this type according to the ruleset
        holds_it = [t for t in ruleset
                    if ((checking_type in ruleset[t]) and (t not in can_hold))]
        # update what bag types we've got
        can_hold = list(set(can_hold + holds_it))
        need_to_check_next = list(set(need_to_check_next + holds_it))
    need_to_check = need_to_check_next
    need_to_check_next = []
print(len(can_hold))

### PART 2
# calculate how many individual bags have to be inside a single 'shiny gold' bag
big_fat_bag = {}
curr_level = ruleset['shiny gold']
while len(curr_level) > 0:
    next_level = {}
    for b in curr_level:
        # update the next step we need to take
        for nb in ruleset[b]:
            if nb not in next_level:
                next_level[nb] = 0
            next_level[nb] += curr_level[b]*ruleset[b][nb]
        # update the total bag
        if b not in big_fat_bag:
            big_fat_bag[b] = 0
        big_fat_bag[b] += curr_level[b]
    curr_level = next_level
print(sum([c for c in big_fat_bag.values()]))
