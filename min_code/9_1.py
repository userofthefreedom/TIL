# find_num = [4,3,6,1,3,1,5,3]
# inp = int(input())
# answer = 0
# for i in find_num:
#     if i == inp:
#         answer += 1
# print(f'숫자{inp}개수는{answer}개')





# arr = [
#     ['A','B','C','D','E'],
#     ['E','A','B','A','B'],
#     ['A','C','D','E','R']
# ]

# inp = input()
# count_num = 0
# for i in arr:
#     for j in i:
#         if j == inp:
#             count_num += 1

# # cnt = sum(x == inp for row in arr for x in row)

# # flat = sum(arr, [])          # 2차원 -> 1차원 (간단하지만 큰 데이터엔 비효율적)
# # cnt = flat.count(inp)

# if count_num == 0:
#     print("미발견")
# elif 1 <= count_num <= 2 :
#     print("발견")
# else:
#     print("대발견")
# # print("미발견" if cnt == 0 else "발견" if cnt <= 2 else "대발견")







# arr = ['A','F','G','A','B','C']
# inp1, inp2 = map(str,input().split())
# cnt1 = sum(i==inp1 for i in arr)
# cnt2 = sum(i==inp2 for i in arr)
# print("와2개" if cnt1 and cnt2 else "오1개" if cnt1 or cnt2 else "우0개")




