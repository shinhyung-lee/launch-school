'''
=== Problem ===
In: List of dictionaries
Out: a list of string
    - summarizes input info
    
=== EXAMPLES ===

=== DATA STRUCTURES ===
- dict 
- list 
    - average of scores 
    
- string 
    - 

=== ALGO ===
- Iterate through each `student` in `students`
- Keep `name` and `average` 
    - `average` HELPER function
    
    
calculate_average (HELPER)
In: List of numbers (scores)
Out: Average score in decimal (one decimal place)

=== BRAINSTORM ===
- list of dict 
- list of dict
    - name, average
- sort them by Average
- create a list with strings
    - ranked by average scores 
    - 'Rank 1: Alice (Average: 91.7)'
'''
def calculate_average(scores):
    sum = 0
    for score in scores:
        sum += score 
    return round(sum / len(scores), 1)

# print(calculate_average([92, 88, 98]))

def create_leaderboard(students):
    students_info = []
    for student in students:
        info = {}
        info['name'] = student['name']
        info['Average'] = calculate_average(student['scores'])
        students_info.append(info)
    
    students_info.sort(key=lambda info: info['Average'], reverse=True)
    result = []
    currRank = 1
    
    for student in students_info:
        result.append(f'Rank {currRank}: {student['name']} (Average: {student['Average']})')
        currRank += 1 
    
    return result
        
        
students = [
    {
        'name': 'Bob',
        'id': 's2',
        'scores': [85, 90, 88]
    }, # Avg: 87.7
    {
        'name': 'Charlie',
        'id': 's3',
        'scores': [92, 88, 95]
    }, # Avg: 91.7
    {
        'name': 'Alice',
        'id': 's1',
        'scores': [92, 88, 98]
    }, # Avg: 92.7
    {
        'name': 'David',
        'id': 's4',
        'scores': [80, 78]
    }, # Avg: 79.0
]

# Expected output:
# [
#  'Rank 1: Charlie (Average: 92.7)',
#  'Rank 2: Alice (Average: 91.7)',
#  'Rank 3: Bob (Average: 87.7)',
#  'Rank 4: David (Average: 79.0)'
# ]

print(create_leaderboard(students))