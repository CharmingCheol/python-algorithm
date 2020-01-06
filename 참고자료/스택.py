class Stack:
    def __init__(self):
        self.list = []
        self.len = 0

    def push(self, num):
        self.list.append(num)
        self.len += 1

    def top(self):
        return self.list[-1] if self.len != 0 else -1

    def size(self):
        return self.len

    def empty(self):
        return 0 if self.len != 0 else 1

    def pop(self):
        if self.len == 0:
            return -1
        self.len -= 1
        return self.list.pop()