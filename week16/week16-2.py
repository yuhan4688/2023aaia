#想研究前個程式 是怎麼跑的
s='00111'
N=len(s)
ans=0
for left in range(N-1):
  print("left:",left,'i<=left有誰?',end=' ')
  for i in range(N):
    if i<=left: print(s[i],end=' ')
  print('i>left有谁?',end=' ')
  for i in range(N):
    if i>left: print(s[i],end=' ')
  print()