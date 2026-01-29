a, b, c = map(int, input().split())
print(a*3)
print(b*3)
print(c*3)

print(f"두 숫자의 차는 {a-b} 입니다.")

print(f"{a}+{b}={a+b}")
print(f"{a}*{b}={a*b}")
print(f"{a}/{b}={a//b}")

if a > b:
    print("a가b보다크다")
else:
    print("b가a보다같거나크다")

if a > b:
    print(f"{a}"*4)
else:
    print(f"{b}"*4)

####

alpha = int(input())
print(f"{alpha} 입력함")
alpha += 1
print(f"a++을 수행하면 {alpha}이 됩니다.")

####

num = int(input())
if num > 0:
    print("###\n###\n###")
elif num == 0:
    pass
else:
    print("$$$\n$$$")

###

a, b, c = map(int, input().split())
if a+b+c >= a*b*c:
    print("행운의 수")
else:
    print("소소한 수")
