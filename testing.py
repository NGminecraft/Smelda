import numpy as np

with open("Untitled spreadsheet - Copy of Sheet2.csv", "r") as csv:
    readCsv = csv.read()
    csv = readCsv.split("\n")
    for i in csv:
        c.append(i.split(","))

print(np.save("map3", np.asarray(c)))
