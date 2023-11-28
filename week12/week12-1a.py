a=120
#1 2 3 4 5 6 8 10 12 16 ...for迴圈
ans=0 #迴圈前面，ans是0
for i in range(1,a+1):
  if a%i==0:
    print(i,end=' ')
    ans+=1
print(ans)