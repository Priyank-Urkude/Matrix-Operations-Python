class Matrix:
    def __init__(self, rows, columns, data):
        if rows <= 0 or columns <= 0:
            raise ValueError("Rows and columns must be positive")
        
        if len(data) != rows:
            raise ValueError("Incorrect number of rows")

        for row in data:
            if len(row) != columns:
                raise ValueError("Incorrect number of columns")
        
        self.rows = rows
        self.columns = columns
        self.data = data

    def add(self, other):

        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrices must have the same dimensions")

        else:
            matrix_sum = []
            for row in range(self.rows):
                matrix_row = []
            
                for column in range(self.columns):
                    value = self.data[row][column] + other.data[row][column]
                    matrix_row.append(value)
                
                matrix_sum.append(matrix_row)

            return Matrix(self.rows, self.columns, matrix_sum)

    def subtract(self, other):

        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrices must have the same dimensions")

        else:
            matrix_diff = []
            for row in range(self.rows):
                matrix_row = []
            
                for column in range(self.columns):
                    value = self.data[row][column] - other.data[row][column]
                    matrix_row.append(value)
                
                matrix_diff.append(matrix_row)

            return Matrix(self.rows, self.columns, matrix_diff)

    def scalar_multiply(self, number):

        multiplied_matrix = []

        for row in range(self.rows):
            matrix_row = []

            for column in range(self.columns):
                value = self.data[row][column] * number

                matrix_row.append(value)
                
            multiplied_matrix.append(matrix_row)

        return Matrix(self.rows, self.columns, multiplied_matrix)

    def multiply(self, other):

        if self.columns != other.rows:
            raise ValueError("first matrix's columns are not equal to second matrix's rows, Multiplication not possible")

        else:
            product_matrix = []
            for row in range(self.rows):
                matrix_row = []

                for column in range(other.columns):
                    value = 0
                
                    for other_row in range(other.rows):

                        value += self.data[row][other_row] * other.data[other_row][column]

                    matrix_row.append(value)

                product_matrix.append(matrix_row)

            return Matrix(self.rows, other.columns, product_matrix)

    def transpose(self):

        matrix_transpose = []

        for row in range(self.columns):
            matrix_row = []

            for column in range(self.rows):
                matrix_row.append(self.data[column][row])

            matrix_transpose.append(matrix_row)

        return Matrix(self.columns, self.rows, matrix_transpose)

    def equality(self, other):

        if self.rows != other.rows or self.columns != other.columns:
            return False

        else:

            for row in range(self.rows):

                for column in range(self.columns):

                    if self.data[row][column] != other.data[row][column]:

                        return False

            return True

    def determinant(self):

        if self.rows != self.columns:
            raise ValueError("requires a square matrix")

        elif self.rows == 2:
            determinant = (self.data[0][0] * self.data[1][1]) - (self.data[0][1] * self.data[1][0])
            return(determinant)

        elif self.rows == 3:
            determinant = (self.data[0][0] * (self.data[1][1] * self.data[2][2] - self.data[2][1] * self.data[1][2]) -
            self.data[0][1] * (self.data[1][0] * self.data[2][2] - self.data[2][0] * self.data[1][2]) +
            self.data[0][2] * (self.data[1][0] * self.data[2][1] - self.data[2][0] * self.data[1][1]))
            return(determinant)
        else:
            raise NotImplementedError("determinant is supported only for 2x2 and 3x3 matrix")

    def inverse(self):

        if self.rows != 2 or self.columns != 2:
            raise ValueError("Enter only 2x2 matrix")

        else:
            a = self.data[0][0]
            b = self.data[0][1]
            c = self.data[1][0]
            d = self.data[1][1]

            determinant = (a * d) - (b * c)

            if determinant == 0:
                print("matrix is singular, inverse not possible")
                return None

            else:
                adjoint = [[d,-b],[-c,a]]

                matrix_inverse = []
                for row in range(self.rows):
                    matrix_row = []
                    
                    for column in range(self.columns):
                        value = adjoint[row][column] / determinant
                        matrix_row.append(value)
                        
                    matrix_inverse.append(matrix_row)

                return Matrix(self.rows, self.columns, matrix_inverse)

                                           
matrices = {}

# Main Menu:

while True:
    print("\n==== Matrix Operations ====")
    print("1. Create New Matrix")
    print("2. View Existing Matrices")
    print("3. Matrix Addition")
    print("4. Matrix Subtraction")
    print("5. Matrix Scalar Multiplication")
    print("6. Matrix Multiplication")
    print("7. Matrix Transpose")
    print("8. Matrix Equality")
    print("9. Determinant of Matrix (2x2) and (3x3)")
    print("10. Inverse of matrix (2x2)")
    print("11. Exit")

    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("Enter valid number")
        continue

    #Option 1: Creating a matrix
    
    if choice == 1:
        try:
            name = input("\nEnter matrix name : ")
            rows = int(input("Enter number of rows: "))
            columns = int(input("Enter number of columns: "))
        except ValueError:
            print("Please Enter valid input")
            continue

        matrix = []

        loop_rows = 1

        while loop_rows < (rows + 1):
            matrix_row = list(map(int,input(f"enter row {loop_rows}: ").split()))
            if len(matrix_row) == columns:
                matrix.append(matrix_row)
                loop_rows += 1
            else:
                print(f"Enter {columns} elements")

        object_matrix = Matrix(rows,columns,matrix)

        matrices[name] = object_matrix

    #Option 2: View Existing Matrices
    elif choice == 2:
        for name,matrix in matrices.items():
            print(f"\nMatrix: {name}")
            for row in matrix.data:
                print(row)

    #Option 3: Matrix Addition
    elif choice == 3:
        matrix_1 = input("Enter first matrix name: ")
        matrix_2 = input("Enter second matrix name: ")

        if matrix_1 not in matrices or matrix_2 not in matrices:
            print("One or both matrices do not exist.")
        else:
            result = matrices[matrix_1].add(matrices[matrix_2])

            for row in result.data:
                print(row)

            response = input("Do you wish to save this matrix? (yes/no)").lower()

            if response == "yes":
                name = input("enter matrix name: ")
                matrices[name] = result

    #Option 4: Matrix Subtraction
    elif choice == 4:
        matrix_1 = input("Enter first matrix name: ")
        matrix_2 = input("Enter second matrix name: ")

        if matrix_1 not in matrices or matrix_2 not in matrices:
            print("One or both matrices do not exist.")
        else:
            result = matrices[matrix_1].subtract(matrices[matrix_2])

            for row in result.data:
                print(row)

            response = input("Do you wish to save this matrix? (yes/no)").lower()
            
            if response == "yes":
                name = input("enter matrix name: ")
                matrices[name] = result

    #Option 5: Matrix Scalar Multiplication
    elif choice == 5:
        matrix = input("enter matrix name: ")
        number = int(input("enter number to multiply with: "))

        if matrix not in matrices:
            print("matrix does not exist")
        else:
            result = matrices[matrix].scalar_multiply(number)

            for row in result.data:
                print(row)

            response = input("Do you wish to save this matrix? (yes/no) ").lower()
            
            if response == "yes":
                name = input("enter matrix name: ")
                matrices[name] = result
            
    #Option 6: Matrix Multiplication
    elif choice == 6:
        matrix_1 = input("Enter first matrix name: ")
        matrix_2 = input("Enter second matrix name: ")

        if matrix_1 not in matrices or matrix_2 not in matrices:
            print("One or both matrices do not exist.")

        else:
            result = matrices[matrix_1].multiply(matrices[matrix_2])

            for row in result.data:
                print(row)

            response = input("Do you wish to save this matrix? (yes/no) ").lower()
            
            if response == "yes":
                name = input("enter matrix name: ")
                matrices[name] = result

    #Option 7: Transpose
    elif choice == 7:
        matrix = input("Enter matrix name: ")

        if matrix not in matrices:
            print("Matrix does not exist")
        else:
            result = matrices[matrix].transpose()

            for row in result.data:
                print(row)

            response = input("Do you wish to save this matrix? (yes/no) ").lower()
            
            if response == "yes":
                name = input("enter matrix name: ")
                matrices[name] = result

    #Option 8: Equality
    elif choice == 8:
        matrix_1 = input("Enter first matrix name: ")
        matrix_2 = input("Enter second matrix name: ")

        if matrix_1 not in matrices or matrix_2 not in matrices:
            print("One or both matrices do not exist.")

        else:
            print(matrices[matrix_1].equality(matrices[matrix_2]))

    #Option 9: Determinant of a matrix
    elif choice == 9:
        matrix = input("enter matrix name: ")

        if matrix not in matrices:
            print("matrix does not exist")

        else:
            print(matrices[matrix].determinant())

    #Option 10: Inverse of 2x2 matrix
    elif choice == 10:
        matrix = input("enter matrix name: ")

        if matrix not in matrices:
            print("matrix does not exist")

        else:
            result = matrices[matrix].inverse()

            if result is None:
                continue

            for row in result.data:
                print(row)

            response = input("Do you wish to save this matrix? (yes/no) ").lower()
            
            if response == "yes":
                name = input("enter matrix name: ")
                matrices[name] = result
        
    
    #Option 11: Exit Programm
    elif choice == 11:
        print("\nExited the program")
        break

    else:
        print("Invalid choice, please select 1-11")




