from abc import ABC, abstractmethod
from typing import List

import numpy

from added_mass_calculator.solid_parsers.patch import Patch


class IntegralCalculator(ABC):
    @abstractmethod
    def calculate_h_g_matrix(self, patches: List[Patch]) -> (numpy.ndarray, numpy.ndarray):
        pass
