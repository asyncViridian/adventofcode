### PART 1
# read the input
f = open('input/day01.txt', 'r')
input = [x.strip() for x in f]
f.close()
# parse input into mass integers
mass = [int(i) for i in input]
# parse mass values into fuel required
fuel = [((i // 3) - 2) for i in mass]
# and get the total fuel requirements...
print(sum(fuel))

### PART 2
# define a function to handle the recursive fuel-requiring-fuel
def fuel_reqs(mass):
    total_fuel = 0
    incr_fuel = (mass // 3) - 2
    while incr_fuel > 0:
        total_fuel += incr_fuel
        incr_fuel = (incr_fuel // 3) - 2
    return total_fuel
# get the total recursive fuel requirements...
print(sum([fuel_reqs(i) for i in mass]))
