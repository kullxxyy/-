N = int(input())
L = list(map(int, input().split()))

count = {}

list
for i in range(N):
    x=L[i]

    if x in count:
        count[x] +=1

    else:
        count[x] = 1

max_count = max(count.values())

ans = []
for j in count:
    if count[j] ==max_count: 
        ans.append(j)
print(max(ans))






    

