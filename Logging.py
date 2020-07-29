import logging
import EmployeeLogging


logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler=logging.FileHandler('Logging.log')

formater=logging.Formatter('%(asctime)s:%(filename)s:%(name)s:%(message)s')
file_handler.setFormatter(formater)

logger.addHandler(file_handler)

# logging.basicConfig(filename='test.log',level=logging.DEBUG,
# format='%(asctime)s:%(filename)s:%(name)s:%(message)s')

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

result=add(10,20)
logger.debug(result)
result=sub(25,26)
logger.debug(result)
result=mul(2,25)
logger.debug(result)
result=div(16,4)
logger.debug(result)
