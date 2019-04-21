from typing import List

import numpy
from numpy import inner, sqrt, arctanh, memmap
from numpy.linalg import norm

from added_mass_calculator.integral_calculators.integral_calculator import IntegralCalculator
from added_mass_calculator.solid_parsers.patch import Patch


class TriangularIntegralCalculator(IntegralCalculator):
    def calculate_h_g_matrix(self, patches: List[Patch]) -> (numpy.ndarray, numpy.ndarray):
        n = len(patches)
        h = memmap("h_mat", dtype='float32', mode='w+', shape=(n, n))
        g = memmap("g_mat", dtype='float32', mode='w+', shape=(n, n))
        for i, origin in enumerate(patches):
            for j, patch in enumerate(patches):
                if i == j:
                    h[i, j] = self._compute_singularity_h(origin)
                else:
                    d = patch.center - origin.center
                    d_norm = norm(origin.center - patch.center)
                    h[i, j] = patch.area / d_norm
                    g[i, j] = - patch.area * inner(d, patch.normal) / (d_norm ** 3)

        return h, g

    @staticmethod
    def _compute_singularity_h(origin):
        ab = origin.vertices[1] - origin.vertices[0]
        bc = origin.vertices[2] - origin.vertices[1]
        ca = origin.vertices[0] - origin.vertices[2]

        ah = origin.center - origin.vertices[0]
        bh = origin.center - origin.vertices[1]
        ch = origin.center - origin.vertices[2]

        a_midab = ab * inner(ab, ah) / inner(ab, ab)
        b_midab = a_midab - ab
        b_midbc = bc * inner(bc, bh) / inner(bc, bc)
        c_midbc = b_midbc - bc
        c_midca = ca * inner(ca, ch) / inner(ca, ca)
        a_midca = c_midca - ca

        sin_midabah = norm(a_midab) / norm(ah)
        sin_midcaah = norm(a_midca) / norm(ah)
        sin_midbcbh = norm(b_midbc) / norm(bh)
        sin_midabbh = norm(b_midab) / norm(bh)
        sin_midcach = norm(c_midca) / norm(ch)
        sin_midbcch = norm(c_midbc) / norm(ch)

        h_midab = sqrt(inner(a_midab, a_midab) + inner(ah, ah))
        h_midbc = sqrt(inner(b_midbc, b_midbc) + inner(bh, bh))
        h_midca = sqrt(inner(c_midca, c_midca) + inner(ch, ch))

        return 0.5 * (
                h_midab * (arctanh(sin_midabah) + arctanh(sin_midcaah)) +
                h_midbc * (arctanh(sin_midbcbh) + arctanh(sin_midabbh)) +
                h_midca * (arctanh(sin_midcach) + arctanh(sin_midbcch))
        )


if __name__ == '__main__':
    print(TriangularIntegralCalculator._compute_singularity_h(
        Patch([numpy.array([0.5, 0, 0]), numpy.array([-0.5, 0, 0]), numpy.array([0, 1, 0])],
              numpy.array([0, 0, 1]),
              numpy.array([0, 1 / 3, 0]),
              1))
    )

    print(4 * arctanh(1 / sqrt(2)))
