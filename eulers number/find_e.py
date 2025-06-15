from decimal import *

import sys 


sys.set_int_max_str_digits(1000000000)


amount = int(input("Amount: "))
for i in range(1,amount):
    getcontext().prec = 10000   
    e = Decimal((1 + 1/i)**i)
    #if i % (amount/100) == 0: 
    print(e)
print(len(str(e)))
    