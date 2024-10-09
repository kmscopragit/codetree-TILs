import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

def to_tri(num):
    if num == 0:
        return '0'
    temp = []
    while num:
        temp.append(str(num%3))
        num = num//3
    return ''.join(temp[::-1])

for i in range(len(a)):
    new = a[:i] + str(1 - int(a[i])) + a[i+1:]
    num = int(new, 2)
    tri_num = to_tri(num)   # type : str
    cnt = 0
    if len(tri_num) != len(b):
            continue
    for j in range(len(b)):
        if tri_num[j] == b[j]:
            cnt += 1
    if cnt == len(b) - 1:
        print(num)
        break