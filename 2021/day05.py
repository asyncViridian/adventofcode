### PART 1
# read the input into a list
f = open('input/day05.txt', 'r')
fi = [x[:-1] for x in f]
f.close()
# parse input into point pair list
lines = [l.split(' -> ') for l in fi]
lines = [
        [[int(i) for i in p.split(',')] for p in l] 
        for l in lines
]
# build collection of intersection counts
intersects = {}
def addCoverage(intersects, point):
    if point not in intersects:
        intersects[point] = 0
    intersects[point] += 1
for l in lines:
    if l[0][0]==l[1][0]:
        a = min(l[0][1], l[1][1])
        b = max(l[0][1], l[1][1])
        for i in range(a, b+1):
            addCoverage(intersects, (l[0][0], i))
    elif l[0][1]==l[1][1]:
        a = min(l[0][0], l[1][0])
        b = max(l[0][0], l[1][0])
        for i in range(a, b+1):
            addCoverage(intersects, (i, l[0][1]))
# count number of 2-or-larger intersects
print(len([e for e in intersects if intersects[e]>=2]))

### PART 2
# TODO
