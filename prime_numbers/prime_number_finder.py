import sys 
import time 
import argparse

sys.set_int_max_str_digits(1000000000)



parser = argparse.ArgumentParser(
    description="primer numbers"
)
parser.add_argument("-n", required=True, type=int) 
args = parser.parse_args()

amount = args.n


prime_numb = []
start = time.time()
for i in range(2,amount):
    is_prime_number = True 
    y = 2
    
    for x in range(2,i):
        if i % y == 0:
            is_prime_number = False
            break
        else:
            y += 1
    
    if is_prime_number == True:
        print(i)
        prime_numb.append(i)    
end = time.time()
dur = end - start
for z in range(0,len(prime_numb)):
    with open("prime_numb.txt", "a") as file: 
        file.write(str(prime_numb[z]) + "\n")
    
print(f"Needed time: {dur} seconds")