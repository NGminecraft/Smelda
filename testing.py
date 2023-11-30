import numpy
"""
c= []
with open("Legend of smelda - Big Collision.csv", "r") as csv:
    readCsv = csv.read()
    csv = readCsv.split("\n")
    for i in csv:
        c.append(i.split(","))

print(np.save("BigMapCollision", np.asarray(c)))"""


collision_map = "BigMapCollision.npy"
carr = numpy.load(collision_map)
dictionary = {}
for row_num, row in enumerate(carr):
    for column_num, column in enumerate(row):
        dictionary[(row_num * 30, column_num * 30)] = column

for i in dictionary:
    with open("Dict.txt", "w")as txt:
        txt.write(str(i))
        txt.write(", ")
        txt.write(str(dict[i]))
        txt.write("\n")