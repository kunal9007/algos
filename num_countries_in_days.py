# def num_countries_in_days(max_days, factor):
#     num_countries = 0
#     days_spent = 0
#     while days_spent < max_days:
#         num_countries += 1
#         days_spent += 1  # Spend 1 day in the current country
#         if days_spent >= max_days:
#             break
#         days_spent *= factor  # Apply the growth factor for the next country visit
#     return num_countries

def num_countries_in_days(max_days, factor):
    if max_days <= 0:
        return 0  # If max_days is less than or equal to 0, the influencer cannot visit any country

    if max_days <= 1:
        return 1  # If max_days is less than or equal to 1, the influencer can only visit one country

    time_left = max_days
    num_countries = 0
    days_spent = 0
    while days_spent < max_days:
        num_countries += 1
        days_spent += 1  # Spend 1 day in the current country
        print("Number of countries", num_countries, "days_spent", days_spent)
        # if days_spent >= max_days:
        #     break
        print("factored days_spent", days_spent)
        time_left = max_days - days_spent
        days_spent *= factor  # Apply the growth factor for the next country visit
        next_trip = days_spent
        if days_spent >= max_days:
            break
    print(num_countries)
    return num_countries


num_countries_in_days(2, 1.2)


# run_cases = [
#     (2, 1.2, 1),
#     (3, 1.2, 2),
# ]

# submit_cases = run_cases + [
#     (10, 1.2, 6),
#     (100, 1.2, 16),
#     (200, 1.2, 20),
#     (1000, 1.3, 21),
#     (0, 1.5, 0),
#     (1, 0.5, 1),
# ]


# def test(input1, input2, expected_output):
#     print("---------------------------------")
#     print(f"Inputs:")
#     print(f" * Max days: {input1}")
#     print(f" * Time factor: {input2}")
#     print(f"Expecting: {expected_output}")
#     result = num_countries_in_days(input1, input2)
#     print(f"Actual: {result}")
#     if result == expected_output:
#         print("Pass")
#         return True
#     print("Fail")
#     return False


# def main():
#     passed = 0
#     failed = 0
#     for test_case in test_cases:
#         correct = test(*test_case)
#         if correct:
#             passed += 1
#         else:
#             failed += 1
#     if failed == 0:
#         print("============= PASS ==============")
#     else:
#         print("============= FAIL ==============")
#     print(f"{passed} passed, {failed} failed")


# test_cases = submit_cases
# if "__RUN__" in globals():
#     test_cases = run_cases

# main()
