# arr = []
# for i in range(4):
#     ad_arr = []
#     for j in range(4):
#         ad_arr.append(((i+1)*2)+(j*8))
#     arr.append(ad_arr)

# for i in arr:
#     print(" ".join(list(map(str, i))))


# arr = []
# for i in range(5):
#     ad_arr = []
#     for j in range(5):
#         ad_arr.append(21+i-(j*5))
#     arr.append(ad_arr)

# t = int(input())
# arr[t] = [t]*5

# for i in arr:
#     print(" ".join(list(map(str, i))))


# class Fruit:
#     def __init__(self, name):
#         self.name = name
#         self.size = 0
#         self.price = 0
# banana = Fruit('banana')
# apple = Fruit('apple')
# banana.size = int(input())
# apple.size = int(input())
# banana.price = banana.size * 250
# apple.price = apple.size * 500
# print(f'{banana.price+apple.price}원')


# def main():
#     inp()


# def inp():
#     txt = input()
#     ck_num = check(txt)
#     if ck_num == 1:
#         print("있음")
#     else:
#         print("없음")


# def check(x):
#     is_num = 0
#     for i in arr:
#         for j in i:
#             if j == x:
#                 is_num = 1
#     return is_num


# arr = [
#     ['D', 'A', 'C', 'C', 'D'],
#     ['S', 'D', 'F', 'A', 'E'],
#     ['E', 'E', 'T', 'J', 'H']
# ]

# main()


# num_list = list(map(int, input().split()))

# arr = []
# for i in num_list:
#     ad_lst = []
#     for j in range(i, i+4):
#         ad_lst.append(j)
#     arr.append(ad_lst)

# for i in arr:
#     print(*i)
