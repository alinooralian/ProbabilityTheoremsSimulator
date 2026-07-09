from abc import ABC, abstractmethod
from random_number_generator import RandomNumberGenerator
import math


class BaseDistribution(ABC):
    def __init__(self, engine: RandomNumberGenerator):
        self.engine = engine

    @abstractmethod
    def generate_sample(self):
        pass

    @abstractmethod
    def theoretical_mean(self):
        pass

    @abstractmethod
    def theoretical_variance(self):
        pass


class Bernoulli(BaseDistribution):
    def __init__(self, engine: RandomNumberGenerator, p):
        super().__init__(engine)

        if 0 <= p <= 1:
            self.p = p
        else:
            raise ValueError("The probability must be between 0 and 1.")

    def generate_sample(self):
        u = self.engine.create()

        if u < self.p:
            return 1

        return 0

    def theoretical_mean(self):
        return self.p

    def theoretical_variance(self):
        return self.p * (1 - self.p)
