class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.location = 0

    def append(self, item):
        self.data.insert(self.location, item)
        if len(self.data) > self.capacity:
                self.data.pop(self.location + 1)

        if self.location == self.capacity:
            self.location = 0
        else:
            self.location += 1

    def get(self):
        return [i for i in self.data]


