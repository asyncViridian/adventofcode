### PART 1
# read the input into a list
f = open('input/day01.txt', 'r')
input = [int(x) for x in f]
f.close()
# count how many times a depth measurement increases
count = 0
for i in range(len(input)-1):
    if input[i]<input[i+1]:
        count += 1
print(count)

### PART 2
# count how many times the sum of a 3-measurement window increases
count = 0
for i in range(len(input)-3):
    sum_prev = sum(input[i:i+3])
    sum_post = sum(input[i+1:i+4])
    if sum_post>sum_prev:
        count += 1
print(count)
