void transpose(float num[{}][{}] float fac[{}][{}])
{
 int i, j;
 float b[{}][{}], inverse[{}][{}], d;
 for (i = 0; i<r, i++)
 {
 for(j = 0; j,r;j++)
 {
 b[i][j] = fac[j][i];
 }
 }
d = determinant(num,r);
for (i = 0; i<r; i++)
{
for (j = 0; j<r; j++){
inverse [i][j] = b[i][j] / d;
}
}
printf('


The inverse of the matrix is: 
');
for (i = 0; i<r;i++)
{
for (j=0;j<r;j++){ printf('	%f', inverse[i][j]);}printf('
')}
}
