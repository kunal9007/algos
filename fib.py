def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


# def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev1 = 1
    prev2 = 0
    i = 0
    while i < n - 1:
        current = prev2 + prev1
        # print("current: ", current)
        prev2 = prev1
        # print("prev2", prev2)
        prev1 = current
        # print("prev1", prev1)
        i += 1

    return prev1


run_cases = [
    (1, 1),
    (10, 55),
    (20, 6765),
]

submit_cases = run_cases + [
    (0, 0),
    (40, 102334155),
    (70, 190392490709135),
    (160, 1226132595394188293000174702095995),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expecting: {expected_output}")
    result = fib(input1)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
