# def flattenDict(d,parent="",sep="."):
#     flat = {}
#     for key, value in d.items():
#         newkey = f"{parent}{sep}{key}" if parent else key
#         if isinstance(value,dict):
#              flat.update(flattenDict(value,newkey,sep=sep))
#         else:
#             flat[newkey]= value
           
#     return flat
# data = {
#     "name":"a",
#     "address":{
#         "city":"bang",
#         "pin":123
#     }
# }
# print(flattenDict(data))


flat = {}
def flattenDict(val,parentkey="",sep="."):
    
    for key, values in val.items():
        newkey = f"{parentkey}{sep}{key}" if parentkey else key
        if isinstance(values,dict):
            flattenDict(values,newkey,sep)
        else:
            flat[newkey]= values

data = {
    "name":"a",
    "address":{
        "pin":122,
        "city":"banglore",
        "lol":{
            "name":"ok"
        }
    }
}
flattenDict(data)
print(flat)
    
        
        
        