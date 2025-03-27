#Question 6: Prime Factors

def isPrime(n):
    for i in range(2, (n//2)+1):
        if n%i==0:
            return False
    
    return True

n = int(input("Enter a number : "))
lst=[]
for i in range (2, (n//2)+1):
    if n%i==0 and isPrime(i):
        lst.append(i)
    
print(lst)