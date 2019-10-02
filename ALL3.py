solution-3
-------------
l=list(map(int,input().split()))
n=0
for i in range (len(1)-1):
If l[i]<=1[i+1]:
n+=1
If n==1:
print(“True”)
else:
print(“False”)

solution-1
-----------
s=list(map(str,input().split()))
k=int(input(""))
p=[]
o=""
o=o+s[0]
for i in s[l::]:
    f=o
    o=o+ " "+i
    if(len(o)>k):
        p.append(f)
        o=" "
        o=i
if k<len(i):
    print("null")
else:
    p.append(o)
    print(p)

soltion-2
-----------
l=s=list(map(int,input().split()))
k=int(input())
g=0
s=0
for i in range(len(l)):
    if g!=len(l):
        p=[]
        s=0
        for j in l[g::]:
            s=s+jp.append(j)
            if s==k:
                print(p)
        g+=1