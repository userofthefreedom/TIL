print_ready = []
for i in range (3,9):
    print_ready.append(f'{i}')
print(" ".join(print_ready))

num = int(input())
print(f'{num}'*3)
print(f'{num+1}'*3)
print(f'{num+2}'*3)

num_list = list(map(int,input().split()))
if num_list == [1,2,3,4]:
    print("로그인성공")
else : 
    print("로그인실패")

num = int(input())
answer = []
for i in range(2,5):
    answer.append(f'{num+i}')
print(" ".join(answer))

num_list = list(map(int,input().split()))
if num_list[0] == max(num_list):
    print("MAX발견")
else :
    print("MAX아님")

num_list = list(map(int,input().split()))
if 30 < num_list[0]*num_list[1] < 50 :
    print("적당한 사이즈")
elif num_list[0]*num_list[1] >= 50 :
    print("큰 사이즈")
else:
    print("작은 사이즈")

a, x = list(map(int,input().split()))
answer = []
for i in range(1,x+1):
    answer.append(f'{a-i}')
print(" ".join(answer))

a, b, c = list(map(int,input().split()))
print_ab = [str(i) for i in range (a, b+1)]
print_ac = [str(i) for i in range (a, c+1)]
print(" ".join(print_ab))
print(" ".join(print_ac))

for i in range(9, 5, -1):
    print(f"{i} {i-3}")

x = int(input())
answer_list = [x]
x0 = x
while x > 1 :
    x -= 2
    answer_list.extend([x,x+((x0-x)*2)])
answer_list = sorted(answer_list)
print_list = list(map(str,answer_list))
print(" ".join(print_list))

print("시작")
answer = []
for i in range(1,6):
    answer.append(f"{i}")
print("".join(answer))
print("종료")

x = int(input())
px = []
for i in range(x):
    px.append(f"##\n@@")
print("\n".join(px))

for i in range(1,6):
    print(f"{i}번go!!")

a, b = list(map(int,input().split()))
if a == 1111 and b == 2222:
    print("로그인성공")
elif a == 1111 and b != 2222:
    print("비밀번호가 틀렸습니다")
else:
    print("아이디가 틀렸습니다")

x = int(input())
x_list = []
for i in range(x,-1,-1):
    x_list.append(f'{i}')
print("".join(x_list))