from sys import stdin
n=list(stdin.readline().rstrip())  # .rstrip() \nė ėė ė¤
for i in range(len(n)):
    if n[i]=='\'':
        n[i]=('\\\'')
    elif n[i]=='\"':
        n[i]=('\\\"')
    elif n[i]=='\\':
        n[i]=('\\\\')
n="".join(n)
print(n)