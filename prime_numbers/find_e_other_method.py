from decimal import * 
import argparse


parser = argparse.ArgumentParser(
        description="euleric number"
    )

parser.add_argument("-a", required=True, type=int) 
parser.add_argument("-p",required=True,type=int)

args = parser.parse_args()
getcontext().prec = args.p
amount = args.a
def factorial (x):
    output = 1
    for i in range(1, x+1):
        output = output*i
    return output

def finding_e(x):
    e = 1
    y = 0
    precion = 0
    for i in range(1, x+1):
        e_before = e
        e = Decimal(e) + Decimal(1/factorial(i))
        print(e)
finding_e(amount)