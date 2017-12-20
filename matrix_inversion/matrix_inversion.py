from math import sqrt
import os
import sys

def fact_history(N): # factorial with history, history excludes 0! because 0! = 1! = 1
    products = [1]
    for i in range(2,N+1):
         products.append(products[-1] * i)
    return products

def fact(N): # excludes 0! because 0! = 1! = 1
    product = 1
    for i in range(2,N+1):
         product *= i
    return product

def find_max_required_dim_size(N):
    required_matrices = 1
    max_required_dim_sz = 0

    # i.e. if N = 7 then required_dim = 6, required_matrices = 6, and max_required_dim_sz = 6*6, and so on...
    for required_dim in range(N-1,0):
        required_matrices *= required_dim
        if required_matrices * required_dim > max_required_dim_sz:
            max_required_dim_sz = required_matrices * required_dim
    return max_required_dim_sz, required_matrices


def make_determinant_func(dim):
    #required_matrices = fact_history(dim)

    #max_required_matrices = fact(dim - 1) # i.e. for dim = 7 1*2*3*4*5*6 theres one for the original then 6 6-dim matrices... and so on
    wM_dim, required_matrices = find_max_required_dim_size(dim)

    print(wM_dim)

    code  = "inline double determinant{}(double M[{}][{}])\n".format(dim,dim,dim)
    code += "{\n"
    code += "int M_dim = {};\n".format(dim)
    code += "int max_wM_dim = M_dim - 1\n;"
    code += "double wMs_old[{}][{}];\n".format(dim-1, wM_dim) # large matrix that can be reused to hold different sized "working matrices"
    code += "double wMs_new[{}][{}];\n".format(dim-1, wM_dim) # rows = max wM_dim, columns = required_matrices * wM_dim
    #We need to double the brackets in case we are going to use format
    code += "double coe_tree[{}] = {{".format(fact(required_matrices-1)) + "1,"*required_matrices + "};\n" # coeficient tree, implemented as array like in class
    code += "int offset, k_offset, wM_dim;\n"
    code += "int n_wM = 1;" # current number of working matrices
    code += "int coe_offset = 0;" # offset into coe_tree
    code += "for (int i = 1; i < dim+1; i++)\n" # n_wM = number of current "working matrices"
    code += "{\n"
    code += "wM_dim = M_dim - n_wM + 1;\n" # dim size of current working matrices
    code += "for (int wM_i = 0; wM_i < n_wM; wM_i++)\n" # wM_i = working matrix index
    code += "{\n"
    code += "offset = wM_i*wM_dim;\n"
    code += "for (int k = offset; k < wM_dim + offset; k++)\n"  # k is column index of selected working matrix
    code += "{\n"
    code += "k_offset = 0;" # can be set to 1 to skip the k column in wM_old when transferred to wM_new
    code += "coe_tree[k + ] *= wMs_old[0][k];\n" # TODO: make this work
    code += "for (int j = 0; j < wM_dim; j++)\n" # j is row index of selected working matrix, starts at 1 because first row is automatically excluded
    code += "{\n"
    code += "if (k == j)\n"
    code += "k_offset = 1;\n"
    code += "wMs_new[j][k] = wMs_old[j+1][k + k_offset];\n"
    code += "}}}\n"
    code += "n_wM *= dim - i;\n" # update n_wM, essentially a factorial
    code += "}\n"

    # for n_matrices in required_matrices:
    #     tmp_dim = dim + 1 - n_matrices # the higher the dimension the less matrices will be needed
    #     code += "double M{}[{}][{}][{}];\n".format(tmp_dim, n_matrices, tmp_dim, tmp_dim)

    return code #Returning the code we built

def make_cofactor_mat():
 
 code = "void cofactor(float num[{}][{}], float f)\n"
 code += "{\n"
 code += " float b[{}][{}], fac [{}][{}]\n"
 code += " int p,q,m,n,i,j;\n" 
 code += " for (q = 0; q<f; q++)\n"
 code += " {\n"
 code += "  for (p = 0; p<f; p++)\n"
 code += "  {\n"
 code += "   m = 0;\n"
 code += "   n = 0;\n"
 code += "   for (i = 0; i < f; i++)\n"
 code += "   {\n"
 code += "    for (j = 0; j<f; j++)\n"
 code += "    {\n"
 code += "     if (i!=q && j!=p)\n"
 code += "     {\n"
 code += "      b[m][n] = num[i][j];\n"
 code += "      if (n<(f-2))\n"
 code += "      {\n"
 code += "       n++;\n"
 code += "      }\n"
 code += "      else\n"
 code += "      {\n"
 code += "       n = 0;\n"
 code += "       m++;\n"
 code += "      }\n"
 code += "     }\n"
 code += "    }\n"
 code += "   }\n"
 code += "   fac[q][p] = pow(-1,q+p)*determinant\n"
 code += "  }\n"
 code += " }\n"
 code += " transpose(num,fac,f)\n"
 code += "}\n"

 return code #We return the code for getting the cofactor matrix

#Creating the code for calculating the transpose matrix
def make_transpose_mat():
 
 code = "void transpose(float num[{}][{}] float fac[{}][{}])\n"
 code += "{\n"
 code += " int i, j;\n"
 code += " float b[{}][{}], inverse[{}][{}], d;\n"
 code += " for (i = 0; i<r, i++)\n"
 code += " {\n"
 code += " for(j = 0; j,r;j++)\n"
 code += " {\n"
 code += " b[i][j] = fac[j][i];\n"
 code += " }\n"
 code += " }\n"
 code += "d = determinant(num,r);\n"
 code += "for (i = 0; i<r; i++)\n"
 code += "{\n"
 code += "for (j = 0; j<r; j++)"
 code += "{\n"
 code += "inverse [i][j] = b[i][j] / d;\n"
 code += "}\n"
 code += "}\n"
 code += "printf('\n\n\nThe inverse of the matrix is: \n');\n"
 code += "for (i = 0; i<r;i++)\n"
 code += "{\n"
 code += "for (j=0;j<r;j++)"
 code += "{"
 code += " printf('\t%f', inverse[i][j]);"
 code += "}"
 code += "printf('\n')"
 code += "}\n"
 code += "}\n"
 
 return code #Returning the code built using this function 

myfile = open("MatInversion.c","w") #Openin file to write our code
code = make_transpose_mat()
myfile.write(code) #Writing code to our file
myfile.close()

#Compiling and running the code
#os.system("gcc -o MatInversion MatInversion.c")
#os.system("./MatInversion")

#Catching the output from running the matrix inversion code
#for line in sys.stdin:
 #print(line)

print(fact(6))
print(36*6)
print(25*6*5)
