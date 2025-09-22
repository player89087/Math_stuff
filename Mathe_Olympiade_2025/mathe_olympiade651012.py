
# all solutions for a^2 + b^2 = 65
solutions_1 = []
for i in range(0,1000):
    for x in range(0,1000):
        if i**2 + x**2 == 65:
                solutions_1.append(i)
                solutions_1.append(x)

print(solutions_1)
# all solutions for a^2 + b^2 = 340
solutions_2 = []
for i in range(0,1000):
    for x in range(0,1000):
        if i**2 + x**2 == 340:
                solutions_2.append(i)
                solutions_2.append(x)

print(solutions_2)

solutions_3 = []

for i in range(0,8024):
    for x in range(0,8024):
        if i**2 + x**2 == 8024:
                solutions_3.append(i)
                solutions_3.append(x)
        

print(solutions_3)

# no result back --> there is no solution

