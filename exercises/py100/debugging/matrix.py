sub_list = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
matrix = []

for num in range(3):
    matrix.append(sub_list[num])

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]