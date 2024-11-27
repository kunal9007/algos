import math


def prime_factors(n):
    factors = []
    remainder = 0

    while (n % 2) == 0:
        print("before::n", n)
        factors.append(2)
        n /= 2
        print("n", n, "factors", factors, "remainder", remainder)

    odd_factor = 3
    while odd_factor <= math.sqrt(n):
        print("odd remainder:::::::::::::::::")
        print(remainder, "square_root", math.sqrt(n), "odd_factor", odd_factor)
        while n % odd_factor == 0:
            factors.append(odd_factor)
            n /= odd_factor

        odd_factor += 2
        print("odd n +++++++++++++++++++++", n, "factors", factors)

    if n > 2:
        print("n > 2", n)
        factors.append(n)

    return factors


#     return factors

# def prime_factors(n):
#     factors = []

#     # Step 1: Divide by 2 as many times as possible
#     while n % 2 == 0:
#         factors.append(2)
#         n //= 2

#     # Step 2: Find prime factors for odd numbers from 3 to sqrt(n)
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#         while n % i == 0:
#             factors.append(i)
#             n //= i

#     # Step 3: If n is still greater than 2, it's a prime factor itself
#     if n > 2:
#         factors.append(n)

#     return factors

# def prime_factors(n):
#     factors = []
#     remainder = 0

#     # while remainder == 0 and n >= 2:
#     while n % 2 == 0:
#         # remainder = n % 2
#         print("before::n", n)
#         factors.append(2)
#         n /= 2
#         # if n == s.0:
#         print("n", n)
#         print("factors", factors)
#         print("remainder", remainder)

#         # if remainder != 0:
#         #     print("before::odd n +++++++++++++++++++++", n)
#         #     factors.append(n)
#     odd_factor = 3
#     while odd_factor <= math.sqrt(n):
#         remainder = n % odd_factor
#         print(
#             "odd remainder:::::::::::::::::",
#             remainder,
#             "square_root",
#             math.sqrt(n),
#             "odd_factor",
#             odd_factor,
#         )
#         while remainder == 0:
#             n /= odd_factor
#             factors.append(n)
#             remainder = n % odd_factor
#         odd_factor += 2
#         print("odd n +++++++++++++++++++++", n, "factors", factors)

#     if n > 2:
#         print("n > 2", n)
#         factors.append(n)

#     return factors

#     return factors


# def prime_factors(n):
#     factors = []
#     remainder = 0

#     while remainder == 0:
#         remainder = n % 2
#         n /= 2
#         factors.append(2)

#     while remainder != 0:
#         odd_factor = 3
#         while odd_factor <= math.sqrt(n):
#             remainder = n % odd_factor
#             if remainder != 0:
#                 odd_factor += 2
#             else:
#                 n /= odd_factor
#                 factors.append(odd_factor)

#     return factors


# Example usage:
print(prime_factors(24))  # Output: [2, 2, 2, 3]

run_cases = [(8, [2, 2, 2]), (10, [2, 5]), (24, [2, 2, 2, 3])]

submit_cases = run_cases + [
    (49, [7, 7]),
    (77, [7, 11]),
    (4, [2, 2]),
    (64, [2, 2, 2, 2, 2, 2]),
    (63, [3, 3, 7]),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expecting: {expected_output}")
    result = prime_factors(input1)
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
