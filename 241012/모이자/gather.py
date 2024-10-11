n = int(input())

arr = list(map(int, input().split()))

res = 10000000
for i in range(n):
    ith_total = 0
    for j in range(n):
        ith_total += arr[j] * abs(j-i)
    if ith_total < res:
        res = ith_total

print(res)