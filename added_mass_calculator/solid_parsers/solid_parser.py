from abc import ABC, abstractmethod
from typing import List

from added_mass_calculator.solid_parsers.patch import Patch


class ABSolidParser(ABC):
    @abstractmethod
    def compute_volume(self, filepath: str) -> float:
        pass

    @abstractmethod
    def make_patches(self, filepath: str) -> List[Patch]:
        pass
