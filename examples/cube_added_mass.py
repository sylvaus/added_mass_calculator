from added_mass_calculator.calculator import AddedMassCalculator
from added_mass_calculator.integral_calculators.triangular_integral_calculator import TriangularIntegralCalculator
from added_mass_calculator.solid_parsers.stl_solid_parser import StlSolidParser

if __name__ == '__main__':
    calculator = AddedMassCalculator(StlSolidParser(), TriangularIntegralCalculator())
    print(calculator.compute_added_mass_coeffs("./objects/cube.stl"))
