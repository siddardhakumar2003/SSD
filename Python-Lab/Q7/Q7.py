playerA_moves = list(map(int, input("Enter 10 numbers for Player A (separated by spaces): ").split()))

playerB_moves = list(map(int, input("Enter 10 numbers for Player B (separated by spaces): ").split()))

# Validate input lengths
if len(playerA_moves) != 10 or len(playerB_moves) != 10:
    print("Error: Each player must enter exactly 10 numbers.")
    exit()

total_score = 0

for round_num in range(0,10):
    A = playerA_moves[round_num]
    B = playerB_moves[round_num]

    total_score += A

    # Penalty condition
    if A < B:
        total_score -= B

    # Bonus condition
    elif A == B:
        total_score += B
    # print(A," ",B," ",total_score)

print(f"The final numeric score after all 10 rounds: {total_score}")
