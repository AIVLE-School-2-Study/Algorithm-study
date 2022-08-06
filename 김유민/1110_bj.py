N = int(input)
count = 0
n = N

while True:
    a = n / 10
    b = n % 10
    c = a + b
    n = (b*10)+(c%10)
    count += 1
    
    if N == n:
        break
print(n)