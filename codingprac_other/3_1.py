number = int(input())
if number >= 10:
    print("WOW")
else:
    print("OMG")

####

a, b = map(int, input().split())
if a > b:
    print(f'큰수는 {a}')
elif a < b:
    print(f'큰수는 {b}')
else:
    print("같은숫자")

####

number = int(input())
if number == 10 or number == 5:
    print("만세")
else:
    print("재도전")

###

a, b = map(int, input().split())
if a == 7 and b == 9:
    print("인증됨")
else:
    print("재시도")

####

for i in range(3, 11):
    print(i)

###

a, b = map(int, input().split())
for i in range(a, b+1):
    print(i)

###

for i in range(25):
    print("PIZZAHOT")

###

number = int(input())
for i in range(number):
    print("##")

###

num_list = []
for i in range(10):
    num_list.append(f'{10-i}')
print(" ".join(num_list))

###

number = int(input())
if int(((number*2)+20)/5) != 100:
    print("Magic")
else:
    pass

####

a, b = map(int, input().split())
incr_num = a
answer = []
while incr_num <= b:
    answer.append(f'{incr_num}')
    incr_num += 1
print("".join(answer))

####

a = int(input())
incr_num = 0
answer = []
while incr_num <= a:
    answer.append(f'{incr_num}')
    incr_num += 1
print("\n".join(answer))

####

a, b, c = map(int, input().split())
if a+b+c > 10:
    print(a*b*c)
else:
    print(0)

###

a = int(input())
answer = []
while a >= 0:
    answer.append(f'{a}')
    a -= 1
print("\n".join(answer))
print("발사")

####

num_list = []
for i in range(-5, 6):
    num_list.append(f"{i}")
print(" ".join(num_list))
