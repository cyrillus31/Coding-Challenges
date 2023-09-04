import json 


def parse_json_data(data: dict):
    id = data["id"]
    name = data["name"]
    parent = None
    if "parent" in data:
        parent = data["parent"]
    return id, name, parent


final_result = []
amount_of_incoming_data = int(input())

for i in range(amount_of_incoming_data):
    rows = int(input())
    json_lst = []
    for i in range(rows):
        row = input()
        json_lst.append(row.strip())

    json_str = ''.join(json_lst)
    json_d = json.loads(json_str)

    result = []

    id_dict = {}
    for category in json_d:
        id, name, parent = parse_json_data(category)
        if parent is None:
            root = {"id": 0, "name": name, "next": []}
            # id_dict['root'] = root
        else:
            if parent not in id_dict:
                id_dict[parent] = [{"id": id, "name": name, "next": []}]
            else:
                id_dict[parent].append({"id": id, "name": name, "next": []})

    def return_children(parent_id: dict) -> {}:
        if parent_id not in id_dict:
            return [] 
        else:
            children = id_dict[parent_id]
            for child in children:
                child["next"] = return_children(child["id"])
            return children

    root["next"] = return_children(0)
    final_result.append(root)

print(json.dumps(final_result))

# added = {}
# for categroy in json_d:
    # data = json_d[category]
    # id, name, parent = parse_json_data(data)
    # if parent is None:
        # root = {"id": 0, "name": name, "next": []}
        # parents["root"] = root
    # if parent not in added:










# parents = {}
# for category in json_d:
    # data = json_d[category]
    # id, name, parent = parse_json_data(data)
    # if parent is None:
        # root = {"id": 0, "name": name, "next": []}
        # parents["root"] = root

    # if parent not in parents:
        # parents[parents] = [{"id": id, "name": name, "next": []}]
    # else:
        # parents[parent].append({"id": id, "name": name, "next": []})

# for parent in parents:
    # if parent == 'root':
        # continue

    

# for category in json_d:
    # data = json_d[category]
    # id, name, parent = parse_json_data(data)
    # if id == 0:
        # root = {"id": id, "name": name, "next": []}
    # result_json = 

