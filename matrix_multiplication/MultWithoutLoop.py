import numpy
import os
import sys

#In this section we will create A (nxn) and B (nx1)
m = 10
n = 10

o = 10
p = 2

#If n!=o we cant do the multiplication, so we will exit the program
if n!=o:
 print("Error, number of columns in the first matrix different from the number of rows in the second matrix")
 sys.exit()

#Creating A (mxn)
A = numpy.random.random((m,n)) 
#print(A)

#Creating B (oxp)
B = numpy.random.random((o,p)) 
#print(B)

#In this section we will write the C file We can define a function to write in the file, that may be more 
#efficient
myfile = open("MatrixMultiplication.c","w")

#First we will include the libraries It will be nice to include comments in the C code too
myfile.write("#include <stdio.h>\n") 
myfile.write("#include <math.h>\n")

#Maybe we can include some functions for this
myfile.write("//Equation") 
myfile.write("\n") 

#Declaring the main function
myfile.write("int main () {\n")

#Declare the matrix in the C program
myfile.write("double C [%i][%i];\n" %(m,n))

#In other version we should declare the array and implement for loops instead

for k in range(0,A.shape[0]):
 for j in range(0,B.shape[1]):
  myfile.write(" C[%i][%i] = " %(k,j))
  for i in range(0,A.shape[1]):
   vble = A[k][j]
   vble2 = B[i][j]
  
   #We will print the number as a float
   myfile.write("%f" %vble)

   if i < A.shape[1]-2:
    myfile.write("*")
    myfile.write("%f" %vble2)
    myfile.write("+")
   else:
    myfile.write(";\n")
 
#Print the results
myfile.write("\n")
myfile.write(" for (int i = 0; i<%i;i++){\n" %m)
myfile.write("  for (int j = 0; j<%i;j++){\n" %p)
#Raw string, so the scape lines dont interfere with Python
myfile.write(r'   printf("%f\t", C[i][j]);')
myfile.write("  }\n")
myfile.write(r'   printf("\n");')
myfile.write(" }\n\n")

#Closing the main function
myfile.write(" return 0;\n")
myfile.write("}")

#Compile button for the Tkinter interface Load file function for Tkinter interface also
myfile.close()

#Compile the file and run it
os.system("gcc -o Matrix MatrixMultiplication.c")
os.system("./Matrix")

#Get rid of old files
os.system("rm MatrixMultiplication.c")
os.system("rm Matrix")
