A,B,C,D = map(int, input().split())

ans = 0
for x in range(A+1): 
    if B >=C*x and x + C*x <=D:
        ans = x

print(ans)

