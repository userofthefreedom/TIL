check_list = list(map(int, input().split()))
count = 0
for i in check_list:
    if i < 5:
        print(f'{count}번은 {i}점 불합격')
    else:
        print(f'{count}번은 {i}점 합격')
    count += 1







ini_list = ['D','T','A','B','W','Q']
ini_inp = input()
count = 0
for i in ini_list:
    if i == ini_inp:
        print(f'{count}번 INDEX')
    count += 1
# ini_list = ['D','T','A','B','W','Q']
# ini_inp = input()
# for idx, ch in enumerate(ini_list):
#     if ch == ini_inp:
#         print(f'{idx}번 INDEX')







base_list = [""]*5
char_num = int(input())
char_list = input().split()

for i in range(char_num):
    base_list[i] = char_list[i]
for i in base_list:
    print(i,end="")







base_list = [""]*17
def inp():
    x,y,z = input().split()
    for i in range(0,7):
        base_list[i] = x
    for i in range(7,13):
        base_list[i] = y
    for i in range(13,17):
        base_list[i] = z
inp()
print("".join(base_list[-i] for i in range(1,18)))






ch1,ch2,num = input().split()
pri_list = ""
for i in range(ord(ch1),ord(ch2)+1):
    pri_list += chr(i)
for i in range(int(num)):
    print(pri_list)
# ch1, ch2, num = input().split()
# num = int(num)
# line = "".join(chr(i) for i in range(ord(ch1), ord(ch2) + 1))
# print("\n".join([line] * num))





chara, num = input().split()
line = "".join(chara for i in range(int(num)))
print("\n".join([line]*int(num)))





arr = [[0 for i in range(3)] for j in range(3)]
point_x,point_y,num = map(int,input().split())
arr[point_x][point_y] = num
print("\n".join(" ".join(map(str,i)) for i in arr))
# # 3x3 배열(0으로 초기화)
# grid = [[0] * 3 for _ in range(3)]
# # 입력: x y num
# x, y, value = map(int, input().split())
# # 좌표에 값 넣기
# grid[x][y] = value
# # 출력 (각 행을 "0 0 0" 형태로)
# for row in grid:
#     print(" ".join(map(str, row)))





arr = [[0]*3 for i in range(6)]
x, y = map(int,input().split())
for i in range(3):
    for j in range(3):
        arr[i][j] = x
for i in range(3,6):
    for j in range(3):
        arr[i][j] = y

for i in arr:
    print("".join(map(str,i)))





fir,scd = input().split()

arr = [([fir]*4)+([scd]*2)]*3
for i in arr:
    print("".join(i))
