""" def power_set(input_set):
    print("input_set", input_set)
    if len(input_set) == 0:
        return []
    power_set = []
    power_set.append([])
    power_set.append(input_set)
    power_set(input_set.pop())
    power_set(power_set.pop(0))
 """


def power_set(input_set):
    print("input_set", input_set)
    if len(input_set) == 0:
        return [[]]  # Return a list containing an empty list
    first_element = input_set[0]  # Get the first element of the input set
    rest_elements = input_set[1:]  # Get the rest of the elements
    subsets = power_set(
        rest_elements
    )  # Recursively call power_set with the rest of the elements
    subsets_with_first = [
        [first_element] + subset for subset in subsets
    ]  # Add first_element to each subset
    return subsets + subsets_with_first  # Combine subsets with subsets_with_first


# Example usage:
# input_set = [1, 2, 3]
# print(power_set(input_set))


# from main import *

run_cases = [
    ([1, 2], [[1, 2], [2], [1], []]),
    ([1, 2, 3], [[1, 2, 3], [2, 3], [1, 3], [3], [1, 2], [2], [1], []]),
]

submit_cases = run_cases + [
    ([], [[]]),
    ([1], [[1], []]),
    (
        [1, 2, 3, 4],
        [
            [1, 2, 3, 4],
            [2, 3, 4],
            [1, 3, 4],
            [3, 4],
            [1, 2, 4],
            [2, 4],
            [1, 4],
            [4],
            [1, 2, 3],
            [2, 3],
            [1, 3],
            [3],
            [1, 2],
            [2],
            [1],
            [],
        ],
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    for i in input1:
        print(f" * {i}")
    print(f"Expecting: {expected_output}")
    result = power_set(input1)
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
