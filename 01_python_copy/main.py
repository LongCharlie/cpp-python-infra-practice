import copy

data = {"id" : 101 ,"labels" : ["cat" , "pet"]}

shallow = data.copy()
shallow["labels"].append("dogs")

print(data)

deep = copy.deepcopy(data)
deep["labels"].append("lions")

print(deep)
print(data)


new = {"id" : data["id"],"labels":list(data["labels"])}
new["labels"].append("monster")
print(new)
print(data)