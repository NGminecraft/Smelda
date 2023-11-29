import numpy as np

c= []
with open("Legend of smelda - Big Collision.csv", "r") as csv:
    readCsv = csv.read()
    csv = readCsv.split("\n")
    for i in csv:
        c.append(i.split(","))

print(np.save("BigMapCollision", np.asarray(c)))