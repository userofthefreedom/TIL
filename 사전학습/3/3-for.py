list = [1,3,5,7,9]
for i in list:
    print(i)

marks = [90, 25, 67, 45, 80]   # 학생들의 시험 점수 리스트

number = 0   # 학생에게 붙여 줄 번호
for mark in marks:   # 90, 25, 67, 45, 80을 순서대로 mark에 대입
    number = number +1 
    if mark >= 60: 
        print("%d번 학생은 합격입니다." % number)
    else: 
        print("%d번 학생은 불합격입니다." % number)

add = 0 
for i in range(1, 11): 
    add = add + i 
print(add)

for i in range(2,10):        # 1번 for문
    for j in range(1, 10):   # 2번 for문
        print(i*j, end=" ") 
    print('')

a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits, 1):  # 1부터 시작
    print(f"{i}: {fruit}")