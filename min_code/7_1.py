arr_odd = [3, 5, 2, 4, 1]
arr_even = [
    [9,8],
    [7,1],
    [3,4],
]
if int(input())%2 == 1 :
    print("".join(map(str,arr_odd)))
else :
    for i in arr_even:
        print("".join(map(str,i)))




a, b = sorted(list(map(int, input().split())))
if (b - a)%2 == 1:
    print("고백한다")
else:
    print("짝사랑만")



arr= [
    [3,1,1],
    [2,3,2],
]
for i in arr:
    for j in i:
        print(j,end="")






arr = list(map(int, input().split()))
answer = 0
for i in arr:
    if 3 <= i <= 7:
        answer += 1
print(answer)




t = int(input())
if t >= 80 :
    print("수")
elif t >= 70 :
    print("우")
elif t >= 60 :
    print("미")
else:
    print("재시도")




t = list(map(int, input().split()))
for i in t:
    if i < 20 :
        print("더 큰수를 입력하세요")
    elif i > 20 :
        print("더 작은수를 입력하세요")
    else:
        print("정답입니다")





t = list(map(int, input().split()))
print(f'MAX={max(t)}')
print(f'MIN={min(t)}')





arr = [
    [3,4,1],
    [2,1,4],
    [3,3,0],
]
count_odd = 0
count_even = 0
for i in arr:
    for j in i:
        if j%2==0:
            count_even += 1
        else:
            count_odd += 1
print (f'짝수 : {count_even}'+"\n"+ f'홀수 : {count_odd}')





t = list(map(int, input().split()))
man_count = 0
for i in t:
    man_count += 1
    test_result = ""
    if i >= 70 :
        test_result = "PASS"
    elif i >= 50 :
        test_result = "RETEST"
    else:
        test_result = "FAIL"
    print(f'{man_count}번사람은{i}점{test_result}')





def input1():
    global result_list
    result_list = []
    for i in range(4):
        result = []
        for j in range (4):
            result.append(alp)
        result_list.append(result)
    return result_list
def output():
    for i in result_list:
        print("".join(i))
alp = input()
input1()
output()





def process(a):
    result_list = []
    for i in range(3):
        result = []
        for j in range(3):
            result.append(a)
            a += 1
        result_list.append(result)
    return result_list
    
def output(b):
    for e,r,t in b:
        print(e,r,t)
            
output(process(int(input())))








def BBQ(a):
    if 0<a<5:
        print("초기값")
    elif 6<a<10:
        print("중간값")
    else:
        print("알수없는값")

num = int(input())
if num == 3 or num == 5 or num == 7 :
    for i in range(1,11):
        print(i,end="")
elif num == 0 or num == 8:
    for i in range(10,0,-1):
        print(i,end="")
else:
    BBQ(num)