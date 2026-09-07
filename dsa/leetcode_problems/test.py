
def fn(i):
    if i > 3:
        return 
    
    print(i)
    fn(i + 1)
    print(f'End of call where i = {i}')
    return 

fn(1)