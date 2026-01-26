find_num = [4, 3, 6, 1, 3, 1, 5, 3]
inp = int(input())
answer = 0
for i in find_num:
    if i == inp:
        answer += 1
print(f'숫자{inp}개수는{answer}개')


arr = [
    ['A', 'B', 'C', 'D', 'E'],
    ['E', 'A', 'B', 'A', 'B'],
    ['A', 'C', 'D', 'E', 'R']
]

inp = input()
count_num = 0
for i in arr:
    for j in i:
        if j == inp:
            count_num += 1

# cnt = sum(x == inp for row in arr for x in row)

# flat = sum(arr, [])          # 2차원 -> 1차원 (간단하지만 큰 데이터엔 비효율적)
# cnt = flat.count(inp)

if count_num == 0:
    print("미발견")
elif 1 <= count_num <= 2:
    print("발견")
else:
    print("대발견")
# print("미발견" if cnt == 0 else "발견" if cnt <= 2 else "대발견")


arr = ['A', 'F', 'G', 'A', 'B', 'C']
inp1, inp2 = map(str, input().split())
cnt1 = sum(i == inp1 for i in arr)
cnt2 = sum(i == inp2 for i in arr)
print("와2개" if cnt1 and cnt2 else "오1개" if cnt1 or cnt2 else "우0개")


arr = [3, 4, 2, 5, 7, 9]
a, b = map(int, input().split())
arr[a], arr[b] = arr[b], arr[a]
print(" ".join(map(str, arr)))


class ABC:
    def __init__(self):
        self.x = 0
        self.y = 0


t = ABC()
a, b = map(int, input().split())
t.x = a
t.y = b
print(t.x + t.y)


arr = []
for i in range(65, 74, 3):
    su_arr = []
    for j in range(i, i+3):
        su_arr.append(chr(j))
    arr.append(su_arr)
old_x, old_y = map(int, input().split())
new_x, new_y = map(int, input().split())
arr[old_x][old_y], arr[new_x][new_y] = arr[new_x][new_y], arr[old_x][old_y]
for i in arr:
    print(''.join(i))


arr = []
for _ in range(6):
    x, y = map(int, input().split())
    arr.append([x, y])
answer = []
change_count = 0
for i in range(6):
    if arr[i][0] < arr[i][1]:
        arr[i][0], arr[i][1] = arr[i][1], arr[i][0]
        change_count += 1
    answer.append(arr[i])

for i in answer:
    print(i[0], i[1])
print(f'{change_count}명')


def main():
    global a, b
    a, b = map(int, input().split())
    BBQ(a, b)
    return


def BBQ(x, y):
    print(f'합:{a+b}')
    print(f'차:{a-b}')
    print(f'곱:{a*b}')
    print(f'몫:{int(a/b)}')


main()


arr = [
    ['F', 'E', 'W'],
    ['D', 'C', 'A']
]


def main():
    global cha
    cha = input()
    findCh(cha)
    return


def findCh(x):
    check = 0
    for i in arr:
        check += (x in i)
    if check == 0:
        print("미발견")
    else:
        print('발견')


main()


arr = input().split()
check = []
for i in arr:
    if i.isupper():
        check.append("대")
    else:
        check.append('소')
print(*check, sep='')


class Person:
    def __init__(self, age=0, height=0):
        self.age = age
        self.height = height


a = Person()
b = Person()

a.age, a.height, b.age, b.height = map(int, input().split())

print(int((a.age+b.age)/2), int((a.height+b.height)/2))
