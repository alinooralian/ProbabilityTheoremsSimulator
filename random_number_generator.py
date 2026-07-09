from abc import ABC, abstractmethod
import time


class RandomNumberGenerator(ABC):
    def __init__(self):
        self.seed = int(time.time() * 1000000)

    @abstractmethod
    def create(self):
        pass


class LinearCongruentialGenerator(RandomNumberGenerator):
    coef = 48271
    mod = (2**31) - 1

    def __init__(self):
        super().__init__()
        self.x = (self.seed % (self.mod - 1)) + 1

    def create(self):
        self.x = (self.coef * self.x) % self.mod
        return self.x / self.mod
