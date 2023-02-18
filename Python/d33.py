# Dictionary in Python
# Combination of key value pairs

info={
    "Name":"Shobhit Yadav",
    "Course":"Python",
    "Age":22,
    "City":"Ghaziabad"
}

print(type(info))
print(info["Age"])              # Ir throws error if key is not present
print(info.get('Age'))          # It does not throw any error

print(info.keys())              # Get all the keys

for key in info.keys():
    print(f"Value corresponding to key {key} is : {info[key]}")

print(info.values())            # Get all the values

print(info.items())
for key,value in info.items():
    print(f"Value for key {key} is : {value}")