# def inp():
#     return map(int, input().split())


# def main():
#     a, b, c = inp()

#     calc(a, b, c)


# def calc(x, y, z):
#     print(x + y + z)


# main()


# def sum(a, b):
#     return a+b


# def comp(a, b):
#     return a-b


# def prt(a, b):
#     print(f'합:{a}')
#     print(f'차:{b}')


# def main():
#     x, y = map(int, input().split())
#     s_num = sum(x, y)
#     c_num = comp(x, y)
#     prt(s_num, c_num)


# main()


# lst = [3,4,1,3,2,7,3]
# test_num = int(input())
# if test_num in lst:
#     print("발견")
# else:
#     print("미발견")


# lst = list(map(int,input().split()))
# print(f'MAX={max(lst)}')
# print(f'MIN={min(lst)}')


# string = "StructPointer"
# txt = input()
# print("발견" if txt in string else "미발견")


# txt_list = list(map(str, input().split()))
# big = []
# small = []
# for i in txt_list:
#     if i.isupper():
#         big.append(i)
#     else:
#         small.append(i)
# print("big=", end="")
# print(*big, sep="")
# print("small=", end="")
# print(*small, sep="")


arr = [
    [3, 2, 6, 2, 4],
    [1, 4, 2, 6, 5]
]


def KFC(x):
    for i in arr:
        if x in i:
            return 1
    return 0
