# Global Stiffness Matrix Calculator for 1D Axially Loaded Component

## Overview

This Python project is designed to calculate the **global stiffness matrix** for a **1D axially loaded component**. The calculation is based on user input regarding material properties and forces applied. The project is structured to interactively guide users through the input of necessary parameters and provide the resulting global stiffness matrix, node displacements, and reaction forces at the anchored end.

This project is modeled after Example 4.1 in the reference textbook, and follows the classic Finite Element Analysis (FEA) approach for structural analysis.

## Features

- **Interactive Input**: The software will prompt the user to input the number of elements, material properties, and dimensions for each element.
- **Axial Force Input**: Users will be able to input applied forces at each node.
- **Global Stiffness Matrix Calculation**: Based on the input parameters, the software will compute the global stiffness matrix for the system.
- **Displacement and Reaction Force Calculation**: Using the global stiffness matrix, the software will solve for the displacement of each node and compute the reaction force at the fixed end.

## Functionality

1. **Number of Elements**: The user inputs the number of elements making up the component.
2. **Element Properties**: For each element, the user is prompted to input the:
   - Young’s modulus (E)
   - Cross-sectional area (A)
   - Length of the element (L)
3. **Force Input**: The user enters the forces applied at each node.
4. **Global Stiffness Matrix Generation**: The software will calculate the global stiffness matrix based on the input data.
5. **Displacement Calculation**: The software will solve for the displacements of each node using the stiffness matrix and the applied forces.

## Usage

1. **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
## For the GUI
3. **Run the script**:
    ```bash
    python main-gui.py
    ```
4. **A prompt will show up in the terminal asking how many elements make up the Axially Loaded Component**
     - After entering a value a window will pop-up.
   
   ![Screenshot 2024-10-26 024212](https://github.com/user-attachments/assets/8dd588a4-20b4-4e85-9407-56ec3c406360)

5. **Fill in your values and press the blue enter button to get your displacements.**

## For the CLI
3. **Run the script**:
    ```bash
    python main.py
    ```
4. **Follow the instructions on the terminal**

   ![Screenshot 2024-10-27 162707](https://github.com/user-attachments/assets/406ba0bf-4703-453a-b1ff-9fe13cf8186b)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or further details, feel free to contact the repository maintainer at valentin.thevoz@tcu.edu.

This readme was partially generated by OpenAI.
