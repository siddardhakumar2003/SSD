# Q10.py - Multi-Round Character Sequence Processor

def char_value(ch, pos):
    """Return base points for a single character given its position (1-4)."""
    if ch.isalpha():
        return ord(ch.upper()) - ord('A') + 1
    elif ch.isdigit():
        return int(ch) * pos
    return 0


def is_palindrome(num):
    """Check if a number is palindrome."""
    s = str(num)
    return s == s[::-1]


def main():
    # Input number of rounds
    rounds = input("Enter number of rounds (2-5): ").strip()
    if not rounds.isdigit() or not (2 <= int(rounds) <= 5):
        print("Invalid input! Please enter a number between 2 and 5.")
        return
    rounds = int(rounds)

    round_scores = []

    # Stage 1: Individual Round Processing
    for r in range(1, rounds + 1):
        seq = input(f"Round {r} - Enter 4 characters: ").strip().upper()
        if len(seq) != 4 or any(not (ch.isalpha() or ch.isdigit()) for ch in seq):
            print("Invalid input! Each round must have 4 characters (A-Z, 0-9).")
            return

        total = 0
        for pos, ch in enumerate(seq, start=1):
            points = char_value(ch, pos)
            # Position modifier
            if pos % 2 == 1:
                points += 3
            else:
                points += 7
            total += points

        # Stage 2: Round-to-Round Effects
        if r > 1 and total > round_scores[-1]:
            total = (total * 15) // 10  # ×1.5 integer division

        if total % r == 0:
            total += 20

        if '7' in str(total):
            total -= 10

        round_scores.append(total)

    # Stage 3: Cross-Round Analysis
    highest = max(round_scores)
    lowest = min(round_scores)
    avg = sum(round_scores) // len(round_scores)
    above_avg_count = sum(1 for x in round_scores if x > avg)

    # Stage 4: Final Calculation
    base_score = sum(round_scores)

    if above_avg_count <= 1:
        final = (base_score * 9) // 10
    elif above_avg_count <= 3:
        final = (base_score * 11) // 10
    else:
        final = (base_score * 13) // 10

    if is_palindrome(base_score):
        final += 50

    # Output section
    print("Processing Results:")
    for i, score in enumerate(round_scores, start=1):
        print(f"Round {i} Score: {score}")
    print(f"Above Average Rounds: {above_avg_count}")
    print(f"Final Score: {final}")


if __name__ == "__main__":
    main()

