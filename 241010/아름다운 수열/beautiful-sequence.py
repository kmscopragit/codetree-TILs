N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))

M = int(input())
B = []
for _ in range(M):
    B.append(int(input()))
B.sort()

answer = []
for i in range(N-M+1):
    subA = sorted(A[i:i+M])
    for j in range(M-1):
        if (subA[j+1] - subA[j]) != (B[j+1] - B[j]):
            break
    else:
        answer.append(i+1)

print(len(answer))
for e in answer:
    print(e)