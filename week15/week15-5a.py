#soit108_advance_008
a=list(map(int,input().split()))

a.sort()

for i in range(10-1,-1,-1):
	print(a[i],end=' ')