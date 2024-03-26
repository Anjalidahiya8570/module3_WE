class Odometer:
    @staticmethod
    def is_ascending(k: int) -> bool:
        sn = str(k)
        return all([a < b for a, b in zip(sn, sn[1:])])

    def __init__(self, size):
        DIGITS = "123456789"
        self.SIZE = size
        self.START = int(DIGITS[:size])
        self.LIMIT = int(DIGITS[-size:])
        self.reading = self.START

    def __repr__(self):
        return f'{self.START}<{self.reading}>{self.LIMIT}'

    def __str__(self):
        return str(self.reading)

    def forward(self, steps=1):
        for _ in range(steps):
            if self.reading == self.LIMIT:
                self.reading = self.START
            else:
                self.reading += 1
                while not Odometer.is_ascending(self.reading):
                    self.reading += 1

    def backward(self, steps=1):
        for _ in range(steps):
            if self.reading == self.START:
                self.reading = self.LIMIT
            else:
                self.reading -= 1
                while not Odometer.is_ascending(self.reading):
                    self.reading -= 1

    def distance(self, other)->int:
        if self.SIZE != other.SIZE:
            return -1
        self_copy = Odometer(self.SIZE)
        self_copy.reading = self.reading
        diff = 0
        while self_copy.reading != other.reading:
            self_copy.forward()
            diff += 1
        return diff
