count = int(input())
result = []
for t in range(1, count + 1):
    nA, nB = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    num_list = []
    if nA >= nB:
        for i in range(nA-nB+1):
            base = 0
            for j in range(nB):
                base = base + A[j+i]*B[j]
            num_list.append(base)
    if nA < nB:
        for i in range(nB-nA+1):
            base = 0
            for j in range(nA):
                base = base + A[j]*B[j+i]
            num_list.append(base)
    answer = max(num_list)
    result.append(f"#{t} {answer}")

print("\n".join(result))