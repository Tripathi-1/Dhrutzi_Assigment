'''Question 3:
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
Example 1:
Input: "()"
Output: true
 
Example 2:
Input: "()[]{}"
Output: true
 
Example 3:
Input: "(]"
Output: false
'''
def isValid(self, string: str) -> bool:
    pairs = {'(':')', '[':']', '{':'}'}
    stack = []

    for char in string:
        if char in pairs.keys():
            stack.append(char)
        elif len(stack) > 0 and pairs.get(stack[-1]) == char:
            stack.pop()
        else: 
            return False

    return len(stack) == 0
