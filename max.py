m=10
n=input().Split()
for i in range(m):
n.insert(i,int(n[i]))
n.remove(n[i+1])
n.sort(reverse=True)
print(n[0])
