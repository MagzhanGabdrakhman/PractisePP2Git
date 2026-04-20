class Snake:
    def __init__(self):
        self.body = [(100, 100)]
        self.dx = 20
        self.dy = 0

    def move(self):
        head = (self.body[0][0] + self.dx, self.body[0][1] + self.dy)
        self.body.insert(0, head)
        self.body.pop()

    def grow(self):
        tail = self.body[-1]
        self.body.append(tail)