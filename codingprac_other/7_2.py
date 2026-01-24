t = input()
for i in range(6):
    if i <= 2:
        for j in range(5):
            print(t,end="")
    else :
        for j in range(3):
            print(t,end="")
    print("")




t = [0]*6
lst_idx = list(map(int, input().split()))
for i in lst_idx:
    t[i]=1
print(*t)



txt_list = list(map(str,input().split()))
if 65 <= ord(txt_list[0]) <= 90 and 65 <= ord(txt_list[1]) <= 90 :
    print("대문자들")
elif 65 <= ord(txt_list[0]) <= 90 or 65 <= ord(txt_list[1]) <= 90 :
    print("대소문자")
else:
    print("".join(f'{chr(i)}' for i in range(97,123)))




txt_base = input()
adding_char = ord(txt_base)
char_list = []
for i in range(3):
    ready_list = []
    for j in range(5):
        ready_list.append(chr(adding_char))
        adding_char += 1
    char_list.append(ready_list)
# char_list[2][2] = chr(ord(char_list[2][2])+32)
char_list[2][2] = char_list[2][2].lower()
print(char_list[2][2])



char_list = list(map(str,input().split()))
count_num = 0
for i in char_list:
    if 'A' <= i <= 'Z' :
        count_num += 1

if count_num == 3:
    print("풍족하다")
elif count_num == 0:
    print("부족하다")
else:
    print("적절하다")


lst_0 = [
    [0,0,0,0],
    [0,0,0,0]
]
x, y =map(int,input().split())
lst_0[x][y] = 1
print(*lst_0[0])
print(*lst_0[1])





lst_ready = list(map(int,input().split()))
answer_list = []
for i in range(3):
    answer_list.append([lst_ready[i*2]+2,lst_ready[i*2+1]+2])
for k in answer_list:
    for j in k:
        print(j,end=" ")
    print("")
