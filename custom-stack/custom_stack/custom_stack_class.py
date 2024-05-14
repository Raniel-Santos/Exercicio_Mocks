class CustomStack:
    def __init__(self, pLimit):
        self.limit = pLimit
        self.elements = []

    def size(self):
        return len(self.elements)

    def isEmpty(self):
        return self.size() == 0

    def push(self, element):
        if self.size() == self.limit:
            raise StackFullException()
        self.elements.append(element)

    def pop(self):
        if self.isEmpty():
            raise StackEmptyException()
        return self.elements.pop()

    def top(self):
        if self.isEmpty():
            raise StackEmptyException()
        return self.elements[-1]

class StackEmptyException(Exception):
    def __init__(self, msg="Stack está vazio."):
        self.msg = msg
        super().__init__(self.msg)

class StackFullException(Exception):
    def __init__(self, message="Stack is full"):
        self.message = message
        super().__init__(self.message)

class NumberAscOrder:
    @staticmethod
    def sort(stack):
        if stack.isEmpty():
            return []
        numbers = []
        while not stack.isEmpty():
            numbers.append(stack.pop())
        numbers.sort()
        return numbers