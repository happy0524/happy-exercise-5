""" 
print(subway[2])
print(subway.index("pu"))
subway.append("iyor")
print(subway)
subway.insert(1,"ru")
print(subway)


subway = ["pu","pidlet","tiger"]

print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)

subway.append("pu")
print(subway.count("pu"))

# subway.clear()

num = [2,4,3,5,1]
num.sort(reverse=True)
print(num)
num.reverse()
print(num)

subway.extend(num)
print(subway)


"""


""" 
print(cab[3])
print(cab.get(5))

print(cab.get(5, "usable"))
print(cab)
print(cab.get(3, "usus"))

print(3 in cab)
print(77 in cab)

print("p" in "pullup")

cab = {3: "pu", 100 : "piglet"}
empty = {}

# del cab[3]
# print(cab)

print(cab.keys())
print(cab.values())
print(cab.items())
cab.clear()

menu = ("don", "che", "a","ca")
print(menu[1:3])

(name, age, hobby) = ("피글렛", 20, "코딩")
print(name)



print(java & python)
print(java.intersection(python))

print(java|python)
print(java.union(python))

print(java - python)
print(java.difference(python))

java = {"pu", "pig", "ti"}
python = set(["pu", "igo"])
go = set()

python.add("pig")
java.remove("pig")

menu = {"커피" , "우유", "주스"}
print(menu)

menu = tuple(menu)
print(type(menu))

"""

from random import *


reply = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:11,12:12,13:13,14:14,15:15,16:16,17:17,18:18,19:19,20:20}
liss = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

shuffle(liss)

win = sample(liss,4)

print("-- 당첨자 발표 --")

print("치킨 당첨자 : ", win[0])
print("커피 당첨자 : ", win[1:])

print("-- 축하합니다! --")


