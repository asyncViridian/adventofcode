### PART 1
# read the input
f = open('input/day10.txt', 'r')
input = [int(x.strip()) for x in f]
f.close()
# calculate the sequence of adapters we need
# we need to use ALL the adapters and match wall joltage of 0 to builtin
# conveniently ... this chain literally is just the adapters sorted
adapters = sorted(input)
# add the wall adapter and the built-in adapter
adapters = [0] + adapters + [max(adapters) + 3]
# calculate the distribution of joltage gaps
gaps = {1:0, 2:0, 3:0}
for i in range(len(adapters)-1):
    gaps[adapters[i+1]-adapters[i]] += 1
print(gaps, gaps[1]*gaps[3])

### PART 2
# calculate the number of ways we can connect the adapters
# we can do this by keeping track of how many ways we get to each adapter
# (yay dynamic programming!)
ways_count = [1] # initialize knowing there's only one wall :)
for i in range(1, len(adapters)):
    ways_sum = 0
    # assume there's no duplicate adapters
    # so the earliest index we should check is just i-3
    i_compat = max(0, i-3)
    for j in range(i_compat, i):
        # sum up how many ways we can get to this adapter from previous compatible adapters
        if (adapters[i]-adapters[j]) <= 3:
            ways_sum += ways_count[j]
    ways_count.append(ways_sum)
print(ways_count[-1])
