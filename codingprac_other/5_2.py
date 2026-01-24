def mincoding():
    A, B = map(int,input().split())
    print(f'({A})({B})')
mincoding()



def KFC():
    print("KFC")
def BBQ():
    print("BBQ")

txt = input()
if txt == "B":
    KFC()
    BBQ()
if txt == "b":
    BBQ()
if txt == "7":
    KFC()




A, B = map(str,input().split())
A = A*5
B = B*5
def PrintAll():
    print(A)
    print(B)

PrintAll()

t = int(input())
list_kfc = []
for i in range(5):
    list_kfc += f"{t-i}"

def KFC():
    for i in list_kfc:
        print(i,end="")

KFC()



arr = "41235"
t = input()
if t == "a" or t == "b" or t == "c" :
    print(" ".join(arr[3::-1]))
else:
    print(" ".join(arr[4:0:-1]))




arr = "3512467"
a, b = map(int,input().split())
print(" ".join(arr[a:b+1]))



num = int(input())
l_num=[]
for i in range(4):
    l_num.append(str(num-i))
print(" ".join(l_num))

A, B = map(int, input().split())
answer_list = []
for i in range(3):
    answer_list.append(str(A+i))
for j in range(3):
    answer_list.append(str(B+j-2))
print(" ".join(answer_list))



A, B = map(int, input().split())
answer_list = []
for i in range(5):
    answer_list.append(str(A+(B*i)))
print(" ".join(answer_list))


t = int(input())
num_list = [t+(i*t) for i in range(6)]
print(*num_list)


base = list(map(int, input().split()))
num_sum = sum(base)
print(f"합은 {num_sum}입니다")


a, b = map(int,input().split())
print("".join(f'{i}' for i in range(a,b+1)))