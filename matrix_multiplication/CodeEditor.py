import re
import numpy as np
import os
import sys
import time

#This script rather than generating code on the fly, it will take a template, and it will introduce the values specific from our problem to the template file to generate an executable code

def matrix_multiplication(A,B,m,n,o,p):
 #If n!=o we cant do the multiplication, so we will exit the function
 if n!=o:
  print("Error, number of columns in the first matrix different from the number of rows in the second matrix")
  return
 

 #In this section we will write the C file We can define a function to write in the file, that may be more 
 #efficient

 time0 = time.time()

 #First we will copy the original template to another file, so we dont loose the original
 os.system("cp Template.c Template2.c")


 #We open the file and allow write and binary mode
 myfile = open("Template2.c","r+b") 

 #We read the content of our template
 myfile_content = myfile.read()

 #Now we will need to replace some parts of the file
 matsizes = r'int m = {}, n = {}, o = {}, p = {};\n'.format(m,n,o,p)
 myfile_content = re.sub(r'//MATRIX SIZES//',matsizes, myfile_content)

 #Now we will introduce the matrix values
 matvalues = ''
 
 #Adding the values of A
 for i in range(0,m):
  for j in range(0,n):
   matvalues += "A [{}][{}] = {},".format(i,j,A[i,j])
 
 #Adding the values of B
 for i in range(0,o):
  for j in range(0,p):
   if i == o-1 and j == p-1:
    matvalues += " B [{}][{}] = {};".format(i,j,B[i,j])
   else:
    matvalues += " B [{}][{}] = {},".format(i,j,B[i,j])
    
 myfile_content = re.sub(r'//MATRIX VALUES//', matvalues, myfile_content)

 #We move the pointer to the top of the file, so we can rewrite the file with the new content generated here
 myfile.seek(0)

 #Code for declaring the size of the matrices should be written like this
 

 #Writing the new content in file
 myfile.write(myfile_content)

 #Closing the file
 myfile.close()

 time1 = time.time()-time0

 timec0 = time.time()
 #Now we compile and run the code
 os.system("tcc -o Temp Template2.c")
 timec1 = time.time()-timec0
 
 tic = time.time()
 os.system("./Temp") 
 toc = time.time()-tic

 #Get rid of the created new template that we won't need anymore
 os.system("rm Template2.c")
 os.system("rm Temp")

 return toc,time1, timec1
 

for i in range(1,10,1):
 #Defining the size of the matrices

 size = 2**i

 #First matrix
 m = size
 n = size
 A = np.random.random((m,n))

 #Second matrix
 o = size
 p = size
 B = np.random.random((o,p))

 #Defining the matrices that we will pass to the main function

 #Calling the function that will edit the code on the template to adapt it to each case
 timeexec,timegen,timecomp = matrix_multiplication(A,B,m,n,o,p)
 
 #Printing size of the matrix, execution time, compiling time, and generating code time
 print("%d\t%f\t%f\t%f" %(size,timeexec,timecomp,timegen))
