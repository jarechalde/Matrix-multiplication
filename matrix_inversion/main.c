#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int M_dim = 5;

double determinant(double M[M_dim][M_dim])
{

}

int main()
{
    double M[M_dim][M_dim];
    memset(M,0,sizeof(double)*M_dim*M_dim);
    M[4][4] = 4;
    double* p_M = &M[0];

    printf("%d\n",((double[M_dim][M_dim])p_M)[4][4]);
    return 0;
}
