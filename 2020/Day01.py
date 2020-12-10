### PART 1
# read the input into a list
f = open('input/Day01.txt', 'rb')
input = [int(x) for x in f]
f.close()
print('input: ', input)
# generate every index of pair of numbers
pairs = [zip([i]*len(input[i+1:]), list(range(i+1, len(input)))) for i in range(len(input))]
pairs = [e for sublist in pairs for e in sublist]
# find the one(s) that sum to 2020
fpairs = [e for e in pairs if (input[e[0]] + input[e[1]] == 2020)]
print(fpairs)
# get the first result's product
print(input[fpairs[0][0]] * input[fpairs[0][1]])

### PART 2
# generate every index of every triplet of numbers!
# we can just add to the pairs ...
triplets = [zip([p[0]]*len(input[p[1]+1:]), [p[1]]*len(input[p[1]+1:]), list(range(p[1]+1, len(input)))) for p in pairs]
triplets = [e for sublist in triplets for e in sublist]
# find the one(s) that sum to 2020
ftriplets = [e for e in triplets if (input[e[0]] + input[e[1]] + input[e[2]] == 2020)]
print(ftriplets)
# get the first result's product
print(input[ftriplets[0][0]] * input[ftriplets[0][1]]* input[ftriplets[0][2]])
