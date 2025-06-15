from decimal import * 
import argparse
import math 

parser = argparse.ArgumentParser(
        description="eulers number"
    )

parser.add_argument("-a", required=True, type=int) 
parser.add_argument("-p",required=True,type=int)

args = parser.parse_args()
getcontext().prec = args.p
amount = args.a


x = 0
for i in range(0,amount):
    x += Decimal(1/math) / Decimal(math.factorial(i))
    #print(x)
    if i % (amount / 100) == 0:
        print(f"Current number: {i}")
        print(f"{x}")


