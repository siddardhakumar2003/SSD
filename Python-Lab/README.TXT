## Lab Overview:

This lab contains 10 Python programming exercises (Q1.py to Q10.py) focusing on variables, operations, branching, looping, and computational logic. The tasks include number processing, mystical number identification, memory games, pattern generation, score calculation, and a text-based adventure game.

Each question has been implemented according to the instructions and output format specified in the lab manual. Assumptions and input validations are included wherever necessary.

---

## Folder Structure for Submission:

```
<roll_number>.zip
│
├── Q1
│   ├── Q1.py
│   └── Q1_output.txt
│
├── Q2
│   ├── Q2.py
│   └── Q2_output.txt
│
├── Q3
│   ├── Q3.py
│   └── Q3_output.txt
│
├── Q4
│   ├── Q4.py
│   └── Q4_output.txt
│
├── Q5
│   ├── Q5.py
│   └── Q5_output.txt
│
├── Q6
│   ├── Q6.py
│   └── Q6_output.txt
│
├── Q7
│   ├── Q7.py
│   └── Q7_output.txt
│
├── Q8
│   ├── Q8.py
│   └── Q8_output.txt
│
├── Q9
│   ├── Q9.py
│   └── Q9_output.txt
│
└── Q10
    ├── Q10.py
    └── Q10_output.txt
```

---

## Question Summary:

### Q1.py – FizzBuzz Variant

* Prints numbers from 1 to `n` with replacements:

  * Divisible by 3 → "Three"
  * Divisible by 5 → "Five"
  * Divisible by both → "ThreeFive"

---

### Q2.py – Mystical Numbers

* Finds all mystical numbers in a user-defined range.
* A mystical number:

  1. Is even
  2. Sum of digits is prime
  3. Digits in strictly ascending order

---

### Q3.py – Memory Game

* Asks user for 3-5 numbers to memorize.
* Generates random numbers (1-9) for the user to remember.
* Evaluates correctness after user input.

---

### Q4.py, Q5.py, Q6.py – Pattern Printing

* Constructs specific patterns using loops.
* Templates provided; implemented logic replaces `pass` statements.

---

### Q7.py – Mastermind Logician

* Simulates a 10-round game for Player A & Player B.
* Calculates final numeric score based on moves, penalties, and bonuses.

---

### Q8.py – Crystal Cavern Explorer (Text-Based Adventure)

* Player navigates through 8 chambers collecting crystals and avoiding traps.
* Calculates final score based on crystal points, bonuses, and remaining health.

---

### Q9.py – Character Sequence Scoring

* Accepts exactly 5 characters (A-Z, 0-9).
* Calculates score based on letter positions, digit multipliers, position bonuses, and special rules.

---

### Q10.py – Multi-Round Character Sequence Processing

* Processes 2-5 rounds of 4-character sequences.
* Computes stage-wise points, applies cross-round modifiers, and calculates final score.

---

## Assumptions & Notes:

* All inputs are validated; invalid inputs are handled gracefully.
* Output format strictly follows lab manual requirements (spacing, newlines, symbols).
* Random numbers in Q3 are generated using Python’s `random` module.
* Maximum health in Q8 cannot exceed 100.
* For prime number checks, standard algorithms are used.
* Integer arithmetic is used for score calculations unless specified otherwise.
* Any assumptions or deviations from the problem statement are documented in the respective code file comments.

---

## How to Run:

1. Navigate to the question folder (e.g., `Q1`).
2. Run the Python program:

   ```bash
   python Q1.py
   ```
3. To generate output file, run:

   ```bash
   python Q1.py > Q1_output.txt
   ```
4. Repeat for Q2 to Q10.

