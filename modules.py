from typing import Any


class Analysis_Element:
    def __init__(self, element_number:int) -> None:
        self.element_number = element_number

    def input_data(self) -> None:
        self.area = int(input(f"Enter area for Element_{self.element_number}: "))
        self.length = int(input(f"Enter length for Element_{self.element_number}: "))
        self.youngs_mod = int(input(f"Enter youngs modulus for Element_{self.element_number}: "))

    def set_area(self, area:int) -> None:
        self.area = area
    def set_length(self, length:int) -> None:
        self.length = length
    def set_youngs_mod(self, youngs_mod:int) -> None:
        self.youngs_mod = youngs_mod

    def generate_k(self) -> float:
        a = self.area
        l = self.length
        e = self.youngs_mod
        self.k = (a*e)/l
        return self.k