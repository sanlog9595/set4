a,b=input().Split()
if(a.isdigit()==True and b.isdigit()==True):
  a=int(A)
  b=int(B)
  
def swap(A,B):
  if(a>0 and b>0):
    (A,B)=(B,A)
    print(a,b)
swap(a,b)
