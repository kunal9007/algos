def is_balanced(input_str):
    stack = Stack()
    if len(input_str) == 0:
        return True
    if input_str[0] == ")":
        return False
    i = 0
    while i < len(input_str):
        if input_str[i] == "(":
            stack.push("(")
            print("push", stack.peek())
        if input_str[i] == ")":
            if stack.pop() is None:
                return False
            print("pop", stack.peek())
        i += 1
    print("out", stack.peek())
    if stack.peek() == None:
        return True
    else:
        return False


# def is_balanced(input_str):
#     stack = Stack()  # Create an instance of the Stack class

#     for char in input_str:
#         if char == "(":
#             stack.push("(")  # Push "(" onto the stack
#         elif char == ")":
#             if stack.pop() is None:  # Try to pop from the stack
#                 return False  # If stack is empty, parentheses are not balanced

#     # If the stack is empty after processing all characters, parentheses are balanced
#     return stack.peek() is None


# don't modify below this line


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items) - 1]


# stack = Stack()

run_cases = [
    ("(", False),
    ("()", True),
    ("(())", True),
]

submit_cases = run_cases + [
    ("()()", True),
    ("(()))", False),
    ("((())())", True),
    ("(()(()", False),
    (")(", False),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expecting: {expected_output}")
    result = is_balanced(input1)
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
