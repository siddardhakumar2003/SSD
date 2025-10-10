# Q2.py
# Program to find and print all "mystical numbers" within a user-defined range.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def digits_strictly_ascending(num):
    digits = str(num)
    for i in range(len(digits) - 1):
        if digits[i] >= digits[i + 1]:
            return False
    return True

def sum_of_digits(num):
    return sum(int(d) for d in str(num))

start = int(input("Please enter the starting number for the range: "))
end = int(input("Please enter the ending number for the range: "))

print("Searching for mystical numbers...\n------------------------------")

for num in range(start, end + 1):
    if num % 2 == 0:  # Condition 1
        digit_sum = sum_of_digits(num)
        if is_prime(digit_sum):  # Condition 2
            if digits_strictly_ascending(num):  # Condition 3
                print(f"Mystical Number: {num} -> Digit Sum: {digit_sum}")
