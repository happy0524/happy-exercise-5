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
"""

cab = {3: "pu", 100 : "piglet"}
empty = {}

# del cab[3]
# print(cab)

print(cab.keys())
print(cab.values())
print(cab.items())
cab.clear()