from abc import ABC, abstractmethod
from typing import List

from added_mass_calculator.patch_makers.patch import Patch


class IntegralCalculator(object):
    @abstractmethod
    def calculate_h_matrix(self, patches: List[Patch]):
        pass

    @abstractmethod
    def calculate_g_matrix(self, patches: List[Patch]):
        pass