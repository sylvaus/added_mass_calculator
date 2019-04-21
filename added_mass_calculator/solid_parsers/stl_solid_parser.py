import stl
from numpy.linalg import norm

from added_mass_calculator.solid_parsers.patch import Patch
from added_mass_calculator.solid_parsers.solid_parser import ABSolidParser


class StlSolidParser(ABSolidParser):
    def compute_volume(self, filepath: str) -> float:
        mesh = stl.mesh.Mesh.from_file(filepath)
        return mesh.get_mass_properties()[0]

    def make_patches(self, filepath: str):
        mesh = stl.mesh.Mesh.from_file(filepath)
        return [
            Patch([mesh.v0[i], mesh.v1[i], mesh.v2[i]], mesh.normals[i] / norm(mesh.normals[i]),
                  (mesh.v0[i] + mesh.v1[i] + mesh.v2[i]) / 3.0, mesh.areas[i][0])
            for i in range(mesh.areas.size)
        ]

