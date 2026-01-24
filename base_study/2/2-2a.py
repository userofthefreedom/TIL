
a = "%.4f"%124.121242
b = "%15.5f"%50.93811255
print(a) 
print(b)
c = "I have {cat} cats and {dog} dogs.".format(cat=3, dog="five")
print(c)

d = "I love"
e = a[:5]
print(d + " " + e + b[7:-3])
f = "{{asdf}}".format()
print(f)
d =  {'nam' : '세진', 'age' : 25}   
g=f'나의 이름은 {d["nam"]}이고, 나이는 {d["age"]}살 입니다.'
print(g)
h = 25
i = f'나는 내년이면 {h**2}살이 된다.'
print(i)
print(i.find('내'))
print(i.find('k'))
print(i.find("살이"))
print(",".join(i))
j = "aPPle"
print(j.lower())
print(j.upper())
print(j.capitalize())
print(i.replace("내년이면", "내후년이면"))
list = [1, 3, 5, 2, "나는", [73, 74], 1.5, "apple"]
del list[4:]
print (list)
list.sort()
print(list)
list.insert(2, 76)
print(list)
print(list.pop(4))
print(list)
