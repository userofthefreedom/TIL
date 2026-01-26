# A = [2, 1, 2, 4, 5]
# B = [
#     [2, 5, 3],
#     [4, 5, 7],
#     [8, 7, 2]
# ]

# count_num = 0
# t = int(input())

# count_num += A.count(t)
# for i in B:
#     count_num += i.count(t)

# print(count_num)


# ch_lst = input().split()
# count_num = 0
# count_num += ch_lst.count('A')
# print(f'문자A는 {count_num}개발견')
# ind_lst = [i for i, x in enumerate(ch_lst) if x == 'A']
# for i in ind_lst:
#     print(f'{i}번')


# arr = [
#     ['D', 'A', 'A'],
#     ['B', 'C', 'D'],
#     ['E', 'F', 'A'],
#     ['A', 'A', 'D'],
#     ['F', 'G', 'E']
# ]

# check = input()
# answer = []
# for i, i_lst in enumerate(arr):
#     for j, j_cha in enumerate(i_lst):
#         if j_cha == check:
#             answer.append((i, j))
# for i, j in answer:
#     print(f'({i},{j})')


# arr = [
#     [10, 3, 20],
#     [60, 30, 40],
#     [20, 30, 40]
# ]

# a, b = map(int, input().split())
# count = 0
# for i in arr:
#     for j in i:
#         if a <= j <= b:
#             count += 1
# print(count)


# def main():

#     def inp():
#         global arr
#         raw_inp = input().split()
#         arr = []
#         for i in range(2):
#             add_lst = []
#             for j in range(3):
#                 add_lst.append(raw_inp[i*3+j])
#             arr.append(add_lst)

#     def findUpper():
#         count = 0
#         for i in arr:
#             for j in i:
#                 if 65 <= ord(j) <= 90:
#                     count += 1
#         print(f'대문자{count}개')

#     def findLower():
#         count = 0
#         for i in arr:
#             for j in i:
#                 if 97 <= ord(j) <= 122:
#                     count += 1
#         print(f'소문자{count}개')

#     inp()
#     findUpper()
#     findLower()
#     return


# main()
