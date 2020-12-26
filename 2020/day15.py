### PART 1
# read the input
f = open('input/day15.txt', 'r')
input = [x.strip() for x in f]
f.close()
# parse input into the numbers
# (assume there's no repeat in the starting numbers)
numbers = [int(i) for i in input[0].split(',')]
def numberGame(numbers, length):
    original_length = len(numbers)
    last_spoken = {}
    just_said = numbers[0]
    for i in range(length):
        if (i < original_length):
            last_spoken[numbers[i]] = (i, i)
            just_said = numbers[i]
        else:
            spacing = last_spoken[just_said]
            if spacing[0]==spacing[1]:
                # the last number was spoken for the first time
                # so say 0
                just_said = 0
                last_spoken[0] = (i, last_spoken[0][0])
            else:
                # the last number was spoken before!
                # so say the interval
                just_said = spacing[0] - spacing[1]
                if just_said not in last_spoken:
                    last_spoken[just_said] = (i, i)
                else:
                    last_spoken[just_said] = (i, last_spoken[just_said][0])
    return just_said
print(numberGame(numbers, 2020))

### PART 2
# do the same thing...
print(numberGame(numbers, 30000000))
