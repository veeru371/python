def create_matrix(rows,cols):
    matrix=[]
    for r in range(rows):
        row=[]
        for c in range(cols):
            v=int(input(f'(enter elements at row{r},column{c}:'))
            row.append(v)
        matrix.append(row)
    return matrix
rows=int(input('enter number of rows:'))
cols=int(input('enetr number of cols:'))
print("\n Enter elements into matrix1:");
mat1=create_matrix(rows,cols)
print("\n Enter the elements into matrix2:");
mat2=create_matrix(rows,cols)
def disp(matrix):
    for row in matrix:
        for val in row:
            print(f'{val:3d}',end='')
        print()
print('\n...........MAT(1).........')
disp(mat1)
print('\n.......MAT(2)........')
disp(mat2)
def mat_add(first,second):
    matrix=[]
    if len(first)==len(second)and len(first[0])==len(second[0]):
       matrix=[[first[i][j]+second[i][j] for j in range(len(first[0]))]for i in range(len(first))]
    return matrix
res=mat_add(mat1,mat2)
print('\n.......ADDITION......')
disp(res)
def mat_mul(first,second):
    matrix=[]
    if len(first[0])==len(second):
        matrix=[[sum(a*b for a,b in zip(row,col))for col in zip(*second)]for row in first]
        return matrix
    res=mat_mul(mat1,mat2)
    print('\n.......multiplication..........')
    disp(res)
