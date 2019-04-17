from typing import List

from numpy import ndarray


class Patch(object):
    __slots__ = ["vertices", "normal", "area", "center"]

    def __init__(self, vertices: List[ndarray], normal: ndarray, center: ndarray, area: float):
        self.vertices = vertices
        self.normal = normal
        self.center = center
        self.area = area
