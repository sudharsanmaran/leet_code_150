from typing import List


def evalRPN(tokens: List[str]) -> int:
    stack = []
    for char in tokens:
        if char in {'*', '/', '-', '+'}:
            val_1 = stack.pop()
            val_2 = stack.pop()
            if char == '*':
                val = val_2 * val_1
            elif char == '/':
                val = int(val_2/val_1)
            elif char == '+':
                val = val_2 + val_1
            elif char == '-':
                val = val_2 - val_1
            stack.append(val)
        else:
            stack.append(int(char))

    return stack.pop()


if __name__ == '__main__':
    print(evalRPN(['2', '3', '+', '4', '*', '15', '-']))
    print(evalRPN(["4", "13", "5", "/", "+"]))
    print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
