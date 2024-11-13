def get_change(amount):
    # bill denominations
    denominations = {
        "hundred dollar bill": 100.00,
        "fifty dollar bill": 50.00,
        "twenty dollar bill": 20.00,
        "ten dollar bill": 10.00,
        "five dollar bill": 5.00,
        "one dollar bill": 1.00,
        "quarter": 0.25,
        "dime": 0.10,
        "nickel": 0.05,
        "penny": 0.01,
    }

    # store the count of each denomination
    change = {}

    # iterate through each denomination in descending order
    for name, value in denominations.items():
        count = int(amount // value)
        if count > 0:
            change[name] = count
            amount -= count * value
        amount = round(amount, 2)

    return change


def run_tests():
    test_cases = [
        (20, {"twenty dollar bill": 1}),
        (19.99, {
            "ten dollar bill": 1,
            "five dollar bill": 1,
            "one dollar bill": 4,
            "quarter": 3,
            "dime": 2,
            "penny": 4
        }),
        (0, {}),
        (186.41, {
            "hundred dollar bill": 1,
            "fifty dollar bill": 1,
            "twenty dollar bill": 1,
            "ten dollar bill": 1,
            "five dollar bill": 1,
            "one dollar bill": 1,
            "quarter": 1,
            "dime": 1,
            "nickel": 1,
            "penny": 1
        }),
        (0.41, {
            "quarter": 1,
            "dime": 1,
            "nickel": 1,
            "penny": 1
        }),
        (0.99, {
            "quarter": 3,
            "dime": 2,
            "penny": 4
        }),
        (123.6, {
            "hundred dollar bill": 1,
            "twenty dollar bill": 1,
            "one dollar bill": 3,
            "quarter": 2,
            "dime": 1
        })
    ]

    # run test cases
    for i, (input_amount, expected_output) in enumerate(test_cases, start=1):
        result = get_change(input_amount)
        if result == expected_output:
            print(f"Test case {i} passed.")
        else:
            print(f"Test case {i} failed.")
            print(f"  Input: {input_amount}")
            print(f"  Expected: {expected_output}")
            print(f"  Got: {result}")

    try:
        # take input from user
        amount = float(input("Enter the amount: $"))
        if amount < 0:
            print("Please enter a positive amount.")
            return
        elif (amount * 100) % 1 != 0:
            print("Please enter up to two decimal places.")
            return

        # calculate change
        change = get_change(amount)

        # print result
        print("Exact change:")
        for denomination, count in change.items():
            if count > 1:
                if denomination == "penny":
                    print(f"{count} pennies")
                else:
                    print(f"{count} {denomination}s")
            else:
                print(f"{count} {denomination}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    run_tests()