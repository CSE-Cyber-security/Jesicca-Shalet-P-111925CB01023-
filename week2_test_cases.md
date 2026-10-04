# Test Cases – Factorial Calculator

| TC  | Feature            | Menu | Input        | Expected Output                                   | Result |
|-----|--------------------|------|--------------|---------------------------------------------------|--------|
| 01  | Iterative          | 1    | 5            | `5! = 120 (Iterative method)`                     | Pass   |
| 02  | Recursive          | 2    | 5            | `5! = 120 (Recursive method)`                     | Pass   |
| 03  | Zero edge case     | 1    | 0            | `0! = 1`                                          | Pass   |
| 04  | One edge case      | 1    | 1            | `1! = 1`                                          | Pass   |
| 05  | Maximum value      | 2    | 20           | `20! = 2432902008176640000`                       | Pass   |
| 06  | Table              | 3    | 5            | Rows for N = 0..5 with correct factorials         | Pass   |
| 07  | History            | 4    | –            | Lists previous calculations with method           | Pass   |
| 08  | Summary            | 5    | –            | Total, iterative, recursive count, largest N      | Pass   |
| 09  | Clear history      | 6    | –            | `History cleared successfully.`; history empty    | Pass   |
| 10  | Negative number    | 1    | -3           | `[ERROR] Factorial is not defined for negative numbers.` | Pass |
| 11  | Overflow           | 1    | 21           | `[ERROR] ... too large. Maximum supported value is 20` | Pass |
| 12  | Non-numeric input  | 1    | abc          | `[ERROR] Invalid input. Please enter a whole number.` | Pass |
| 13  | Decimal input      | 1    | 4.5          | `[ERROR] Invalid input. Please enter a whole number.` | Pass |
| 14  | Empty input        | 1    | (Enter only) | `[ERROR] Invalid input. Please enter a whole number.` | Pass |
| 15  | Invalid menu       | –    | 9            | `[ERROR] Invalid choice. Enter a number from 1 to 7.` | Pass |
| 16  | Exit               | 7    | –            | `Exiting... Goodbye!`                             | Pass |
