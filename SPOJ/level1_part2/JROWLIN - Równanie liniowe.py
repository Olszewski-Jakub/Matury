a,b,c = list(map(float, input().split()))
if a!=0:
    print(f"{round((c-b)/a,2):.2f}")
elif a==0 and b!=c:
    print("BR")
else:
    print("NWR")