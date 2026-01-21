# t = input()
# for i in range(6):
#     if i <= 2:
#         for j in range(5):
#             print(t,end="")
#     else :
#         for j in range(3):
#             print(t,end="")
#     print("")




# t = [0]*6
# lst_idx = list(map(int, input().split()))
# for i in lst_idx:
#     t[i]=1
# print(*t)


# 97 <= x <= 122: 소문자 65 <= ord(txt_list[0]) <= 90

txt_list = list(map(str,input().split()))
if 65 <= ord(txt_list[0]) <= 90 and 65 <= ord(txt_list[1]) <= 90 :
    print("대문자들")
elif 65 <= ord(txt_list[0]) <= 90 or 65 <= ord(txt_list[1]) <= 90 :
    print("대소문자")
else:
    print("".join(f'{chr(i)}' for i in range(97,123)))
