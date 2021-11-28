import json

datadict =  { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 }
json_str = json.dumps(datadict)
print(type(json_str))
json_dict = json.loads(json_str)

print(type(datadict),datadict['a'])
print (type(json_dict),json_dict['a'])

#===

