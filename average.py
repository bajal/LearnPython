N=int(input())
a={}
for i in range(0,N):
    b = input()
    a[b.split()[0]] = [float(s) for s in b.split()[1:]]
print(a)
match=input()
res = round(sum(a[match]) / len(a[match]), 2)
print( "%0.2f" % res)
