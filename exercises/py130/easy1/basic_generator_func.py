def yield_nums():
    num = 1
    while num <= 5:
        yield num 
        num += 1
        
for number in yield_nums():
    print(number)
