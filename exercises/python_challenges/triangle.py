class Triangle:
    def __init__(self, s1, s2, s3):
        if not self.all_length_greater_than_zero(s1, s2, s3) or not self.valid_lengths(s1, s2, s3):
            raise ValueError('Invalid lengths for triangles')

        self.s1 = s1 
        self.s2 = s2 
        self.s3 = s3 
    
    @property 
    def kind(self):
        if self.is_equilateral():
            return 'equilateral' 
        elif self.is_isosceles():
            return 'isosceles'
        else:
            return 'scalene'
    
    def all_length_greater_than_zero(self, s1, s2, s3):
        if s1 > 0 and s2 > 0 and s3 > 0:
            return True 
        else:
            return False  
        
    def valid_lengths(self, s1, s2, s3):
        if sum([s1, s2]) > s3 and sum([s2, s3]) > s1 and sum([s1, s3]) > s2:
            return True 
        else:
            return False 
        
    def is_equilateral(self):
        return self.s1 == self.s2 == self.s3 
    
    def is_isosceles(self):
        return (self.s1 == self.s2) or (self.s1 == self.s3) or (self.s2 == self.s3) 
    
    def is_scalene(self):
        return (self.s1 != self.s2) and (self.s1 != self.s3) and (self.s2 != self.s3)