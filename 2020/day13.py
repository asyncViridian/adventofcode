### PART 1
# read the input
f = open('input/day13.txt', 'r')
input = [x.strip() for x in f]
f.close()
# parse buses data
bustime = int(input[0])
buses = [int(e) for e in input[1].split(',') if (e != 'x')]
# calculate first bus that leaves at least at bustime
departtime = bustime
can_depart = any([(departtime%b==0) for b in buses])
while not can_depart:
    departtime += 1
    can_depart = any([(departtime%b==0) for b in buses])
# get the (bus number)*(wait time)
print([b for b in buses if (departtime%b==0)][0]*(departtime-bustime))

### PART 2
buses = [(int(e) if (e != 'x') else 1) for e in input[1].split(',')]
def time_is_valid(time, buses):
    for i in range(len(buses)):
        if buses[i]!=1 and not (time + i)%buses[i]==0:
            return False
    return True
start = max(buses[:2])-buses.index(max(buses[:2]))
interval = max(buses[:2])
# build up the junction between points first
for i in range(2, len(buses)+1):
    time = start
    while not time_is_valid(time, buses[:i]):
        time += interval
    start_step = time
    time += interval
    while not time_is_valid(time, buses[:i]):
        time += interval
    interval_step = time - start_step
    start = max([start, start_step])
    interval = max([interval, interval_step])
print(start)

### PART 2 - the brute force method, which is slow lol
# buses = [(int(e) if (e != 'x') else 1) for e in input[1].split(',')]
# # Show us the parameters of the problem we're solving!
# print([(e, buses.index(e)) for e in buses if e!=1])
# # check if this time matches the list
# def time_is_valid(time, buses):
#     for i in range(len(buses)):
#         if buses[i]!=1 and not (time + i)%buses[i]==0:
#             return False
#     return True
# # get the index of the largest bus
# largest_bus = max(buses)
# largest_bus_i = buses.index(largest_bus)
# multiplier = int(100000000000000/largest_bus)-1
# checking_time = largest_bus*multiplier-largest_bus_i
# while not time_is_valid(checking_time, buses):
#     checking_time += largest_bus
# print(checking_time)
