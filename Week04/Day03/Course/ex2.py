sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
keysToRemove = ["name", "salary"]

sampleDict2 = dict(sampleDict)

print(sampleDict)
print(sampleDict2)
for key in keysToRemove:
    del sampleDict[key]
    waste = sampleDict2.pop(key)
print(sampleDict)
print(sampleDict2)