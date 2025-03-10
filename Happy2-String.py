""" 
sentence = "I'm a boy"
print(sentence , type(sentence))

print(sentence[-6:])





python = "Python is Amazing"

print(python.lower())
print(python.upper())
print(python[0].isupper())
print(python[1:3].islower())
print(python.replace("Python","Java"))



find = python.find("n")
print(find)

find = python.find("n" , find + 1)
print(find)

find = python.find("java")
print(find)

index = python.index("n")
print(index)

index = python.index("n", index + 1)
print(index)

print(python.count("n"))
print(python.count("v"))

print(len(python))


print("ab" + "ab")
print("ab", "ab")

age = 20

print("나는 %d살 입니다" % age)
print("나는 %s살 입니다" % "파이썬")
print("나는 %c살 입니다" % 'D')
print("나는 %s살 입니다" % 20)
print("나는 %s색과 %s색을 좋아합니다." %("파란" , "빨간"))

print("i'm {} years old".format(25))
print("i'm {} years {} old".format("blue" , "red"))
print("i'm {1} years {0} old".format("blue" , "red"))
print("i'm {color2} years {color1} old".format(color1 = "blue" , color2 = "red"))

age = 25
color = "red"
print(f"i like {color} color, \n{age} old years.")
print(r"https://chatgpt.com/c/67baf46c-08dc-800f-a3d9-73f653a7ae40")
print("Red Apple\rPine")
print("redd\b apple")
print("appllee\tcore")

"""

n = "https://naver.com"
d = "https://daum.com"
g = "https://google.com"
y = "https://youtube.com"

n1 = n[8:-4]
d1 = d[8:-4]
g1 = g[8:-4]
y1 = y[8:-4]

print(n1[0:3] + str(len(n1)) + str(n1.count("e")) + "!")
print(d1[0:3] + str(len(d1)) + str(d1.count("e")) + "!")
print(g1[0:3] + str(len(g1)) + str(g1.count("e")) + "!")
print(y1[0:3] + str(len(y1)) + str(y1.count("e")) + "!")
