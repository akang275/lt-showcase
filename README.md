# Exact Change Calculator

This application calculates the exact change for a given amount in US currency denominations with the least amount of bills and coins. It supports values up to two decimal places.

## Features

- Calculates the minimum amount of bills and coins needed for any amount in US currency.
- Supports various denominations: hundreds, fifties, twenties, tens, fives, ones, quarters, dimes, nickels, and pennies.
- Includes automated test cases to verify correctness.

## Requirements

- Python 3.x

## Install and run

Clone this repository to your local machine:

```bash
git clone https://github.com/akang275/lt-showcase.git
cd lt-showcase
```

Run the application to calculate the exact change for a user-specified amount:
```bash
python exact_change.py
```

The program will prompt for an input amount:
```bash
Enter the amount: $19.99
```
The output will display the minimum number of each denomination needed for the amount:
```bash
Exact change:
1 ten dollar bill
1 five dollar bill
4 one dollar bills
3 quarters
2 dimes
4 pennies
```