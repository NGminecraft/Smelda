import numpy as np

c= []
with open("Legend of smelda - Big (1).csv", "r") as csv:
    readCsv = csv.read()
    csv = readCsv.split("\n")
    for i in csv:
        c.append(i.split(","))

print(np.save("map", np.asarray(c)))
