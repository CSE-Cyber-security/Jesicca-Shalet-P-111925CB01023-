# Week 02 – Factorial Calculator (C)

A menu-driven C program that calculates factorials using both iterative and
recursive methods, with input validation, file-based history and a summary report.

## Features
- Factorial using **iteration** and **recursion**
- Factorial table from 0 to N
- Calculation history saved to `data/factorial_history.txt`
- Summary (total, iterative/recursive count, largest N)
- Input validation: negative, non-numeric, decimal, empty, and overflow (>20)

## Why the limit of 20?
`21!` exceeds the range of `unsigned long long` (max 18,446,744,073,709,551,615),
so inputs above 20 are rejected to prevent overflow.

## Project Structure
```
Week-02-Factorial-Calculator/
├── src/factorial.c
├── data/factorial_history.txt
├── tests/test_cases.md
├── screenshots/
└── README.md
```

## Compile & Run (from project root)
```bash
gcc src/factorial.c -o factorial
./factorial          # Windows: factorial.exe
```

## Sample Output
```
Enter your choice: 1
Enter a number (0-20): 5

5! = 120   (Iterative method)
```

## Screenshots to capture
01-calculate-iterative.png, 02-calculate-recursive.png, 03-factorial-table.png,
04-history.png, 05-summary.png, 06-clear-history.png, 07-input-validation.png

## Concepts Used
Functions, recursion, loops, switch-case, file handling, `fgets` + `strtol` validation.
