import argparse
# --------------------------
# c) Hourglass pattern (centered)
# --------------------------
def pattern_c(n):
    """
    Generates a centered hourglass pattern of stars.

    Args:
        n (int): The number of rows in the upper half of the hourglass.
    """
    # Hollow Diamond inside Square Frame for n = 5

    size = 2 * n - 1  # total number of rows and columns

    for i in range(size):
        for j in range(size):
            # outer frame border
            if i == 0 or i == size - 1:
                print("*", end="")
            # upper half of diamond
            elif i <= n - 1 and (j == i or j == size - i - 1):
                print("*", end="")
            # lower half of diamond
            elif i >= n - 1 and (j == size - i - 1 or j == i):
                print("*", end="")
            else:
                print(" ", end="")
        print()

# --------------------------
# Main Program
# --------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate an equilateral triangle pattern of stars.")
    parser.add_argument("n", type=int, help="The number of rows in the triangle.")
    args = parser.parse_args()
    n = args.n
    pattern_c(n)