#Question 5: Harmonic Sum till n: (1/1 + 1/2 + ... + 1/n)

def harmonic(n):
    sum = 0
    for i in range (1, n+1):
        sum += (1/i)
    return sum

n =int(input("Enter the last number: "))
print(f"Harmonic Sum: {harmonic(n)}")