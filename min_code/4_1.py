arr = list(map(int, input().split()))
pr_list = []
for i in arr:
    pr_list.append(f"{i}")
print(" ".join(pr_list))

x = "41369"
t = int(input())
print(f'{t}번index의값은{x[t]}입니다')

arr = list(map(int, input().split()))
print(arr[0]+arr[len(arr)-1])

x = int(input())
pr_list = []
for i in range(5):
    pr_list.append(f"{x+5}")
print(" ".join(pr_list))

arr = "341675"
a, b = map(int,input().split())
print(int(arr[a])+int(arr[b]))

arr = "3125"
x = int(input())
if int(arr[x]) > 2 :
    print("우와")
else:
    print("ㅠㅠ")

arr = [3,9,27,81,243]
x = int(input())
print(arr[x]-100)

x = int(input())
if x > 5:
    for i in range(1,11):
        print(i)
else:
    for i in range(5,0,-1):
        print(i)

x = [5,2,3,4,7]
rev_x = list(map(str,reversed(x)))
print(" ".join(rev_x))

arr = []
x = int(input())
for i in range(0,5):
    arr.append(x-i)
print(arr[2])

a = list(map(int,input().split()))
result = 0
for i in a:
    result += i
print(result)

list_a = [5, 25, 54, 2, -33, 57, 82, -8, 13, 1]
x = int(input())
for i in range(x,len(list_a)):
    print(list_a[i])
