### PART 1
# read the input
f = open('input/day25.txt', 'r')
input = [x.strip() for x in f]
f.close()
public_key_card = int(input[0])
public_key_door = int(input[1])
# figure out what the device loop sizes are
def find_loop(public_key):
    loops = 0
    value = 1
    while value != public_key:
        value = value * 7
        value = value % 20201227
        loops += 1
    return loops
loop_card = find_loop(public_key_card)
loop_door = find_loop(public_key_door)
print("      loop_card:", loop_card)
print("      loop_door:", loop_door)
print("public_key_card:", public_key_card)
print("public_key_door:", public_key_door)
# do the crypto handshake computation given subject and loop size
def handshake(subject_num, loop_size):
    value = 1;
    for i in range(loop_size):
        value = value * subject_num
        value = value % 20201227
    return value;
print(" encryption_key:", handshake(public_key_card, loop_door))
print(" encryption_key:", handshake(public_key_door, loop_card))

### PART 2
