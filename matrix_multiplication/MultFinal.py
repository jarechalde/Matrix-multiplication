import numpy as np
import os
import sys
import time

#Defining the function for the matrix code implementation

def matrix_multiplication(A,B,m,n,o,p,optflag,parflag):
 #If n!=o we cant do the multiplication, so we will exit the function
 if n!=o:
  print("Error, number of columns in the first matrix different from the number of rows in the second matrix")
  return
 
 #If the file already exists we delete it
 try:
  os.remove("MatrixMultiplication.c")
 except OSError:
  pass

 tgen0 = time.time()

 #In this section we will write the C file We can define a function to write in the file, that may be more 
 #efficient
 myfile = open("MatrixMultiplication.c","w")

 #First we will include the libraries
 code = "#include <stdio.h>\n"
 code += "#include <math.h>\n"
 
 if parflag == 1:
  code += "#include <omp.h>\n" 
 code += "int main () {\n" #Declaring the main function
 code += " double A [{}][{}];\n".format(m,n) #Declaring A matrix
 code += " double B [{}][{}];\n".format(o,p)
 code += " double C [{}][{}];\n\n".format(m,p) #Declare the matrix in the C program

 #Declaring the matrices values

 for i in range(0,m):
  for j in range(0,n):
   code += " A [{}][{}] = {};\n".format(i,j,A[i,j])

 for i in range(0,o):
  for j in range(0,p):
   code += " B [{}][{}] = {};\n".format(i,j,B[i,j])

#Implementing the for loop 
 
 code += "double sum = 0;\n"

 if parflag == 1:
  code += "for(int i = 0; i < {}; i++)\n".format(m)
  code += "{\n"
  code += " for(int j = 0; j < (); j++)\n".format(p)
  code += " {\n"
  code += "  for(int k = 0; k < {}; k++)\n".format(o)
  code += "   sum = sum + A[i][k]*B[k][j];\n"
  code += " sum = 0;\n" #Resetting the sum value
  code += " C[i][j] = sum;\n"

 else: 
  code += "for(int i = 0; i < {}; i++)\n".format(m)
  code += "{\n"
  code += " for(int j = 0; j < {}; j++)\n".format(p)
  code += " {\n"
  code += "  for(int k = 0; k < {}; k++)\n".format(o)
  code += "  {\n"
  code += "   sum = sum + A[i][k]*B[k][j];\n"
  code += "  }\n"
  code += " C[i][j] = sum;\n"
  code += " }\n"
  code += "}\n"

 #We will skip printing the results to see how it affects our performance
 
 #code += "\n" #In this next lines of code, we tell the C program to print the results
 #code += " for (int i = 0; i<{};i++)".format(m)
 #code += "{\n"
 #code += "  for (int j = 0; j<{};j++)".format(p)
 #code += "{\n"
 #code += r'   printf("C[%d][%d] = ",i,j);'#Raw string, so the scape lines dont interfere with Python
 #code += r'   printf("%f ", C[i][j]);'
 #code += "  }\n"
 #code += r'   printf("\n");'
 #code += " }\n\n"

 
 code += " return 0;\n" #Closing the main function
 code += "}"

 #Writing the code to the file and closing the file
 myfile.write(code)
 myfile.close()

 tgen = time.time()-tgen0

 #Compile the file and run it
 topt0 = time.time()
 os.system("tcc -O{} -o Matrix MatrixMultiplication.c".format(optflag))
 tcomp = time.time()-topt0
 
 #It maybe better to save the results in CSV format
 #Lets time how long does it take for our program to run only
 trun0 = time.time()
 os.system("./Matrix")
 texec = time.time()-trun0

 #Removing old files
 os.system("rm Matrix")
 os.system("rm MatrixMultiplication.c")
 
 return(texec,tcomp,tgen)

#Calling the function and sending the arguments

#What happens if instead of accesing a numpy matrix we are accessing a bidimensional list on python
#Try this because it makes more sense, as we are trying to replace numpy

#Lets compare the different methods: Python, Numpy, and ours

for i in range(1,10,1):

 x = 2**i

 A = np.random.random((x,x))
 B = np.random.random((x,x))

 m = A.shape[0]
 n = A.shape[1]
 
 o = B.shape[0]
 p = B.shape[1]

 t = time.time()
 texec,tcomp,tgen = matrix_multiplication(A,B,m,n,o,p,0,0)
 to0 = time.time()-t

 #Printing matrix size, execution time, compiling time and generating code time
 print("%d\t%f\t%f\t%f\t" %(x,texec,tcomp,tgen))

 #Numpy??
