# if (조건문)

a = int(input()) #정수값 입력
if a == 3 :
    print("정답")
else :
    print("오답")


if a>3:
    print("오삼")
if a<1:
    print("냉면")
elif a>5:
    print("불고기")
else:
    print("만세")

if a % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 반복문 (for/while)
x = 0
while x < 5:
    print("*", end="")
    x += 1

y = 0 
while y < 10 :
    print("*",end=" ")
    y += 1

for x in range (10):
    print("*",end=" ")

numbers = [1,2,3,4,5,6,7,8,9]
for i in numbers:
    if i % 2 == 1 :
        print(f"{i}은(는) 홀수입니다.")
    else:
        pass

for idx in range(len(numbers)):
    if numbers[idx]%2==1:
        print(f'{numbers[idx]} is 홀수')

# 함수

def a():
    print("------")
    print("++++++")
a()

# 모듈
import random
menu = ["새마을식당", "요아정", "마라탕", "가지볶음"]
select_lunch = random.choice(menu)
print(select_lunch)

select_lunch = random.choices(menu,k=2)
print(select_lunch)

select_lunch = random.sample(menu,k=2)
print(select_lunch)


# SWAP
y, x = 1, 5

temp = y
y = x
x = temp
print(x, y)


# bool

a = 0
b = -10
a = bool(a)
b = bool(b)
print(a, b)


#float, 소수점

a = 3.15
print(type(a))
print(round(a,1))
print(f'{a:.1f}')

a = 1.2 - 1.1
print(a)
print(round(a,1))

print(round(0.5))
print(round(1.5))
print(round(2.5))
print(round(3.5))
print(round(4.5))

print(round(0.05+0.0000001,1))
print(round(0.15+0.0000001,1))
print(round(0.25+0.0000001,1))
print(round(0.35+0.0000001,1))
print(round(0.45+0.0000001,1))
print(round(0.55+0.0000001,1))

print(round(0.05+1e-8,1))
print(round(0.15+1e-8,1))
print(round(0.25+1e-8,1))
print(round(0.35+1e-8,1))
print(round(0.45+1e-8,1))
print(round(0.55+1e-8,1))

# 순서가 있는 자료형
s = "abcdeFG"
print(s[:3])
print(s[3:])
print(s[2:5])
print(s[5:2:-1])
print(s[1:6:2])
print(s[::-1])
print(s[-2])

print(s+"ABC")
print(s*2)
print(s+"1")


ret = s.replace(s[1],"ㄱ")
print(ret)

test1 = s.capitalize()
print(test1)
test1 = s.lower()
print(test1)
test1 = s.upper()
print(test1)

capital = "A"
test = chr(ord(capital)+32)
print(test)
print(ord(capital))
print(chr(97))

small = "b"
test1 = small.upper()
print(test1)

test2 = chr(ord(small)-32)
print(test2)

# Range

print(range(3))
print(list(range(3)))
print(*list(range(3)))



# tuple
tp = (1,2,3,4,5)
print(tp)
print(type(tp))
print(tp[1])
print(len(tp))

test = list(tp)
print(test)


# 딕셔너리
di = { 1:3,
      2: { "ㄱ" : "가자",
          "ㄴ" : "나는",
      },
      3 : "집",
      "교" : [2, 3, 4]
      }
print(di)
di[3] = "집에 가자"
print(di)

di.pop(1)
print(di)
di ['test'] = 2352163
print(di)
di ["test"] = 55
print(di)



# set
s = {1,2,3,4,5}
print(s)
print(type(s))

lit = [1,2,2,1,111,2,1,3,4,5,3,4,5,6,7,4,5,6,8,9,99]
lit = set(lit)
print(lit)
lit = list(set(lit))
print(lit)


s1 = {1,2,3}
s2 = {3,6,9}
print(s1|s2)
print(s1-s2)
print(s1&s2)



# 킬러 문항 
a, b = 0, -1
print(bool(a),bool(b))
a1 = bool("k")
a2 = bool("")
print(bool(a1),bool(a2))


print("a"and"b")
print(""and"c")
print(0 and 1)

print( 1 or 0 )
print( 0 or -1 )
print( -1 or 1)


a = 1
b = 0
c = 3
print(a|c)
print(b|c)
print(a&b)
print(a&c)
print(c&a)
