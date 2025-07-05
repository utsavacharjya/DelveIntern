score_a = 0
score_b = 0

while score_a < 5 and score_b < 5:
    a = input("Player A move: ").casefold()
    b = input("Player B move: ").casefold()

    if a == b:
        print("DRAW")
    elif (a == "stone" and b == "scissor") or \
         (a == "paper" and b == "stone") or \
         (a == "scissor" and b == "paper"):
        print("Player A wins")
        score_a += 1
    else:
        print("Player B wins")
        score_b += 1

if score_a == 5:
    print("Player A wins the game")
else:
    print("Player B wins the game")