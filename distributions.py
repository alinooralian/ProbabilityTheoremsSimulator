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


class Binomial(BaseDistribution):
    def __init__(self, engine, n, p):
        super().__init__(engine)

        if n >= 0:
            self.n = n
        else:
            raise ValueError("This number must be positive.")

        if 0 <= p <= 1:
            self.p = p
        else:
            raise ValueError("The probability must be between 0 and 1.")

        self.bernoulli = Bernoulli(self.engine, self.p)

    def generate_sample(self):
        cnt = 0

        for _ in range(self.n):
            cnt += self.bernoulli.generate_sample()

        return cnt

    def theoretical_mean(self):
        return self.n * self.p

    def theoretical_variance(self):
        return self.n * self.p * (1 - self.p)


class Geometric(BaseDistribution):
    def __init__(self, engine, p):
        super().__init__(engine)

        if 0 <= p <= 1:
            self.p = p
        else:
            raise ValueError("The probability must be between 0 and 1.")

        self.bernoulli = Bernoulli(self.engine, self.p)

    def generate_sample(self):
        cnt, u = 0, 0

        while u != 1:
            u = self.bernoulli.generate_sample()
            cnt += 1

        return cnt

    def theoretical_mean(self):
        return 1 / self.p

    def theoretical_variance(self):
        return (1 - self.p) / (self.p**2)


class Poisson(BaseDistribution):
    def __init__(self, engine, lam):
        super().__init__(engine)
        
        if lam <= 0:
            raise ValueError("λ must be positive.")
        self.lam = lam

    def generate_sample(self):
        threshold = math.exp(-self.lam)

        cnt = 0
        p = 1.0

        while p > threshold:
            u = self.engine.create()
            p *= u
            cnt += 1

        return cnt - 1

    def theoretical_mean(self):
        return self.lam

    def theoretical_variance(self):
        return self.lam


class Exponential(BaseDistribution):
    def __init__(self, engine, lam):
        super().__init__(engine)

        if lam <= 0:
            raise ValueError("λ must be positive.")
        self.lam = lam

    def generate_sample(self):
        u = self.engine.create()
        return -math.log(u) / self.lam

    def theoretical_mean(self):
        return 1 / self.lam

    def theoretical_variance(self):
        return 1 / (self.lam**2)

