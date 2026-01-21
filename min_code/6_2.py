cara1, cara2 = map(str, input().split())
print(
    f"문자'{cara1}'의 아스키코드값은 {ord(cara1)}\n"
    +f"문자'{cara2}'의 아스키코드값은 {ord(cara2)}"
      )


cara = input()
x = ord(cara)
while x >= ord('a') :
    print(chr(x),end="")
    x -= 1




car_list = list(map(str, input().split()))
car_print1 = " ".join(car_list)
car_print2 = " ".join(car_list)
print(car_print1)
print(car_print2)





deci_num = ord(input())
if 48 <= deci_num <= 57:
    print("숫자문자입력!!")
if 65 <= deci_num <= 90:
    print("대문자입력!!")
if 97 <= deci_num <= 122:
    print("소문자입력!!")



num_list = list(map(int,input().split()))
pr_list = list(map(str,num_list))
for i in range(sum(num_list)):
    print(" ".join(pr_list))


ch_list = list(map(str,input().split()))
check_list = 0
for i in ch_list:
    if i.isdigit():
        check_list += 1

if check_list == 0:
    print("숫자미발견")
else:
    print(f"숫자{check_list}개발견")



alph_list = list(map(str, input().split()))
result = []
for i in alph_list:
    if 65 <=  ord(i) <= 90:
        result.append(chr(ord(i)+32))
    if 97 <= ord(i) <= 122:
        result.append(chr(ord(i)-32))
print(" ".join(result))



list_for =""
list_back = ""
t = input()
for i in range(5):
    list_for += chr(ord(t)+i)
    list_back += chr(ord(t)-i)
print(list_for)
print(list_back)





alph_list = ["5","4","1","2","7","8"]
rev_list = reversed(alph_list)
line = " ".join(rev_list)
print("\n".join([line]*int(input())))





alph_list = list(map(str, input().split()))
if ord(alph_list[0]) >= ord(alph_list[1]) and ord(alph_list[0]) >= ord(alph_list[2]):
    print(f"옳다{alph_list[0]}")
else:
    print("옳지않음")




ch1, ch2 = map(str, input().split())
print(ord(ch2)-ord(ch1))
