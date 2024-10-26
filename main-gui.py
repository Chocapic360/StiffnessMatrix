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

        self.young_entry = ct.CTkEntry(self, placeholder_text="Young's Modulus (GPa)")
        self.young_entry.grid(row=3,padx=10,pady=(10,10),sticky="nsw")

    def enter_data(self):
        self.element.set_area(float(self.area_entry.get()))
        self.element.set_length(float(self.length_entry.get()))
        self.element.set_youngs_mod(float(self.young_entry.get()))

class ForceVectorFrame(ct.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.force_vec = np.zeros(3)

        self.label = ct.CTkLabel(self, text="Forces:");
        self.label.grid(row=0,padx=10,pady=(0,0),sticky="nsw")

        self.entry_list = []
        for i in range(num_elements):
            x = ct.CTkEntry(self, placeholder_text=f"Force on node {i+1} (kN)")
            if i == num_elements-1:
                x.grid(row=i+1,padx=10,pady=(10,10))        
            else:
                x.grid(row=i+1,padx=10,pady=(10,0))        
            self.entry_list.append(x)
    
    def enter_data(self):
        self.force_vec = [0]*num_elements
        for i in range(num_elements):
            self.force_vec[i] = float(self.entry_list[i].get())

class OutputFrame(ct.CTkFrame):
    def __init__(self,master):
        super().__init__(master)

        self.label = ct.CTkLabel(self, text="Displacement Output")
        self.label.grid(row=0,columnspan=4,padx=10,pady=(0,0),sticky="nsw")

        self.node_out_array = []
        self.label_array = []
        new_index = 0;
        for i in range(num_elements):
            x = ct.CTkLabel(self, text=f"Node {i+1}: ")
            x.grid(row=1,column=new_index,padx=10,sticky="nsw")
            self.label_array.append(x)

            x = ct.CTkLabel(self, text=0)
            x.grid(row=1,column=new_index+1,padx=10,sticky="nsw")
            self.node_out_array.append(x)
            new_index = new_index+2

    def update_out(self, d_vec:np.ndarray):
        for i in range(num_elements):
            node = self.node_out_array[i]
            displacement = float(d_vec[i])
            node.configure(text=f"{(displacement*1000):.3f}mm")
        
class App(ct.CTk):
    def __init__(self):
        super().__init__()

        self.title("Stiffness Matrix")
        self.num_elements = int(input("How many elements?: "))
        global num_elements #IK it's goofy but it's 1am
        num_elements = self.num_elements
        self.geometry("720x300") # TODO: Change aspect ratio with element # (Make sure it's not too big)
        self._set_appearance_mode("dark");

        self.element_list = []
        for i in range(self.num_elements):
            x = ElementFrame(self,i+1)
            x.grid(row=0,column=i,padx=10,pady=(10,0),sticky="nsw")
            self.element_list.append(x)

        self.force_frame = ForceVectorFrame(self)
        self.force_frame.grid(row=0,column=self.num_elements,padx=10,pady=(10,0),sticky="nsw")

        self.entr_btn = ct.CTkButton(self, text="Enter", command=self.enter_all_data)
        self.entr_btn.grid(row=1,columnspan=self.num_elements,padx=10,pady=(10,10),sticky="ew")

        self.output = OutputFrame(self)
        self.output.grid(row=3,columnspan=self.num_elements,padx=10,pady=(10,10),sticky="ew")

    def calculate(self) -> None:
        f_vec = self.force_frame.force_vec

        self.k_mat = np.zeros((num_elements+1,num_elements+1))
        for i in range(self.num_elements):
            k_val = self.element_list[i].element.generate_k()
            self.k_mat[i][i] += k_val
            self.k_mat[i+1][i] = -k_val
            self.k_mat[i][i+1] = -k_val
            self.k_mat[i+1][i+1] += k_val

        self.k_mat = np.delete(self.k_mat, (0), axis=0)
        self.k_mat = np.delete(self.k_mat, (0), axis=1)

        d = np.matmul(f_vec,np.linalg.inv(self.k_mat))
        self.output.update_out(d)

    def enter_all_data(self) -> None:
        for i in range(num_elements):
            self.element_list[i].enter_data()
        self.force_frame.enter_data()
        self.calculate()

app = App()
app.mainloop()