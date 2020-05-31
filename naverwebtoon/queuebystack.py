class queue:
    def __init__(self):        
        self.inBox = []
        self.outBox = []

    def push(self, data):
        self.inBox.append(data)

    def pop(self):
        if not self.outBox:
            while self.inBox:
                t = self.inBox.pop()
                self.outBox.append(t)
        return self.outBox.pop()

if __name__ == "__main__":
    q = queue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)

    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
