map_town = """                                      ---------------- 
                                     /              / \      
                                    /              /   |
                  /-------\          |  PizzaPlex |  O |
-------           | Weapon|          |            |    |
| Spawn point     |  Shop |          |            |    |
|                 |    0  |          |      0     |    |
----------------------------------------------------------------------
"""


def map_parser(map_to_parse): #turns maps into 2d arrays
    i = 0
    d1 = []
    d2 = []
    while i < len(map_to_parse):
        
        if(map_to_parse[i] == "\n"):
            d2.append(d1)
            d1 = []
        else:
            d1.append(map_to_parse[i])
        i+=1
    return d2

print(map_parser(map_town))




"""
#recursion method was not allowed by python
i = 0 
d2_list_to_return = []
d1_to_append_to_2d = []
def map_parser(map_to_parse): #turns maps into 2d arrays
    global i 
    global d2_list_to_return
    global d1_to_append_to_2d
    if(map_to_parse[i] == "\n"):
        d2_list_to_return.append(d1_to_append_to_2d)
        d1_to_append_to_2d = []
    else:
        d1_to_append_to_2d.append(map_to_parse[i])
    if(i<len(map_to_parse)):
        map_parser(map_to_parse)
    i+=1
    return d2_list_to_return
i = 0 
d2_list_to_return = []
d1_to_append_to_2d = []
print(map_parser(map_town))
"""


