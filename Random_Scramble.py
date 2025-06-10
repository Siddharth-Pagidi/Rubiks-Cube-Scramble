# A simple Rubik's cube scrambler
import random as rand

print("\n")
moves = ["R", "L", "F", "B", "U", "D", "M",
         "R'", "L'", "F'", "B'", "U'", "D'", "M'",
         "R2", "L2", "F2", "B2", "U2", "D2", "M2",
         "R'2", "L'2", "F'2", "B'2", "U'2", "D'2", "M'2"
]

numberOfMoves = rand.randint(20, 25)
i = 0

for i in range(numberOfMoves):
    move = rand.randint(0, len(moves) - 1)
    print(moves[move], end = ' ')

print("\n")

