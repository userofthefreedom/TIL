a = "\"나는 지금\" 집에가고 싶다"
print(a)
print(type(a))
b= '''\'나는 지금\'
집에가고 싶다'''
print(b)
print(type(b))  
c = """\"나는 지금\"
집에가고 싶다"""
print(c)
print(type(c))
d ="what i need now \n is a good rest \t and sleep"
print(d)
e = "now"
f = " is time"
print(e*2)
print (len(a))
print(e[1])
print(a[-2])
print(a[0:5])
print(a[5:])
a = "20230331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)

real ="I eat %d apples." % 3
print(real)

native = "I eat %s apples." % "five"
print(native)

number = 3
print("I eat %d apples." % number)

number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))

print("I have %s%% apples" % 3)
print("%-10sjane." % 'hi')
print("%0.4f" % 3.42134234)


number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))