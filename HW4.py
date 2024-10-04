# HW4
# Quinn Dickey
# 5th hour

print("hello world")

famDict = {
    "Quinn": "17",
    "Ashton": "30",
    "JD": "33",
    "Mom": "56"
}
print(famDict['Ashton'])
famDict.update({"Dad": "58"})
print(famDict)
famDict.clear()
print(famDict)
clasDict = {
    "student1": {
        "Name": "Quinn", "hair": "blond", "attendance": "present"
    },
    "student2": {
        "Name": "Ethan", "hair": "brown", "attendance": "present"},
    "student3": {
        "Name": "Preston", "hair": "blond", "attendance": "absent"}

}

print(clasDict)
print(clasDict["student1"]["Name"], clasDict["student2"]["Name"], clasDict["student3"]["Name"])