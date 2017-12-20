#include <stdio.h>
#include <math.h>

//Main function

int main(){


 //MATRIX SIZES//

 double A [m][n];
 double B [o][p];
 double C [m][p];

 //MATRIX VALUES//

 //Start the sum value
 double sum = 0;

 for (int i = 0; i<m; i++){
  for (int j = 0; j<p; j++){
   for (int k = 0; k<o; k++){
    sum = sum + A[i][k]*B[k][j];
   }
  C[i][j] = sum;
  //Resetting the sum value
  sum = 0;
  }
 }

 //Printing the results to screen
 //for (int i = 0; i<m; i++){
  //for (int j = 0; j<p; j++){
   //printf("C[%d][%d] = ",i,j);
   //printf("%f\t",C[i][j]);
  //}
  //printf("\n");
 //}

 return 0;

}
