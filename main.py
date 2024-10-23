import numpy as np

class Analysis_Element:
    def __init__(self, element_number:int) -> None:
        self.element_number = element_number

    def input_data(self) -> None:
        self.area = float(input(f"Enter area for Element {self.element_number} (m^2): "))
        self.length = float(input(f"Enter length for Element {self.element_number} (m): "))
        self.youngs_mod = float(input(f"Enter youngs modulus for Element {self.element_number} (kPa): "))
        self.node_force = float(input(f"Enter the force applied on node {self.element_number+1} (N): "))

    def generate_k(self) -> float:
        a = self.area
        l = self.length
        e = self.youngs_mod
        self.k = (a*e)/l
        return self.k

element_list = []
num_elements = int(input("How many elements?: "))
for i in range(num_elements):
    element = Analysis_Element(i+1)
    element.input_data()
    element_list.append(element)

k_mat = np.zeros((num_elements+1,num_elements+1))
F_vec = []
for i in range(num_elements):
    k_val = element_list[i].generate_k()
    k_mat[i][i] += k_val
    k_mat[i+1][i] = -k_val
    k_mat[i][i+1] = -k_val
    k_mat[i+1][i+1] += k_val
    F_vec.append(element_list[i].node_force)

k_mat = np.delete(k_mat, (0), axis=0)
k_mat = np.delete(k_mat, (0), axis=1)

d = np.matmul(F_vec,np.linalg.inv(k_mat))
print(d)
