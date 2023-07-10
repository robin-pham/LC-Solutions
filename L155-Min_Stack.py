L155 - Min_Stack


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        if not self.stack or val < self.stack[-1][1]:
            self.stack.append((val, val))
        else:
            self.stack.append((val, self.stack[-1][1]))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]
