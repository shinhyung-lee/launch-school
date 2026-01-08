class Transform:
    
    def __init__(self, data):
        self.data = data 

    def uppercase(self):
        return self.data.upper()
    
    @classmethod
    def lowercase(cls, string):
        return string.lower()

my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz