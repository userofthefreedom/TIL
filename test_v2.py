# 리스트 최대값 구하기
#  [122, 72, 252, 182] → 252

lst = [112, 17, 215, 118]
check_num = -21e8
for i in lst:
    if i > check_num:
        check_num = i
print(check_num)

# 리스트의 문자열중 길이가 가장 긴 문자열출력 (길이가 같다면 앞에문자열) (len 사용금지)
# print(longest_string(['panda', 'caterpillar', 'dog', 'rabbit'])) → caterpillar 출력
# 만약 길이가 같은 문자열이 여러 개 있다면, 리스트에서 먼저 찾은 문자열을 반환한다
lst = ['panda', 'caterpillar', 'dog', 'rabbit', 'watermellon']
check_lst = []
for i in lst:
    count = 0
    for j in i:
        count += 1
    check_lst.append(count)
default_num = -21e8
for i in check_lst:
    if i > default_num:
        default_num = i
print(lst[check_lst.index(default_num)])

# eat 그리고 exercise 가 들어있는 문자열 리스트가 있는데 eat의 확률을 반올림 하지 말고 소숫점으로 출력하라.
# (sum len filter count 사용금지)
# ['eat', 'exercise', 'eat', 'exercise'] → 0.5 출력

lst = ['eat', 'exercise', 'eat', 'exercise']
count_all = 0
count_eat = 0
for i in lst:
    if i == 'eat':
        count_eat += 1
    count_all += 1
print(count_eat/count_all)


# 리스트에 정수값이 있다 짝수가 몇개있고 짝수의 합을 튜플로 출력 (sum len filter 사용금지)
#  [12, 7, 10, 5, 8] → (3, 30) 출력

lst = [212, 27, 110, 55, 68]
ev_count = 0
ev_sum = 0
for i in lst:
    if i % 2 == 0:
        ev_count += 1
        ev_sum += i
print(ev_count, ev_sum)

# 리스트 안에 있는 key의 값들을 모두 더했을때 합 출력하기
# sum Max 사용불가

# data = {'onion': 1000, 'lettuce': 800} 가 주어지고
# lst = ['lettuce', 'onion', 'onion'] 가 주어진다면 # 2800 출력

data = {'mango': 1000, 'apple': 900, 'grape': 1200}
lst = ['apple', 'apple']  # 1800

pl_num = 0
for i in lst:
    pl_num += data.get(i, 0)
print(pl_num)


set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

print(set3 <= set1)  # -subset->
print(set1 >= set3)  # <-superset-

print(set1.difference(set2))  # {0, 2, 4} -
print(set1.intersection(set2))  # {1, 3} &
print(set1.issubset(set2))  # False <=
print(set3.issubset(set1))  # True <=
print(set1.issuperset(set2))  # False >=
print(set1.union(set2))  # {0, 1, 2, 3, 4, 5, 7, 9} |
