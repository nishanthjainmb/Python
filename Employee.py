
class EmployeeLogging:
    raise_amount=1.8
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay

    @property
    def email(self):
        return f'{self.first}.{self.second}@gmail.com'
    
    @property
    def fullname(self):
        return f'{self.first} {self.second}'
    
    def apply_raise(self):
        self.pay=self.pay*raise_amount