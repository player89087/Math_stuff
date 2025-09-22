solutions = []
for i in range(100000,1000000):
    i = str(i)
    if "0" in i:
        continue
    
    sum_first_nums = int(i[0]) + int(i[1])
    last_num = int(i[4] + i[5])
    middle_num = int(i[2] + i[3]) 
    if sum_first_nums == last_num and middle_num  == sum_first_nums + 1 : 
        solutions.append(i)


print(len(solutions))
print(solutions)
