import operator

### PART 1
# read the input
f = open('input/day03.txt', 'r')
input = [x.strip() for x in f]
f.close()
def countTrees(slope_right, slope_down):
    # iterate through the trees
    position = 0
    tree_count = 0
    while (position*slope_down) < len(input):
        if input[position*slope_down][operator.mod(position*slope_right, len(input[position*slope_down]))] == '#':
            tree_count = tree_count + 1
        position = position + 1
    return tree_count
# check how many trees if we descend at (-3, -1)
print(countTrees(3, 1))

### PART 2
# get the product of descent at (-1, -1), (-3, -1), (-5, -1), (-7, -1), (-1, -2)
print(countTrees(1, 1)*countTrees(3, 1)*countTrees(5, 1)*countTrees(7, 1)*countTrees(1, 2))
