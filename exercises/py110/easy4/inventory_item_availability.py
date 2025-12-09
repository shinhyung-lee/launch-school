'''
Input:  An item ID and a list of transactions 
Output: Boolean value indicating whether the item is available (quantity > 0)

Rules
Explicit:
    - quantity needs to be greater than 0 for the item to be available 
Implicit:

Questions

Data Structures
    - dictionary
    - list: list of dictionaries 
Algorithms:
    - ITEMS_WITH_TARGET_ID = all transactions filtered with "TARGET_ID" using transactions_for function
    - QTY = 0
    - For each ITEM in ITEMS_WITH_TARGET_ID, add or subtract to QTY depending on movement property. (in = +, out = -)
    
    Return Value 
    - If QTY > 0, return True. 
    -Otherwise, return False.
'''
# helper function : filters out all transaction with the target_id 
def transactions_for(target_id, transactions):
    return [item for item in transactions if item['id'] == target_id] 

def is_item_available(target_id, transactions):
    items_with_target_id = transactions_for(target_id, transactions)
    quantity = 0
    for item in items_with_target_id:
        if item['movement'] == 'in':
            quantity += item['quantity']
        else: # 'out'
            quantity -= item['quantity']
    return quantity > 0 

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True