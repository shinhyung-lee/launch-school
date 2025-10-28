

def every_other(nums: list) -> list: 
    return [num for idx, num in enumerate(nums) if idx%2 == 0]

print(every_other([1,4,7,2,5]))


def third_occurrence(sentence, target):
    count = 0 
    for index, char in enumerate(sentence): 
        if char == target and count == 2:
            return index 
        elif char == target:
            count+=1 
    return None 

print(third_occurrence('aaaxbxcdxexaa', 'a'))

            
    