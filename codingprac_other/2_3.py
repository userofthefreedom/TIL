print('WWW."MIN"CODING.CO.KR')

###

a, b = map(int, input().split())
if a == b:
    print("같습니다")
else:
    print("다릅니다")

###

a, b, c = map(int, input().split())
print(f"첫번째 숫자는 {a} 입니다.\n두번째 숫자는 {b} 입니다.\n세번째 숫자는 {c} 입니다.")

###

a, b, c, d = map(int, input().split())

print(f'a + b = {a+b}\nc + d = {c+d}\nALL SUM = {a+b+c+d}')

####

a, b, c = map(int, input().split())
if a == b:
    if b == c:
        print("만세")
    else:
        pass
else:
    pass

###

b1, b2, b3, b4 = map(int, input().split())
if b1 >= b2:
    if b1 >= b3:
        if b1 >= b4:
            print("b1이 가장 크다")
        else:
            pass
    else:
        pass
else:
    pass

###

list = list(map(int, input().split()))
mid_base = 0
answer = []
for i in list:
    mid_base += i
mid = mid_base//len(list)

for j in list:
    if j > mid:
        answer.append(f'{j}>{mid}')
    elif j == mid:
        answer.append(f'{j}=={mid}')
    else:
        answer.append(f'{j}<{mid}')
print("\n".join(answer))

###

a, b = map(int, input().split())

if (a-b) > 5:
    print("멀다")
else:
    print("가깝다")

###

a, b = map(int, input().split())
if a + b > 10:
    print("합만세")
else:
    pass
if a*b > 10:
    print("곱만세")
else:
    pass

####

numbers = list(map(str, input().split()))
answers = numbers[3:]
print(" ".join(answers))

###
print_ready = ""
for i in range(10):
    print_ready += "#"
print(print_ready)
