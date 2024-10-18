import numpy as np

class Analysis_Element:
    def __init__(self, element_number:int) -> None:
        self.element_number = element_number

    def input_data(self) -> None:
        self.area = int(input(f"Enter area for Element_{self.element_number}: "))
        self.length = int(input(f"Enter length for Element_{self.element_number}: "))
        self.youngs_mod = int(input(f"Enter youngs modulus for Element_{self.element_number}: "))

    def generate_k(self) -> float:
        a = self.area
        l = self.length
        e = self.youngs_mod
        self.k = (a*e)/l
        return self.k


element1 = Analysis_Element(1)
element1.input_data()
k1 = element1.generate_k()

element2 = Analysis_Element(2)
element2.input_data()
k2 = element2.generate_k()

element3 = Analysis_Element(3)
element3.input_data()
k3 = element3.generate_k()

k_mat = np.array(
    [[k1+k2,-k2,0],
    [-k2,k2+k3,-k3],
    [0,-k3,k3]]
)

F_vec = np.zeros(3);

for i in range(3):
    F_vec[i] = int(input(f"Input force at node {i+2}: "))

d = np.matmul(F_vec,np.linalg.inv(k_mat))
d = np.insert(d,0,0)
print(d)
