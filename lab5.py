import numpy as np

# print(((np.sin(2.4564))**2)+((np.cos(2.4564))**2))
while(1):
    print("1)Matrix Addition 2)Matrix Subtraction 3)Scalar Matrix Multiplication 4)Elementwise Matrix Multiplication")
    print("5)Matrix Multiplication 6)Matrix Transpose 7)Trace of a Matrix 8)Solve System of Linear Equations")
    print("9)Determinant 10)Inverse 11)Singular Value Decomposition 12)Eigen Value 13)Search an Element")
    print("14)Difference of Sum of Upper and Lower Triangular Matrix  15)Exit")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        m = int(input("Enter no. of rows matrices :"))
        n = int(input("Enter no. of columns matrices:"))
        mat1 = np.random.randint(0, 10, (m, n))
        print(mat1)
        mat2 = np.random.randint(0, 10, (m, n))
        print(mat2)
        print(mat1+mat2)
    elif ch == 2:
        m = int(input("Enter no. of rows matrices :"))
        n = int(input("Enter no. of columns matrices:"))
        mat1 = np.random.randint(0, 10, (m, n))
        print(mat1)
        mat2 = np.random.randint(0, 10, (m, n))
        print(mat2)
        print(mat1-mat2)
    elif ch == 3:
        m = int(input("Enter no. of rows matrices :"))
        n = int(input("Enter no. of columns matrices:"))
        mat1 = np.random.randint(0, 10, (m, n))
        print(mat1)
        sc = int(input("Enter number for scalar multiplication : "))
        print(mat1*sc)
    elif ch == 4:
        m = int(input("Enter no. of rows matrices :"))
        n = int(input("Enter no. of columns matrices:"))
        mat1 = np.random.randint(0, 5, (m, n))
        print(mat1)
        mat2 = np.random.randint(0, 5, (m, n))
        print(mat2)
        print(mat1*mat2)
    elif ch == 5:
        m = int(input("Enter no. of rows 1st matrix :"))
        n = int(input("Enter no. of columns 1st matrix:"))
        mat1 = np.random.randint(0, 10, (m, n))
        print(mat1)
        x = int(input("Enter no. of rows 2nd matrix :"))
        y = int(input("Enter no. of columns 2nd matrix:"))
        mat2 = np.random.randint(0, 10, (x, y))
        print(mat2)
        try:
            mat3 = mat1@mat2
            print(mat3)
        except:
            print("Dimensional Mismatch!")
    elif ch == 6:
        m = int(input("Enter no. of rows matrices :"))
        n = int(input("Enter no. of columns matrices:"))
        mat1 = np.random.randint(0, 5, (m, n))
        print("The transpose is : \n", mat1.Transpose())
    elif ch == 7:
        m = int(input("Enter no. of rows matrices :"))
        n = int(input("Enter no. of columns matrices:"))
        mat1 = np.random.randint(0, 5, (m, n))
        print("The Trace of matrix is : \n", mat1.trace())
    elif ch == 8:
        m = int(input("Enter no. of rows matrices :"))
        n = int(input("Enter no. of columns matrices:"))
        mat1 = np.random.randint(0, 10, (m, n))
        print(mat1)
        mat2 = np.random.randint(0, 10, (m, n))
        print(mat2)
        try:
            print(np.linalg.solve(mat1, mat2))
        except:
            print("Not a Square matrix , Solving not possible")
    elif ch == 9:
        m = int(input("Enter no. of rows matrices :"))
        n = int(input("Enter no. of columns matrices:"))
        mat1 = np.random.randint(0, 5, (m, n))
        print("The Determinant is : \n", np.linalg.det(mat1))
    elif ch == 10:
        m = int(input("Enter no. of rows matrices :"))
        n = int(input("Enter no. of columns matrices:"))
        mat1 = np.random.randint(0, 5, (m, n))
        print("The Inverse is : \n", np.linalg.inv(mat1))
    elif ch == 11:
        m = int(input("Enter no. of rows matrices :"))
        n = int(input("Enter no. of columns matrices:"))
        mat1 = np.random.randint(0, 5, (m, n))
        print("The Single value Decomposition is : \n", np.linalg.svd(mat1))
    elif ch == 12:
        m = int(input("Enter no. of rows matrices :"))
        n = int(input("Enter no. of columns matrices:"))
        mat1 = np.random.randint(0, 5, (m, n))
        
        print("The Eigen Values is : \n", np.linalg.eigvals(mat1))

    elif ch == 13:
        m = int(input("Enter no. of rows matrices :"))
        n = int(input("Enter no. of columns matrices:"))
        mat1 = np.random.randint(0, 5, (m, n))
        print(mat1)
        ser = int(input("Enter the search element (between 0 to 5) : "))
        print(np.where(mat1 == ser))
    elif ch == 14:
        x = 1
    elif ch == 15:
        print("Exiting!")
        break
    else:
        print("Ener valid Choice!")


#  m= int(input("Enter no. of rows 1st matrix :"))
#         n= int(input("Enter no. of columns 1st matrix:"))
#         mat1 = np.random.randint(0,10,(m,n))
#         print(mat1)
#         x= int(input("Enter no. of rows 2nd matrix :"))
#         y= int(input("Enter no. of columns 2nd matrix:"))
