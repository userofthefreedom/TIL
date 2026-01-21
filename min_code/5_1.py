x = input()
print(x*3)

x = list(map(int,input().split()))
answer = 0
for i in x:
    answer += i
print(answer)

x = "min"
num = int(input())
print(x[num])

def KFC():
    print("KFC입니다")

def MC():
    print("MC입니다")

x = int(input())
if x == 1:
    KFC()
if x == 2:
    MC()

def LOT():
    print("12345")

x = int(input())
for i in range(x):
    LOT()


def KFC():
    print("##########")

def MC():
    print("@@@@@@@@@@")

KFC()
MC()


x = list(map(int,input().split()))
x.append(int(input()))
x.extend([x[3]+1, x[3]+2])
plist = []
for i in x:
    plist.append(str(i))
print(" ".join(plist))


x = 0
def KFC():
    global x
    x = int(input())

def BBQ():
    if x > 5:
        print("만세")
    else:
        print("다시")

KFC()
BBQ()


x = "ABC"

def KFC():
    for i in x:
        print(i, end="")
    print()

def main():
    count_num = int(input())
    for i in range(count_num):
        KFC()

main()



def get_input():
    global base_list
    base_list = list(map(str,input().split()))

def output():
    for i in range(1, len(base_list)+1):
        print(base_list[-(i)],end="")

def main():
    get_input()
    output()

main()


x = int(input())
list_x = [int(i) for i in range(x,x+6)]
def PrintAll():
    for i in list_x:
        print(i)

PrintAll()




def QTR():
    print("QTR100%")

def BBQ():
    print("BBQ100%")

A, B, C = map(int, input().split())
if A + B + C >= 10:
    QTR()
else:
    BBQ()


x = "34158177369"
t = int(input())
result = []
for i in range(0,len(x),t):
    result.append(x[i])
print(" ".join(result))