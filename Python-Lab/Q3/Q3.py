import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    try:
        count = int(input("How many numbers do you want to memorize (between 3 and 5)? "))
        if 3 <= count <= 5:
            break
        else:
            print("Please enter a number between 3 and 5.")
    except ValueError:
        print("Invalid input. Please enter a number between 3 and 5.")

# Generate random sequence
sequence = [random.randint(1, 9) for _ in range(count)]

print("\nMemorize these numbers:")
print("\n".join(str(num) for num in sequence))
input("\nPress Enter when you are ready to recall...")

# Clear screen after user presses Enter
clear_screen()

print("Now, enter the numbers in the same order:")
user_input = []
for i in range(count):
    val = int(input(f"Number {i+1}: "))
    user_input.append(val)

correct = sum(1 for i in range(count) if sequence[i] == user_input[i])

if correct == count:
    print("\nCorrect! You have a great memory!")
else:
    print(f"\nOops! You remembered {correct} out of {count} correctly.")
