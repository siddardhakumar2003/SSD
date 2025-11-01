import argparse
# --------------------------
# b) Spiral numbers
# --------------------------
def pattern_b(n):
    """
    Generates a spiral pattern of numbers in an n x n matrix.

    Args:
        n (int): The size of the square matrix.
    """
    matrix = [[0]*n for _ in range(n)]

    top, bottom, left, right = 0, n-1, 0, n-1
    num = 1

    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    for row in matrix:
        print(" ".join(f"{x:2d}" for x in row))

# --------------------------
# Main Program
# --------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate an equilateral triangle pattern of stars.")
    parser.add_argument("n", type=int, help="The number of rows in the triangle.")
    args = parser.parse_args()
    n = args.n
    pattern_b(n)