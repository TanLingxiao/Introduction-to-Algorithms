class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        print(str(item) + " pushed to stack ")

    def pop(self):
        if self.isEmpty():
            print('Stack is empty')
        return self.stack[-1]


if __name__ == '__main__':

    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
