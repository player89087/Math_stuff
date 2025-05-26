import argparse
import time 
import sys 
import os 
from decimal import * 


getcontext().prec = 250 # precision of the golden ratio is specified
start = time.time()
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="fibonacci sequence"
    )
    parser.add_argument("-n", required=True, type=int) 
   
    args = parser.parse_args()

    numb = args.n
    prev = 1
    prev2 = 0
    new = 0 
for i in range(0,numb):
    new = prev + prev2
    if i == numb -1 : 
         golden_ratio = Decimal(new) / Decimal(prev) # relationship between two sections
    prev2 = prev
    prev = new
    if i % (numb / 100) == 0:
        stat = int(i / numb *100)
        os.system("cls")
        print("Progress: "+ str(stat) + "%   " + "#"*int(stat) )

end = time.time()

dur = end - start
size = int(sys.getsizeof(new)) / 1000

print(f"the number: {new}\n Time needed: {dur} \n Length of the number {len(str(new))} \n Golden Ratio: {golden_ratio}") 
with open("fibonacci.txt", "w") as file:
    file.write(f"Number: {new} \n Time needed: {dur} \n Number size: {size} kB \n Golden Ratio: {golden_ratio}")