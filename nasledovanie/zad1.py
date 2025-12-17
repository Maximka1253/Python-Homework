class Counter:
    def __init__(self, start=0):
        self.value = max(0, start)

    def inc(self, amount=1):
        self.value += amount

    def dec(self, amount=1):
        self.value -= amount
        if self.value < 0:
            self.value = 0

class NonDecCounter(Counter):
    def dec(self, amount=1):
        pass

class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        super().__init__(start)
        self.limit = limit
        if self.value > self.limit:
            self.value = self.limit

    def inc(self, amount=1):
        temp_val = self.value + amount
        if temp_val > self.limit:
            self.value = self.limit
        else:
            self.value = temp_val

c = Counter(start=5)
c.inc()
c.dec(10)
print(f"Counter: {c.value}")

nd = NonDecCounter(start=5)
nd.inc(5)
nd.dec(3)
print(f"NonDecCounter: {nd.value}")

lc = LimitedCounter(start=8, limit=10)
lc.inc(11)
print(f"LimitedCounter: {lc.value}")
lc.dec(5)
print(f"LimitedCounter (после уменьшения): {lc.value}")