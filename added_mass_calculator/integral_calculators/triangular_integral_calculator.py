from typing import List

import numpy

from added_mass_calculator.integral_calculators.integral_calculator import IntegralCalculator
from added_mass_calculator.patch_makers.patch import Patch


class TriangularIntegralCalculator(IntegralCalculator):
    def calculate_h_matrix(self, patches: List[Patch]):
        n = len(patches)
        H = numpy.zeros(n, n)
        for l, origin in enumerate(patches):
            for k, patch in enumerate(patches):
                if l == k:
                    self._compute singularity_h(origin)


    def calculate_g_matrix(self, patches: List[Patch]):
        pass
