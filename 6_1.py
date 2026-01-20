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
