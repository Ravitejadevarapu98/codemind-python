n=int(input())
su=0
i=n*n
while i>0:
    r=i%10
    su+=r
    i=i//10
if su==n:
    print('Neon Number')
else:
    print('Not Neon Number')