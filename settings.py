the_map = [
    [0, 0, 1, 0],
    [1, 3, 3, 0],
    [2, 3, 3, 1],
    [0, 0, 2, 0]
]
a1 = the_map[0][0]
a2 = the_map[0][1]
a3 = the_map[0][2]
a4 = the_map[0][3]
b1 = the_map[1][0]
b4 = the_map[1][3]
c1 = the_map[2][0]
c4 = the_map[2][3]
d1 = the_map[3][0]
d2 = the_map[3][1]
d3 = the_map[3][2]
d4 = the_map[3][3]

print(a1)
position = a1
place = int(input("place? "))
if place > 11:
    place -= 12
if place == 0:
    position = a1
elif place == 1:
    position = a2
elif place == 2:
    position = a3
elif place == 3:
    position = a4
elif place == 4:
    position = b4
elif place == 5:
    position = c4
elif place == 6:
    position = d4
elif place == 7:
    position = d3
elif place == 8:
    position = d2
elif place == 9:
    position = d1
elif place == 10:
    position = c1
elif place == 11:
    position = b1

print(position)
print(place)
