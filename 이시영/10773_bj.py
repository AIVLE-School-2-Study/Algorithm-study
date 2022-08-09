from sys import stdin

k=int(stdin.readline())
sta=[]
for _ in range(k):
    a=int(stdin.readline())
    if a==0:
        sta.pop()
    else:
        sta.append(a)
    
print(sum(sta))