
# assume input string always has at least two words
# input: string
# output: string 
# string operation, turn it into a list, return second to the last element 
def penultimate(sentence):
    return sentence.split(" ")[-2]

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")