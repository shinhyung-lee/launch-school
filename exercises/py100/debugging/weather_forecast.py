# while it's great the weather is always sunny according to the original program,
# this is not what the programmer intended.
# Instead of feeding list of strings 'True' and 'False' as arguments to random.choice,
# we should change the values to True and False (bool)

import random

def predict_weather():
    sunshine = random.choice([True, False])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

predict_weather()