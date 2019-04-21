from numpy import zeros, pi, ndarray
from scipy.linalg import solve

from added_mass_calculator.integral_calculators.integral_calculator import IntegralCalculator
from added_mass_calculator.solid_parsers.solid_parser import ABSolidParser


class AddedMassCalculator(object):
    def __init__(self, solid_parser: ABSolidParser, integral_maker: IntegralCalculator):
        self._solid_parser = solid_parser
        self._integral_maker = integral_maker

    def compute_added_mass_coeffs(self, filepath: str) -> ndarray:
        patches = self._solid_parser.make_patches(filepath)
        n = len(patches)
        dphis = [zeros((n,)), zeros((n,)), zeros((n,))]
        for k, patch in enumerate(patches):
            dphis[0][k] = patch.normal[0]
            dphis[1][k] = patch.normal[1]
            dphis[2][k] = patch.normal[2]

        h, g = self._integral_maker.calculate_h_g_matrix(patches)
        for i in range(n):
            g[i, i] -= 2 * pi
        phis = []
        for dphi in dphis:
            phis.append(
                solve(g, h.dot(dphi), overwrite_a=True, overwrite_b=True)
            )

        volume = self._solid_parser.compute_volume(filepath)
        coefficients = zeros((3, 3))
        for i in range(3):
            for j in range(3):
                result = 0
                for k, patch in enumerate(patches):
                    result -= phis[i][k] * dphis[j][k] * patch.area

                coefficients[i, j] = result / volume

        return coefficients
