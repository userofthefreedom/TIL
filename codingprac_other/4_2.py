x = "326718"
print(x[int(input())])

x = int(input())
if x != 3: print("3이 아니다")
if x != 5: print("5가 아니다")
if 1 < x < 10:
    for i in range (5,0,-1):
        print(i)

x = int(input())
list = ""
for i in range(5):
    list += str(x)
print(list)

x = "17326"
y = ""
for i in x:
    y += i
print(y)

num_list = list(map(int,input().split()))
print(num_list[0]+num_list[1]+num_list[2])

num_list = [3, 9, 12, 15, 55]
num_set = list(map(int,input().split()))
if sum(num_set)>10:
    print(num_list[len(num_list)-1])
else:
    print(num_list[0])

num_list = [5, 7, 1, 8, -4, -73, 4, 2, 20, 84]
x = int(input())
for i in range(x,-1,-1):
    print(num_list[i])

x = int(input())
num_list = []
for i in range(0,6):
    num_list.append(x+i)
for i in num_list:
    print(i)

x = ["0","0","0","0"]
num_list = list(map(int,input().split()))
x[0],x[2] = str(num_list[0]),str(num_list[1])
print("".join(x))