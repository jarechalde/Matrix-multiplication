import matplotlib

#Import some of the libraries we are going to need
import matplotlib.pyplot as plt
import numpy as np
import math

#Open the file that contains the data
mydataCE = open("ResultsCE.txt")
mydataV4 = open("ResultsV4.txt")

#Reading the lines in the files
mydataCE = mydataCE.readlines();
mydataV4 = mydataV4.readlines();

n = []
texecce = []
texecv = []
tcompce = []
tcompv = []
tgence = []
tgenv = []

for i in range(1,len(mydataCE)):
 linece = mydataCE[i]
 linev = mydataV4[i]

 datace = linece.split('\t')
 datav = linev.split('\t')

 n.append(int(datace[0]))
 texecce.append(float(datace[1]))
 texecv.append(float(datav[1]))
 tcompce.append(float(datace[2]))
 tcompv.append(float(datav[2]))
 tgence.append(float(datace[3]))
 tgenv.append(float(datav[3]))

#Plots

plt.figure(1)

#First plot
plt.subplot(311)
plt.plot(n, texecce, 'k--', label='Improved version')
plt.plot(n, texecv, 'k', label='Original')

plt.title('Execution time')
plt.ylabel('t')

#Legend
plt.legend(loc='upper center', shadow=True, fontsize='large')

#Second plot
plt.subplot(312)
plt.plot(n, tcompce, 'k--')
plt.plot(n, tcompv, 'k')

plt.title('Compiling time')
plt.ylabel('t')

#Third plot
plt.subplot(313)
plt.plot(n, tgence, 'k--')
plt.plot(n, tgenv, 'k')

plt.title('Code generation time')
plt.ylabel('t')
plt.xlabel('Size of the matrix')

plt.show()
