#variables help you store a value that value can later change with time
name="lohith"
#list can store multiple values together
Games = ["minecraft","roblox","forza4","tabs","spore"]
#dictionaries can be used to store values in key-value pairs
diction = {
    "lohith":100,
    "tanshi":90,
    "raj":80,
    "arnay":75,
}
print(diction)
print(diction.keys())
print(diction.values())
#do changes to current value
diction["arnay"]=73
print(diction)
print(diction.get("raj"))
diction.clear()
print(diction)