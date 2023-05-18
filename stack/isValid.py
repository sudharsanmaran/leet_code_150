def isValid(s: str) -> bool:
    """t O(n) / s O(1)"""
    stack, brackets = [], {')': '(', ']': '[', '}': '{'}
    for i, char in enumerate(s):
        if char in brackets:
            if stack and brackets[char] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return True if not stack else False


if __name__ == '__main__':
    print(isValid(s="(){{}}{}"))
    print(isValid(s="()[]{"))
    print(isValid(s="([]{}"))
