import random 
import math 

prime = []
def fermat(p,k):
    a = random.randrange(2,p)
    for i in range(k):

        if pow(a, p-1, p) != 1:

            return False
    return True 
            
        
for i in range(100001,1000000,2):
    if i % 100 == 0:
        print(i)
    if fermat(i,10) == True:
        prime.append(i)
print(prime)

