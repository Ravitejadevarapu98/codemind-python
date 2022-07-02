a=int(input())
arr=list(map(int,input().split()))
ri=arr[0]
j=1
while j<a:
    if arr[j]%ri==0:
        j+=1
    else:
        ri=arr[j]%ri
print(ri)