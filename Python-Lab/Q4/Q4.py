import argparse
# --------------------------
# a) Equilateral triangle
# --------------------------
def pattern_a(n):
    """
    Generates an equilateral triangle pattern of stars.

    Args:
        n (int): The number of rows in the triangle.
    """
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)

# --------------------------
# Main Program
# --------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate an equilateral triangle pattern of stars.")
    parser.add_argument("n", type=int, help="The number of rows in the triangle.")
    args = parser.parse_args()
    n = args.n
    pattern_a(n)