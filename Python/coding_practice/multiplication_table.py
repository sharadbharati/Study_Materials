def multiplication_table(n):
    i = 1 
    while i <= 10: 
    # for i in range(1, 11): 
        # print(n, "x", i, "=", n*i) 
        print(f"{n} X {i} = {n*i}")  # f-string
        # print("{} X {} = {}".format(n, i, n*i))
        i = i + 1
        
# n = int(input()) 
n = input("Enter Number: ")  
multiplication_table(int(n))
