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

