
# we can only concatenate str to str 
# in len(tweet + 5), tweet is a str and 5 is an int.
# str and int cannot be concatenated together
# We can rewrite the last line as length_of_tweet = len(tweet) + 5

tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

try:
    length_of_tweet = len(tweet + 5)
    print(length_of_tweet)
except TypeError as e: 
    print(e)
