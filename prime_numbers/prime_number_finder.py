import sys 
import time 
import argparse

sys.set_int_max_str_digits(1000000000)



parser = argparse.ArgumentParser(
    description="fibonacci sequence"
)
parser.add_argument("-n", required=True, type=int) 
args = parser.parse_args()

amount = args.n


prime_numb = []

for i in range(2,amount):
    is_prime_number = True 
    for x in range(2,amount):
        y = 2
        if i % y == 0:
            is_prime_number = False
            break
        else:
            y += 1
    if is_prime_number == True:
        prime_numb.append(i)
print(prime_numb)