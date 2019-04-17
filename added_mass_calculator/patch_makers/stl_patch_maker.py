from added_mass_calculator.patch_makers.patch import Patch
from added_mass_calculator.patch_makers.patch_maker import ABPatchMaker
import stl


class StlPatchMaker(ABPatchMaker):
    def __init__(self, filepath: str):
        self._filepath = filepath

    def make_patches(self):
        mesh = stl.mesh.Mesh.from_file(self._filepath)
        return [
            Patch([mesh.v0[i], mesh.v1[i], mesh.v2[i]], mesh.normals[i],
                  (mesh.v0[i] + mesh.v1[i] + mesh.v2[i])/3.0, mesh.areas[i][0])
            for i in range(mesh.areas.size)
        ]


if __name__ == '__main__':
    maker = StlPatchMaker("300_polygon_sphere_100mm.STL")
    patches = maker.make_patches()
    pass

