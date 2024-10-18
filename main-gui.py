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
        self.area_entry.grid(row=1,column=0,padx=10,pady=(10,0),sticky="nsw")

        self.length_entry = ct.CTkEntry(self, placeholder_text="Length (m)")
        self.length_entry.grid(row=2,column=0,padx=10,pady=(10,0),sticky="nsw")

        self.young_entry = ct.CTkEntry(self, placeholder_text="Young's Modulus (Pa)")
        self.young_entry.grid(row=3,column=0,padx=10,pady=(10,10),sticky="nsw")

    def enter_data(self):
        self.element.set_area(self.area_entry.get())
        self.element.set_length(self.length_entry.get())
        self.element.set_youngs_mod(self.young_entry.get())

class App(ct.CTk):
    def __init__(self):
        super().__init__()

        self.title("Stiffness Matrix")
        self.geometry("600x400")
        self._set_appearance_mode("dark");

        self.e1_frame = ElementFrame(self, 1)
        self.e1_frame.grid(row=0,column=0,padx=10,pady=(10,0),sticky="nsw")

        self.e2_frame = ElementFrame(self, 2)
        self.e2_frame.grid(row=0,column=1,padx=10,pady=(10,0),sticky="nsw")

        self.e3_frame = ElementFrame(self, 3)
        self.e3_frame.grid(row=0,column=2,padx=10,pady=(10,0),sticky="nsw")

        self.entr_btn = ct.CTkButton(self, text="Enter", command=self.enter_all_data)
        self.entr_btn.grid(row=1,columnspan=3,padx=10,pady=(10,10),sticky="ew")

    def enter_all_data(self) -> None:
        self.e1_frame.enter_data()
        self.e2_frame.enter_data()
        self.e3_frame.enter_data()

app = App()
app.mainloop()