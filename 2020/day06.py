### PART 1
# read the input
f = open('input/day06.txt', 'r')
input = [x.strip() for x in f]
f.close()
# parse these into groups and answers
responses = ' '.join([(x if (x != '') else '\t') for x in input]).split('\t')
responses = [x.strip().split() for x in responses]
# get the number of questions anyone answered yes for each group
groupanycounts = [len(set(''.join(e))) for e in responses]
print(sum(groupanycounts))

### PART 2
# get the number of questions everyone answered yes for each group
groupallcounts = [set(''.join(e)) for e in responses]
groupallcounts = [
    list(zip([all([(q in indiv) for indiv in r[1]]) for q in r[0]], r[0]))
    for r in zip(groupallcounts, responses)
]
groupallcounts = [len(set([q[1] for q in r if q[0]])) for r in groupallcounts]
print(sum(groupallcounts))
