
# all solutions for a^2 + b^2 = 65
solutions = []
for i in range(0,1000):
    for x in range(0,1000):
        if i**2 + x**2 == 1000000:
                solutions.append(i)
                solutions.append(x)

print(solutions)