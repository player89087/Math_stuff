import hashlib
import random 
import math 
import time 
import numpy as np 

file_path = "/home/siredgar20/Schreibtisch/coding_challenge/challenge/level0/start.html" # insert here 
hash_func = hashlib.new("sha-256")
    
with open(file_path, 'rb') as file:
    # 8192 bits since its most efficient that way 
    while chunk := file.read(8192):
        hash_func.update(chunk)
    



hash_bytes = hash_func.digest()      # to gain real bytes
hash_int = int.from_bytes(hash_bytes, "big") # first  bit is highest byte




# calculate rsa key pair 





e = int(input("Please type in the value of e:"))
n = int(input("Please type in the value of n:"))
 # thats important 



signature = int(input("Please type in the value of the signature: "))
print(f"signature:{signature}")



verification = pow(signature, e, n)

if verification == hash_int:
    print("signature valid")
else:
    print("signature invalid")