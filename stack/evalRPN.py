from typing import List


def evalRPN(tokens: List[str]) -> int:
    stack = []
    for char in tokens:
        if char in {"*", "/", "-", "+"}:
            val_2, val_1 = stack.pop(), stack.pop()
            if char == "*":
                val = val_2 * val_1
            elif char == "/":
                val = int(val_2 / val_1)
            elif char == "+":
                val = val_2 + val_1
            elif char == "-":
                val = val_2 - val_1
            stack.append(val)
        else:
            stack.append(int(char))
    return stack[0]


def evalRPN_1(tokens: List[str]) -> int:
    stack, operators = [], {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: int(a / b),
    }
    for char in tokens:
        if char in operators:
            right, left = stack.pop(), stack.pop()
            stack.append(operators[char](left, right))
        else:
            stack.append(int(char))
    return stack[0]


if __name__ == "__main__":
    print(evalRPN(["2", "3", "+", "4", "*", "15", "-"]))
    print(evalRPN(["4", "13", "5", "/", "+"]))
    print(
        evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
    )
