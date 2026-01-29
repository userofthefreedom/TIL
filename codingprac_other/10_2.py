arr = []
for i in range(4):
    ad_arr = []
    for j in range(4):
        ad_arr.append(((i+1)*2)+(j*8))
    arr.append(ad_arr)

for i in arr:
    print(" ".join(list(map(str, i))))


arr = []
for i in range(5):
    ad_arr = []
    for j in range(5):
        ad_arr.append(21+i-(j*5))
    arr.append(ad_arr)

t = int(input())
arr[t] = [t]*5

for i in arr:
    print(" ".join(list(map(str, i))))


class Fruit:
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.price = 0


banana = Fruit('banana')
apple = Fruit('apple')
banana.size = int(input())
apple.size = int(input())
banana.price = banana.size * 250
apple.price = apple.size * 500
print(f'{banana.price+apple.price}원')


def main():
    inp()


def inp():
    txt = input()
    ck_num = check(txt)
    if ck_num == 1:
        print("있음")
    else:
        print("없음")


def check(x):
    is_num = 0
    for i in arr:
        for j in i:
            if j == x:
                is_num = 1
    return is_num


arr = [
    ['D', 'A', 'C', 'C', 'D'],
    ['S', 'D', 'F', 'A', 'E'],
    ['E', 'E', 'T', 'J', 'H']
]

main()


num_list = list(map(int, input().split()))

arr = []
for i in num_list:
    ad_lst = []
    for j in range(i, i+4):
        ad_lst.append(j)
    arr.append(ad_lst)

for i in arr:
    print(*i)


arr = []
for i in range(6):
    ad_lst = []
    for j in range(3):
        ad_lst.append(10+i+(j*6))
    arr.append(ad_lst)

a, b = map(int, input().split())
for i in range(a, b+1):
    arr[i] = [7, 7, 7]

for i in arr:
    print(*i)


def main():
    result = aToZ()
    print(result)


def aToZ():
    t = input()
    result = None
    if abs(ord(t) - ord('A')) < abs(ord(t) - ord('Z')):
        result = 'A'
    else:
        result = 'Z'
    return result


main()


def main():
    t = Calculator()
    print(t)


def Calculator():
    score = int(input())
    result = None
    if score >= 90:
        result = 'A'
    elif score >= 80:
        result = 'B'
    elif score >= 70:
        result = 'C'
    else:
        result = 'D'
    return result


main()


arr = [
    [1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0]
]


def main():
    t = inp()
    p = process(t)
    out(p)


def inp():
    result = int(input())
    return result


def process(x):
    result = 0
    for i in arr:
        if i[x] == 1:
            result += 1
    return result


def out(x):
    print(x)


main()


def main():
    t = int(input())
    run(t)


def run(x):
    arr = []
    if x < 10:
        for i in range(3):
            ad_arr = []
            for j in range(3):
                ad_arr.append(1 + j + (i*3))
            arr.append(ad_arr)
    else:
        for i in range(3):
            ad_arr = []
            for j in range(3):
                ad_arr.append(3 - j + (i*3))
            arr.append(ad_arr)

    for i in arr:
        print(*i, sep="")


main()


def main():
    t = yesOrNo()
    print(t)


def yesOrNo():
    r = int(input())
    result = None
    if r % 3 == 0:
        result = 7
    elif r % 3 == 1:
        result = 35
    else:
        result = 50
    return result


main()
