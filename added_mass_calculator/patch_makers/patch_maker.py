from abc import ABC, abstractmethod
from typing import List

from added_mass_calculator.patch_makers.patch import Patch


class ABPatchMaker(ABC):
    @abstractmethod
    def make_patches(self) -> List[Patch]:
        pass
