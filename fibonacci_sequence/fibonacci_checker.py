import argparse
import decimal
import sys 
import os 




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
x = 1
for i in range(0,numb):
    x += 1
    new = prev + prev2
    if new == numb :
        print(f"Is a fibonacci number, place {i + 1 }") # did not start at zero so 
        break
    prev2 = prev
    prev = new
    if x % (x / 100) == 0: # auto get int as result
        stat = (x // i *100)
        os.system("cls")
        print("Progress: "+ str(stat) + "%   " + "#"*int(stat) )

