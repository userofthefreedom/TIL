def one():
    num = int(input())
    return num


def two():
    txt = input()
    return txt


n = one()
t = two()
print(n, t, sep="")


arr = [[0]*4 for _ in range(4)]
check = int(input())
if check % 2 == 0:
    for i in range(4):
        arr[i][i] = i+1
else:
    for i in range(4):
        arr[i][-(i+1)] = i+1
for i in arr:
    print(" ".join(list(map(str, i))))


def main():
    KFC()
    return


def KFC():
    x = chicken()
    y = coke()
    print(x, y, sep="")


def chicken():
    num = int(input())+10
    return num


def coke():
    txt = input()
    return txt


main()


def main():
    t = getChar()
    print(t)


def getChar():
    lst = list(map(str, input().split()))
    lst.sort(reverse=True)
    return lst[0]


main()


answer = []
check = (int(input())) % 5
if check == 1:
    for i in range(9, 6, -1):
        ad_lst = []
        for j in range(3):
            ad_lst.append(i-(j*3))
        answer.append(ad_lst)
elif check == 2:
    for i in range(3):
        ad_lst = []
        for j in range(3):
            ad_lst.append(7-(i*3)+j)
        answer.append(ad_lst)
else:
    for i in range(3):
        ad_lst = []
        for j in range(3):
            ad_lst.append(10+i+(j*3))
        answer.append(ad_lst)
for i in answer:
    print(" ".join(list(map(str, i))))


def main():
    a, b = map(int, input().split())
    if int(a/b) % 2 == 0:
        even(int(a/b))
    else:
        odd(int(a/b))
    printData(a+b)


def even(x):
    printData(x*2)


def odd(x):
    printData(x-10)


def printData(x):
    print(x)


main()


def main():
    a = GOP()
    b = SUM()
    if a > b:
        print("GOP>SUM")
    elif a < b:
        print("GOP<SUM")
    else:
        print("GOP==SUM")


def GOP():
    x, y = map(int, input().split())
    return x*y


def SUM():
    x, y = map(int, input().split())
    return x+y


main()


def main():
    stone = int(input())
    ret = pingpong(stone)
    print(ret)


def pingpong(x):
    tong = x
    return tong + 10


main()


arr = []
for i in range(4):
    ap_arr = []
    for j in range(4):
        ap_arr.append(13+i-(j*4))
    arr.append(ap_arr)
for i in arr:
    print(" ".join(list(map(str, i))))


arr = []
for i in range(3):
    ap_arr = []
    for j in range(4):
        ap_arr.append(12-(i*4)-j)
    arr.append(ap_arr)
change = int(input())
for i in arr:
    i[change] = 0
for i in arr:
    print(" ".join(list(map(str, i))))


arr = []
for i in range(4):
    arr.append(list(map(int, input().split())))
for i in range(4):
    for j in range(4):
        if arr[i][j] % 2 == 0:
            if arr[i][j] == 0:
                arr[i][j] = "!"
            else:
                arr[i][j] = '#'
        else:
            arr[i][j] = '@'
for i in arr:
    print("".join(i))


def main():
    t = int(input())
    CountDown(t)


def CountDown(x):
    for i in range(x, 0, -1):
        print(i, end=" ")


main()
