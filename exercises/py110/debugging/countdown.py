'''
counts down from 10 to 1
range(10) counts number from 0(inclusive) to 10 (exclusive)
we have to add stop and step index of the range.
range(10, 0, -1) will do the job
We also have to update the value of counter
Right now we are decreasing the counter but it is not getting saved anywhere.
'''

def decrease(counter):
    return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    counter = decrease(counter)

print('LAUNCH!')