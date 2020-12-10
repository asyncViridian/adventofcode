### PART 1
# read the input
f = open('input/day02.txt', 'r')
input = [x for x in f]
f.close()
# function to calculate if a password entry line is valid according tp P1 rules
def isValid1(pw):
    pw = pw.split()
    pw[0] = [int(i) for i in pw[0].split('-')]
    pw[1] = '' + pw[1][0]
    count = sum([(1 if c==pw[1] else 0) for c in pw[2]])
    return ((count >= pw[0][0]) and (count <= pw[0][1]))
print(sum([(1 if isValid1(x) else 0) for x in input]))

### PART 2
# function to calculate if a password entry line is valid according tp P2 rules
def isValid2(pw):
    pw = pw.split()
    pw[0] = [int(i) for i in pw[0].split('-')]
    pw[1] = '' + pw[1][0]
    return (1 == int(pw[2][pw[0][0]-1] == pw[1]) + int(pw[2][pw[0][1]-1] == pw[1]))
print(sum([(1 if isValid2(x) else 0) for x in input]))
