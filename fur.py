import json

# Load JSON data
with open("D:/try8/extraction/extractedgodrej/output.json/updated_master_bedroom_godrej.json") as f:
    master_bedroom_data = json.load(f)

with open('D:/try8/extraction/extractedgodrej/output.json/MasterBedroom_6.json') as f:
    master_bedroom_details = json.load(f)

# Room dimensions
room_width = master_bedroom_data['room']['width']
room_length = master_bedroom_data['room']['length']

# Wall mapping
wall_mapping = {
    1: "Wall_1",
    2: "Wall_2",
    3: "Wall_3",
    4: "Wall_4"
}

# Dimensions of furniture
bed_dimension = [2.0, 1.5]  # Example: [length, width]
side_stool_1_dimension = [0.5, 0.5]
side_stool_2_dimension = [0.5, 0.5]

# Update furniture positions
furniture = []
for wall in master_bedroom_details["WallDetails"]:
    wall_name = wall_mapping.get(wall["WallNo"])
    subspace_key = wall["SubspaceProductCKey"]

    if "KSB" in subspace_key:
        # King Size Bed
        config = {
            "Wall_1": ([0, room_width / 2, 0], 1.5708),
            "Wall_2": ([room_length / 2, room_width, 0], 0),
            "Wall_3": ([room_length, room_width / 2, 0], 4.71239),
            "Wall_4": ([room_length / 2, 0, 0], 3.14159)
        }
        location, z_rotation = config[wall_name]
        furniture.append({
            "type": "Bed",
            "name": "King Size Bed",
            "model_path": f"{master_bedroom_data['path']['base_path']}Rest/King Size Bed.blend",
            "location": location,
            "rotation": [0, 0, z_rotation],
            "material_config":{},
            "scale": [1, 1, 1],
            "geometry_nodes_params": {}
        })

    if "ST1" in subspace_key:
        # Side Stool 1
        config = {
            "Wall_1": ([0, (room_width / 2) - (bed_dimension[1] / 2) - (side_stool_1_dimension[1] / 2), 0], 1.5708),
            "Wall_1": ([0, (room_width / 2) - (bed_dimension[1] / 2) - (side_stool_2_dimension[1] / 2), 0], 1.5708),
            "Wall_2": ([(room_length / 2) - (bed_dimension[0] / 2) - (side_stool_1_dimension[0] / 2), room_width, 0], 0),
            "Wall_3": ([room_length, (room_width / 2) + (bed_dimension[1] / 2) + (side_stool_1_dimension[1] / 2), 0], 4.71239),
            "Wall_4": ([(room_length / 2) - (bed_dimension[0] / 2) - (side_stool_1_dimension[0] / 2), 0, 0], 3.14159)
        }
        location, z_rotation = config[wall_name]
        furniture.append({
            "type": "Side_stool_1",
            "name": "Side Stool 1",
            "model_path": f"{['base_path']}Rest/Side Stool 1.blend",
            "location": location,
            "rotation": [0, 0, z_rotation],
            "scale": [1, 1, 1],
            "material_config":{},
            "geometry_nodes_params": {}
        })

    if "ST2" in subspace_key:
        # Side Stool 2
        config = {
            "Wall_1": ([0, (room_width / 2) + (bed_dimension[1] / 2) + (side_stool_2_dimension[1] / 2), 0], 1.5708),
            "Wall_2": ([(room_length / 2) + (bed_dimension[0] / 2) + (side_stool_2_dimension[0] / 2), room_width, 0], 0),
            "Wall_3": ([room_length, (room_width / 2) - (bed_dimension[1] / 2) - (side_stool_2_dimension[1] / 2), 0], 4.71239),
            "Wall_4": ([(room_length / 2) - (bed_dimension[0] / 2) - (side_stool_2_dimension[0] / 2), 0, 0], 3.14159)
        }
        location, z_rotation = config[wall_name]
        furniture.append({
            "type": "Side_stool_2",
            "name": "Side Stool 2",
            "model_path": f"{['base_path']}Rest/Side Stool 2.blend",
            "location": location, 
            "rotation": [0, 0, z_rotation],
            "scale": [1, 1, 1],
            "material_config":{},
            "geometry_nodes_params": {}
        })

# Add updated furniture to the JSON
master_bedroom_data["furniture"] = furniture

# Save the updated JSON
updated_file_path = 'D:/try8/extraction/extractedgodrej/updated_master_bedroom_with_furniture.json'
with open(updated_file_path, 'w') as f:
    json.dump(master_bedroom_data, f, indent=4)

print(f"Updated JSON saved to {updated_file_path}")
