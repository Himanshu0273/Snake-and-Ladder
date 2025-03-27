from random import randint

class Coupon:
    @staticmethod
    def coupon(lst, limit):
        set1 = set()
        i=0
        while i!=len(lst):
            if lst[i] in set1:
                i+=1
            else:
                x = randint(0,limit)
                if x==lst[i]:
                    i+=1
                set1.add(x)
                print(f"Random Number : {x}")
                    
        return len(set1)
    
        
n = int(input("Enter the number of elements: "))
lst = [] 
for _ in range(n):
    x = int(input())
    lst.append(x)

limit = int(input("Enter the max value of the coupon possible: "))
print(f"Distinct coupon numbers: {Coupon.coupon(lst, limit)}")
