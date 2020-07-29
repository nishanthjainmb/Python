import logging

logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler=logging.FileHandler('Employee.log')

formater=logging.Formatter('%(asctime)s:%(filename)s:%(name)s:%(message)s')
file_handler.setFormatter(formater)

logger.addHandler(file_handler)
logging.basicConfig(filename='Employee.log',level=logging.INFO,format='%(asctime)s:%(filename)s:%(name)s:%(message)s')

class EmployeeLogging:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        logger.info(f'Employee class created for {self.first}!!!')

    @property
    def email(self):
        return f'{self.first}.{self.second}@gmail.com'

emp1=EmployeeLogging('Nishanth','M P',150000)
