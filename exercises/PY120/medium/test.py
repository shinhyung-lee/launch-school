class Foo:
    def __init__(self, obj):
        self.obj = obj 
        
    def bar(self, qux):
        return self.obj.name() + qux.name()
    
# self.obj and qux are both collaborators of the Foo class's 
# instance objects 

'''
collaboration can take place inside a class's methods by using
instance variables or method arguments as collaborators 
'''