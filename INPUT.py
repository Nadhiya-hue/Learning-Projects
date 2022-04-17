# Enter your code here. Read input from STDIN. Print output to STDOUT
xk=list(map(int,input().split()))
print(xk)
x = xk[0]
k = xk[1]
P= input()
if eval(P)==k:
    print(True)
else:
    print(False)
