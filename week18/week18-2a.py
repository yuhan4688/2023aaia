#soit106_base_011
a,b=list(map(int,input().split()))

if a<b: ans=-1
if a==b: ans=0
if a>b: ans=1
print(ans)