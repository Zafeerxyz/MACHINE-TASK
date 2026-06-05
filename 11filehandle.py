with open("names.txt","w") as names:
    names.write("zafeer alkan  lalu")
count = 0  
names = open("names.txt","r")
view = names.read()
splitted = view.split()
for i in splitted:
    count += 1
print("The number of names in the list",len(splitted))
print(view)
print(splitted)
print(count)
