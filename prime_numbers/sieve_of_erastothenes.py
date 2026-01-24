import time 
prime = []

nums = []

for i in range(0,150000000):
    nums.append(True)
nums[0] = False
nums[1] = False
for x in range(0,len(nums)):
    if nums[x] == True:
        prime.append(x)
        for y in range(x,len(nums),x):
            nums[y] = False

print(prime)



