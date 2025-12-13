'''
Input: a matrix
Ouput: 90-degree clockwise rotated matrix 

Rules
Explicit:
- should not mutate the original matrix 

Data Structures:
- List 

Algorithms: 
IDEA
- 

Pseudocode:
- 

2 * 3 becomes 3 * 2
1 * 4 becomes 4 * 1
row_num 
[[3, 4, 1]
 [9, 7, 5]]
[[9, 3]
 [7, 4]
 [5, 1]]  
0, 0 > 0, 1
0, 1 > 1, 1
0, 2 > 2, 1
1, 0 > 0, 0 
1, 1 > 1, 0
1, 2 > 2, 0
'''

def rotate90(matrix):
    transposed = []
    num_rows = len(matrix)
    
    for _ in range(len(matrix[0])):
        transposed.append([])
    
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[0])):
            transposed[col_idx].append(matrix[row_idx][col_idx])
    
    return [row[::-1] for row in transposed]

matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)