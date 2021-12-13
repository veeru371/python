def create_matrix(rows,cols):
    matrix = []
    for r in range(rows):
        row = []
        for c in range(cols):
              v = int(input(f'enter element at row {r},column {c} :'))
              row.append(v)
        matrix.append(row)
    return matrix
def mat_add(first,second):
            matrix = []
            if len(first) == len(second) and len(first[0]) == len (second[0]):
                matrix = [[first[i][j]+second[i][j]] for j in range(len(first[0])) for i in range(len(first))]
                return matrix
def mat_mul(first,second):
    matrix = []
    if len (first[0]) ==len(second):
        matrix = [[sum(a*b for a,b in zip(row,col)) for col in zip(*second)] for row in first]
        return matrix
def disp(matrix):
    for row in matrix:
       for val in row:
         print(f'{val:3d}',end='  ')
print()
rows = int(input("enter number of rows:"))
cols = int(input("enter number of colums:"))
print("\n eneter elememts into matrix1:");
mat1 = create_matrix(rows,cols)
print("\n enter elements into matrix2:");
mat2 = create_matrix(rows,cols)
print('\n---------------mat(1)---------------')
disp(mat1)
print('\n---------------mat(2)---------------')
disp(mat2)
res = mat_add(mat1,mat2)
print('\n-------------ADDITION--------------')
disp(res)
res = mat_mul(mat1,mat2)
print('\n------------MULTIPLICATION--------------')
disp(res)
