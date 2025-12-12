'''
Input: 3 * 3 matrix 
Output:

Rules:
Explicit:
- Do not modify the original matrix 

Data Structures
- List 
- range
- len()

Algorithms:
IDEA
- Define a new 3 * 3 list new_list
- Iterate through the inner list to get indexes (i, j)
- Assign lst[j][i] to new-list  

Pseudocode
- new_list = [[], [], []]
- for i in range(len(matrix)):
    - for j in range(len(matrix[0])):
        - new_list[j][i] = matrix[i][j]
- return new_list
'''

def transpose(matrix):
    new_list = [['', '', ''], ['', '', ''], ['', '', '']]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_list[j][i] = matrix[i][j]
    return new_list 

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True