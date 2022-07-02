a=int(input())
c=oc=0
while a>0:
    r=a%10
    if r%2==0:
        c+=1
    else:
        oc+=1
    a//=10
if c!=0 and oc==0:
    print("Even")
elif c==0 and oc!=0:
    print("Odd")
elif c>0 and oc>0:
    print("Mixed")