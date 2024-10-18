import customtkinter as ct
import numpy as np
import modules

class ElementFrame(ct.CTkFrame):
    def __init__(self, master, element_number:int):
        super().__init__(master)
        self.element_number = element_number
        self.element = modules.Analysis_Element(element_number)

        self.label = ct.CTkLabel(self, text=f"Element {self.element_number}")
        self.label.grid(row=0,column=0,padx=10,pady=(0,0),sticky="nsw")

        self.area_entry = ct.CTkEntry(self, placeholder_text="Area (m^2)")
        self.area_entry.grid(row=1,padx=10,pady=(10,0),sticky="nsw")

        self.length_entry = ct.CTkEntry(self, placeholder_text="Length (m)")
        self.length_entry.grid(row=2,padx=10,pady=(10,0),sticky="nsw")

        self.young_entry = ct.CTkEntry(self, placeholder_text="Young's Modulus (Pa)")
        self.young_entry.grid(row=3,padx=10,pady=(10,10),sticky="nsw")

    def enter_data(self):
        self.element.set_area(int(self.area_entry.get()))
        self.element.set_length(int(self.length_entry.get()))
        self.element.set_youngs_mod(int(self.young_entry.get()))

class ForceVectorFrame(ct.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.force_vec = np.zeros(3)

        self.label = ct.CTkLabel(self, text="Forces on nodes 2-4");
        self.label.grid(row=0,padx=10,pady=(0,0),sticky="nsw")

        self.f2_entry = ct.CTkEntry(self, placeholder_text="Froce 2 (N)")
        self.f2_entry.grid(row=1,padx=10,pady=(10,0))
        self.f3_entry = ct.CTkEntry(self, placeholder_text="Froce 3 (N)")
        self.f3_entry.grid(row=2,padx=10,pady=(10,0))
        self.f4_entry = ct.CTkEntry(self, placeholder_text="Froce 4 (N)")
        self.f4_entry.grid(row=3,padx=10,pady=(10,10))
    
    def enter_data(self):
        self.force_vec = [int(self.f2_entry.get()),int(self.f3_entry.get()),int(self.f4_entry.get())]

class OutputFrame(ct.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        self.label = ct.CTkLabel(self, text="Displacement Output")
        self.label.grid(row=0,columnspan=4,padx=10,pady=(0,0),sticky="nsw")

        self.n1 = ct.CTkLabel(self, text="Node 1: ")
        self.n1.grid(row=1,column=0,padx=10,pady=(0,0),sticky="nsw")
        self.n1_val_label = ct.CTkLabel(self, text=0)
        self.n1_val_label.grid(row=1,column=1,padx=10,pady=(0,0),sticky="nsw")

        self.n2 = ct.CTkLabel(self, text="Node 2: ")
        self.n2.grid(row=1,column=2,padx=10,pady=(0,0),sticky="nsw")
        self.n2_val_label = ct.CTkLabel(self, text=0)
        self.n2_val_label.grid(row=1,column=3,padx=10,pady=(0,0),sticky="nsw")

        self.n3 = ct.CTkLabel(self, text="Node 3: ")
        self.n3.grid(row=1,column=4,padx=10,pady=(0,0),sticky="nsw")
        self.n3_val_label = ct.CTkLabel(self, text=0)
        self.n3_val_label.grid(row=1,column=5,padx=10,pady=(0,0),sticky="nsw")

        self.n4 = ct.CTkLabel(self, text="Node 4: ")
        self.n4.grid(row=1,column=6,padx=10,pady=(0,0),sticky="nsw")
        self.n4_val_label = ct.CTkLabel(self, text=0)
        self.n4_val_label.grid(row=1,column=7,padx=10,pady=(0,0),sticky="nsw")

    def update_out(self, d_vec:np.ndarray):
        self.n1_val_label.configure(text=f"{d_vec[0]:.3f} m")
        self.n2_val_label.configure(text=f"{d_vec[1]:.3f} m")
        self.n3_val_label.configure(text=f"{d_vec[2]:.3f} m")
        self.n4_val_label.configure(text=f"{d_vec[3]:.3f} m")
        
class App(ct.CTk):
    def __init__(self):
        super().__init__()

        self.title("Stiffness Matrix")
        self.geometry("750x400")
        self._set_appearance_mode("dark");

        self.e1_frame = ElementFrame(self, 1)
        self.e1_frame.grid(row=0,column=0,padx=10,pady=(10,0),sticky="nsw")

        self.e2_frame = ElementFrame(self, 2)
        self.e2_frame.grid(row=0,column=1,padx=10,pady=(10,0),sticky="nsw")

        self.e3_frame = ElementFrame(self, 3)
        self.e3_frame.grid(row=0,column=2,padx=10,pady=(10,0),sticky="nsw")

        self.force_frame = ForceVectorFrame(self)
        self.force_frame.grid(row=0,column=3,padx=10,pady=(10,0),sticky="nsw")

        self.entr_btn = ct.CTkButton(self, text="Enter", command=self.enter_all_data)
        self.entr_btn.grid(row=1,columnspan=4,padx=10,pady=(10,10),sticky="ew")

        self.output = OutputFrame(self)
        self.output.grid(row=3,columnspan=4,padx=10,pady=(10,10),sticky="ew")

    def calculate(self) -> None:
        f_vec = self.force_frame.force_vec
        k1 = self.e1_frame.element.generate_k()
        k2 = self.e2_frame.element.generate_k()
        k3 = self.e3_frame.element.generate_k()

        k_mat = np.array(
            [[k1+k2,-k2,0],
            [-k2,k2+k3,-k3],
            [0,-k3,k3]]
        )

        d = np.matmul(f_vec,np.linalg.inv(k_mat))
        d = np.insert(d,0,0)
        self.output.update_out(d)

    def enter_all_data(self) -> None:
        self.e1_frame.enter_data()
        self.e2_frame.enter_data()
        self.e3_frame.enter_data()
        self.force_frame.enter_data()
        self.calculate()

app = App()
app.mainloop()