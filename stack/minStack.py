

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if self.min_stack:
            self.min_stack.append(min(self.min_stack[-1], val))
        else:
            self.min_stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]


if __name__ == '__main__':
    obj = MinStack()
    print(obj.pop())
    print(obj.top())
    print(obj.push(-2))
    print(obj.push(2))
    print(obj.push(-3))
    print(obj.top())
    print(obj.pop())
    print(obj.getMin())
