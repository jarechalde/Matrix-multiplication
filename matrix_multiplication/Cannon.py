import re
import numpy as np
import os
import sys
import time

#This script rather than generating code on the fly, it will take a template, and it will introduce the values specific from our problem to the template file to generate an executable code

#In the case of the Cannon multiplication we will have to return an error and exit the function if the matrices are not square and both matrices are equal
def matrix_multiplication(A,B,m,n,o,p):

 #If the matrices are square (nxn) and they have the same size we can continue, otherwise we will exit the function
 if m==n and o==p and m==o:
  print("All OK")
 else:
  print("Matrices are not square or have the same size")
  return
 
 #Now we will introduce the matrix values
 matvalues = ''
 
 #Writing the matrices to text files so we can multily them laterusing
 #Cannon's algorithm

 Amat = open("A.txt","w")
 Bmat = open("B.txt","w")

 #Adding the values of A
 Aval = ''
 for i in range(0,m):
  for j in range(0,n):
   if j<n-1:
    Aval += "{} ".format(A[i,j])
   else:
    Aval += "{}\n".format(A[i,j])

 #Writing the B matrix values
 Amat.write(Aval)
 Amat.close()

 #Adding the values of B
 Bval = ''
 for i in range(0,o):
  for j in range(0,p):
   if j<p-1:
    Bval += "{} ".format(B[i,j])
   else:
    Bval += "{}\n".format(B[i,j])

 #Writing the B matrix values
 Bmat.write(Bval) 
 Bmat.close()
    

 #Now we compile and run the code
 os.system("mpicc -o Cannon TemplateCannon.c")

 #Cannon's algorithm needs to use p^2 processes
 os.system("mpiexec -np {} ./Cannon".format(m**2)) 

 #Get rid of old files
 os.system("rm A.txt")
 os.system("rm B.txt")
 os.system("rm Cannon")

#Defining the size of the matrices

#First matrix
m = 8
n = 8
A = np.random.random((m,n))

#Second matrix
o = 8
p = 8
B = np.random.random((o,p))

#Defining the matrices that we will pass to the main function

#Calling the function that will edit the code on the template to adapt it to each case
matrix_multiplication(A,B,m,n,o,p)

