"""
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

"""

def valid_parentheses(s: str) -> bool:
    stack = [] # create an empty stack to store a closing bracket for every opening bracket
    for char in s: # iterate through the string
        if char == "(": # if the current character is an opening bracket, add the corresponding closing bracket to the stack
            stack.append(")")
        elif char == "[":
            stack.append("]")
        elif char == "{":
            stack.append("}")
        elif not stack or char != stack.pop(): # if the stack is empty or the current character is not the closing bracket at the top of the stack, return False
            return False
    return not stack # if the stack is empty, return True, otherwise return False. stack empty means everything got closed. stack not empty means something was left open

def test_valid_parentheses():
    assert valid_parentheses("()") == True, "Should be True"
    assert valid_parentheses("()[]{}") == True, "Should be True"
    assert valid_parentheses("(]") == False, "Should be False"
    assert valid_parentheses("([)]") == False, "Should be False"
    assert valid_parentheses("{[]}") == True, "Should be True"

if __name__ == "__main__":
    test_valid_parentheses()
    print("Everything passed")

"""
time complexity: O(n)
    - iterates through the string once so the time is proportional to the length of the string
    - got a run time of 30 ms, which beats 81.8% of users

space complexity: O(n)
    - creates a stack to store a closing bracket for every opening bracket
    - got a memory usage of 14 MB, which beats 17.16% of users

This problem is a stack problem. The stack is used to store a closing bracket for every opening bracket.
When an opening bracket is encountered, the corresponding closing bracket is added to the stack.
When a closing bracket is encountered, it is compared to the closing bracket at the top of the stack.
If the closing bracket at the top of the stack is the same as the current closing bracket, then the top of the stack is popped.
If the closing bracket at the top of the stack is not the same as the current closing bracket, then the string is invalid.
If the stack is empty when a closing bracket is encountered, then the string is invalid.
If the stack is not empty when the end of the string is reached, then the string is invalid.

This one i got some help from copilot. I realize I need to think less about brute force and more about different data structures.

"""