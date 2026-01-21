def debugger(code, password):
    nums = 0
    for i in code:
        if nums < len(password) and i == password[nums]:
            nums += 1
        
    return "통과" if nums == len(password) else "실패"


T = int(input().strip())
results = []

for i in range(1,T+1):
    code = input().strip()
    password = input().strip()
    result = debugger(code, password)
    results.append((i,result))

for i, result in results:
    print(f"#{i} {result}")

