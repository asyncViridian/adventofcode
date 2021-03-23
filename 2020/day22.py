### PART 1
# read the input
f = open('input/day22.txt', 'r')
input = [x.strip() for x in f]
f.close()
# process input into two player decks
playerA = [int(i) for i in input[1:input.index('')]]
playerB = [int(i) for i in input[input.index('')+2:]]
# play the game until someone wins!
def play_combat_round(playerA, playerB):
    if playerA[0]>playerB[0]:
        playerA = playerA + [playerA[0]]
        playerA = playerA + [playerB[0]]
    if playerB[0]>playerA[0]:
        playerB = playerB + [playerB[0]]
        playerB = playerB + [playerA[0]]
    return playerA[1:], playerB[1:]
while len(playerA)>0 and len(playerB)>0:
    playerA, playerB = play_combat_round(playerA, playerB)
# calculate the winning player's score
winning = playerA if len(playerA)>0 else playerB
print(sum([winning[(-1*i)-1]* (i+1) for i in range(len(winning))]))

### PART 2
# reset our two player decks
playerA = [int(i) for i in input[1:input.index('')]]
playerB = [int(i) for i in input[input.index('')+2:]]
# now play recursive combat :p
def play_recursivecombat_game(playerA, playerB):
    def play_recursivecombat_round(playerA, playerB):
        if len(playerA)>playerA[0] and len(playerB)>playerB[0]:
            rwinner, tempA, tempB = play_recursivecombat_game(playerA[1:playerA[0]+1], playerB[1:playerB[0]+1])
            if rwinner == 'A':
                playerA = playerA + [playerA[0]]
                playerA = playerA + [playerB[0]]
            else:
                playerB = playerB + [playerB[0]]
                playerB = playerB + [playerA[0]]
        else:
            if playerA[0]>playerB[0]:
                playerA = playerA + [playerA[0]]
                playerA = playerA + [playerB[0]]
            if playerB[0]>playerA[0]:
                playerB = playerB + [playerB[0]]
                playerB = playerB + [playerA[0]]
        return playerA[1:], playerB[1:]
    # keep track of game history
    history = []
    while len(playerA)>0 and len(playerB)>0:
        game_str = str(playerA) + str(playerB)
        if game_str in history:
            return 'A', playerA, playerB
        else:
            history = history + [game_str]
        playerA, playerB = play_recursivecombat_round(playerA, playerB)
    return ('A' if len(playerA)>len(playerB) else 'B'), playerA, playerB
winner, playerA, playerB = play_recursivecombat_game(playerA, playerB)
winning = playerA if winner=='A' else playerB
print(sum([winning[(-1*i)-1]* (i+1) for i in range(len(winning))]))
