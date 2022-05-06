a=int(input())
sum=0
for i in range (1,a+1):
    sum+=1/i
print("{1:.2f}".format(a,sum))