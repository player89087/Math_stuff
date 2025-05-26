import sys 
import time 
import argparse

sys.set_int_max_str_digits(1000000000)

start = time.time()
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="fibonacci sequence"
    )
    parser.add_argument("-n", required=True, type=int) 
    args = parser.parse_args()
    
amount = args.n


prime_numb = []
for i in range(2,amount):
    for x in range(2,i-1):
        divi = i / x 
        if i % x  == 0:
            prime_numb.append(i)
            print(f" x {x} i {i } divi {divi}")
            break
        