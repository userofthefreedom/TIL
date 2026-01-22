# x = int(input())
# t = 1
# while t <= x:
#     print(t,end=" ")
#     t += 1


# st_list = list(map(int,input().split()))
# for i in st_list:
#     if i == 7:
#         break
#     print(i,end=" ")




# def inp():
#     global a, b
#     a,b = map(int,input().split())

# def out():
#     t = 5
#     while t <= a+b:
#         print(t,end=" ")
#         t += 1

# inp()
# out()






# st_list = list(map(int,input().split()))
# for i in range(len(st_list)-1,-1,-1):
#     if st_list[i] == 7:
#         print(st_list[i])
#         break
#     print(st_list[i],end=" ")




# st_pr = [3,4,1,6,7,5]
# cout_num = 0
# while cout_num < len(st_pr):
#     print(st_pr[cout_num],end=" ")
#     cout_num += 1


# def inp():
#     global first_list
#     first_list = []
#     start_num = int(input())
#     for i in range(3):
#         addme = []
#         for j in range(4):
#             addme.append(start_num + j + (i*4))
#         first_list.append(addme)
# # def inp():
# #     global first_list
# #     start_num = int(input())
# #     nums = list(range(start_num, start_num + 12))
# #     first_list = [nums[i*4:(i+1)*4] for i in range(3)]
# # def make_grid():
# #     start_num = int(input())
# #     return [[start_num + i*4 + j for j in range(4)] for i in range(3)]
# # first_list = make_grid()

# def process():
#     for i in range(3):
#         for j in range(4):
#             first_list[i][j] += 1
# # def process():
# #     global first_list
# #     first_list = [[x + 1 for x in row] for row in first_list]
# # def process():
# #     global first_list
# #     first_list = [list(map(lambda x: x + 1, row)) for row in first_list]

# def out():
#     for i in first_list:
#         print(*i)

# inp()
# process()
# out()





def inp():
    global txt
    txt = input()

def out():
    if 'a' <= txt <= 'z':
        print('BD5QA')
    elif 'A' <= txt <= 'Z':
        print('QEREF')
    else :
        print("".join(chr(i) for i in range(72,64,-1)))
    
inp()
out()