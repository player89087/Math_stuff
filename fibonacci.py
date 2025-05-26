import argparse
import time 
import sys 
import os 
sys.set_int_max_str_digits(10000000) # set the limit higher
start = time.time()
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="fibonacci sequence"
    )
    parser.add_argument("-n", required=True, type=int) # amount of places
   
    args = parser.parse_args()

    numb = args.n
    prev = 1
    prev2 = 0
    new = 0 
for i in range(0,numb):
    new = prev + prev2
    prev2 = prev
    prev = new
    if i % (numb / 100) == 0:
        stat = int(i / numb *100)
        os.system("cls")
        print("Progress: "+ str(stat) + "%   " + "#"*int(stat) )

end = time.time()

dur = end - start

print(f"the number: {new}\n Time needed: {dur} \n Length of the number {len(str(new))}")
with open("fibonacci.txt", "w") as file:
    file.write(f"Number: {new} \n Time needed: {dur}")