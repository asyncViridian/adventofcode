### PART 1
# read the input
f = open('input/day05.txt', 'r')
input = [x.strip() for x in f]
f.close()
# calculate the (row number, column number)
def getSeatLoc(passnum):
    rownum = int(''.join([('0' if (e == 'F') else '1') for e in passnum[:7]]), 2)
    colnum = int(''.join([('0' if (e == 'L') else '1') for e in passnum[7:]]), 2)
    return rownum, colnum
# get the seat locations for all tickets
seatLocs = [getSeatLoc(e) for e in input]
seatNums = [(8*e[0]+e[1]) for e in seatLocs]
print(max(seatNums))

### PART 2
seatNums = sorted(seatNums)
# calculate if there's a gap between adjacent seats in the sorted list
seatContig = [(seatNums[i]+1 == seatNums[i+1]) for i in range(len(seatNums)-1)]
# we're guaranteed that our seat isn't at the end
# this output list should contain only ONE seat, and its ID is one lower than our seat
print([e for e in zip(seatNums[:-1], seatContig) if (not e[1])])
