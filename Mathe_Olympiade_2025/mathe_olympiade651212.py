solutions = []
prime_numb = []
final_solution = []
 
def prime_checker(i):
    for z in range(2,i):
        if i % z == 0:
            is_prime_number = False
            return False
    prime_numb.append(z)    
            
    
    
       



for i in range(1,len(solutions)):
    try:
        for y in range(1,len(solutions)):
            if i % 2 != 0:
                solutions.append(i)
            if i > 95:
                break
            elif solutions[i] == solutions[i-1]:
                solutions.remove(i)
        for x in range(0,(len(solutions))):
            if solutions[x] in prime_numb:
                continue
            if len(final_solution) == 2:
                break
        print(final_solution) 
        print("jgjsdfjbjseg")
        prime_checker(i)
        print(prime_checker(i))
        print(i)
    except KeyboardInterrupt:
        print("Bye")
        
      
