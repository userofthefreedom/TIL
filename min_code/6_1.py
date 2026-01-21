def get_input():
    global A, B
    A, B = map(str,input().split())
def let_output():
    print(f"{A} {B}")
def main_fuc():
    get_input()
    let_output()
main_fuc()



ascii_list = list(map(str,input().split()))
for i in ascii_list:
    print(ord(i))

x = int(input())
for i in range(x):
    for j in range(1,6):
        print(j,end=" ")
    print("")



askk = "$@DA9#"
for i in askk:
    print(f"{i}:{ord(i)}")





wo_list = ["B", "T", "K", "A"]
for i in range(int(input())):
    print(*wo_list)



chr = input()
if ord(chr) > 90:
    print("소문자입니다")
else :
    print("대문자입니다")


shap_count = int(input())
for i in range(shap_count):
    for j in range(shap_count):
        print("#",end="")
    print("")

chr = input()
check = int(chr)
if 0 <= check <= 9:
    print(check+5)


alphab = input()
wrong_list = []
x = "A"
while ord(x) <= ord(alphab) :
    wrong_list.append(x)
    x = chr(ord(x)+1)

print("".join(wrong_list))




t = input()
print(chr(ord(t)-32))


ch1, ch2 = map(str, input().split())
pri_list = []
for i in range(ord(ch1),ord(ch2)+1):
    pri_list.append(chr(i))
for i in range(4):
    print(" ".join(pri_list))





flag = 0
a, b, c = map(str, input().split())

def process():
    global flag
    if a == "A" and b == "B" and c == "C":
        flag = 1
def output1():
    if flag == 1:
        print("ABC를찾았다")
    else:
        print("못찾았다")

process()
output1()





a, b, c = map(int, input().split())
atoc_list = []
for i in range(a,b+1):
    atoc_list.append(str(i))
for j in range(c):
    print(" ".join(atoc_list))