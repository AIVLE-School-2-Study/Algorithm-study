from sys import stdin

n=int(stdin.readline())
sta=[]
for i in range(n):
    h=int(stdin.readline())
    sta.append(h)

key=sta[-1]
count=1
for i in reversed(range(n)):
    if key<sta[i]:
        count+=1
        key=sta[i]
        
    
        
print(count)