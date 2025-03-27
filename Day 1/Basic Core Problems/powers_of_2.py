#Question 4: All powers of 2 less than 2^n:

def powerOf2(n):
    # Method 1:
    # for i in range(n):
    #     print(2**i, end=" ")

    #Method 2:
    x = 1
    for _ in range(n):
        print (x, end=" ")
        x*=2
    
    return x
n=int(input("Enter a value: "))
powerOf2(n)
