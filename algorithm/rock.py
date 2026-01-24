A, B = map(int,input().split())

if A>B:
    if A-B == 2 :
        Answer = "B"
    else:
        Answer = "A"
else:
    if B-A == 2 :
        Answer = "A"
    else :
        Answer = "B"

print (Answer)

    
    