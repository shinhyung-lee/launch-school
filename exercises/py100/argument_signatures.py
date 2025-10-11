

# str.join() method expects one argument. It needs to be an iterable.
# if the method is called with fewer or more arguments, it will return an error.

words = ('falcons', 'hawks', 'hyundai')
print(",".join(words))

print(",".join()) # method called with 0 argument. Returns TypeError
print(",".join(words, words)) # method called with more than 1 argument. Returns TypeError
