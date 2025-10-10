# Q9.py - Character Sequence Scoring Program

def char_score(ch):
    """Return basic score for a single character."""
    if ch.isalpha():
        return ord(ch.upper()) - ord('A') + 1
    elif ch.isdigit():
        return int(ch) * 3
    else:
        return 0


def main():
    seq = input("Enter 5 characters: ").strip().upper()

    if len(seq) != 5 or any(not (ch.isalpha() or ch.isdigit()) for ch in seq):
        print("Invalid input! Please enter exactly 5 characters (A-Z, 0-9).")
        return

    total = 0
    for i, ch in enumerate(seq, start=1):
        # 1. Basic Points
        total += char_score(ch)

        # 2. Position Bonus
        if i % 2 == 1:  # odd position
            total += 5
        else:  # even position
            total += 10

        # 3. Special Rule (after each character)
    if total % 2 == 0:
        total = total * 12 // 10  # multiply by 1.2 (integer division)
    else:
        total += 15

    print(f"Final Score: {total}")


if __name__ == "__main__":
    main()
