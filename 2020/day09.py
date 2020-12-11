### PART 1
# read the input
f = open('input/day09.txt', 'r')
input = [int(x.strip()) for x in f]
f.close()
# hyperparameters
preamble_len = 25
# calculate whether a list of numbers can sum to value
def canSum(numbers, value):
    # brute force calculate sums of all pairs
    sums = [[(n1 + n2) for n2 in numbers] for n1 in numbers]
    sums = list(set([e for sublist in sums for e in sublist]))
    # next, for each elem (b) in one half, check if its complement (value-n) is in the other half
    return any([(e==value) for e in sums])
# find the first number in the list that's NOT the sum of two prev (preamble_len) numbers
for i in range(preamble_len, len(input)):
    if not canSum(input[i-preamble_len:i], input[i]):
        invalid_num = input[i]
        break
print(invalid_num)

### PART 2
# Find a contiguous set of at least two numbers which sum to the invalid number we found before
bounds = [0, 2] # lower incl, upper excl
while (sum(input[bounds[0]:bounds[1]]) != invalid_num) or (bounds[1]-bounds[0] < 2):
    if sum(input[bounds[0]:bounds[1]]) < invalid_num:
        # if it's too low, add a number
        bounds[1] += 1
    elif sum(input[bounds[0]:bounds[1]]) > invalid_num:
        # if it's too high, take out a number
        bounds[0] += 1
    else:
        # if the bounds are too short (contains only one number?), add a number
        bounds[1] += 1
# then, to find the encryption weakness, add the smallest and largest number within the bounds
bounds_set = input[bounds[0]:bounds[1]]
print(min(bounds_set) + max(bounds_set))
