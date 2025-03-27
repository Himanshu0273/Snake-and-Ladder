#Question 3: Leap Year or not

year = int(input("Enter a 4 digit year: "))

if year>=1000 and year<=9999:
    if (year%4==0 and year%100!=0) or year%400==0:
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is not a leap year")        
else:
    print("Enter a Valid year")