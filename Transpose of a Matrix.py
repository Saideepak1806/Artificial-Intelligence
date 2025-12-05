rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
print("Enter matrix elements:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row)

transpose = []
for i in range(cols):
    t_row = []
    for j in range(rows):
        t_row.append(matrix[j][i])
    transpose.append(t_row)

print("Original Matrix:")
for r in matrix:
    print(r)

print("Transposed Matrix:")
for r in transpose:
    print(r)
