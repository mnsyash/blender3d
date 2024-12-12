import json

# File paths
input_json_file = "D:/try8/extraction/extractedgodrej/output.json/MasterBedroom_6.json"  # The extracted information file
master_bedroom_file = "D:/try8/extraction/master_bedroom.json"  # The template file
output_file = "D:/try8/extraction/extractedm3m/updated_master_bedroom_godrej.json"

# Load data from input files
with open(input_json_file, "r") as file:
    output_data = json.load(file)

with open(master_bedroom_file, "r") as file:
    master_bedroom_data = json.load(file)

# Extract room dimensions from output.json
room_length = output_data["SpaceDetails"]["Length"] / 1000  # Convert mm to meters
room_width = output_data["SpaceDetails"]["Width"] / 1000  # Convert mm to meters
room_height = output_data["SpaceDetails"]["Height"] / 1000  # Convert mm to meters
wall_thickness = 0.2  # Example wall thickness in meters
skirting_height = 0.0375

def calculate_room_location(length, width):
    return [length / 2, width / 2, 0]

# Update room dimensions and location in master_bedroom.json
master_bedroom_data["room"].update({
    "length": room_length,
    "width": room_width,
    "height": room_height,
    "location": calculate_room_location(room_length, room_width)
})
# Update room dimensions in master_bedroom.json
# master_bedroom_data["room"]["length"] = room_length
# master_bedroom_data["room"]["width"] = room_width
# master_bedroom_data["room"]["height"] = room_height

# Extract door and window details
door_details = output_data["DoorDetails"]
window_details = output_data["WindowDetails"]

# Function to calculate cutout details
# def calculate_cutout_common(start_point, width, height, wall_index, is_window=False, sill_height=0):
#     base_location = [
#         -(wall_thickness / 2),
#         start_point + (width / 2),
#         height / 2 + (sill_height if is_window else 0)
#     ] if wall_index == 1 else [
#         start_point + (width / 2),
#         room_width + (wall_thickness / 2),
#         height / 2 + (sill_height if is_window else 0)
#     ]
#     return {
#         "location": base_location,
#         "scale": [wall_thickness / 2, width / 2, height / 2]
#     }

# # Update floor and ceiling details
# master_bedroom_data["floor"].update({
#     "dimensions": [room_length + 0.2, room_width + 0.2, 0.001],
#     "location": [room_length / 2, room_width / 2, 0]
# })
# master_bedroom_data["ceiling"].update({
#     "scale": [room_length + 0.2, room_width + 0.2, 0.001],
#     "location": [room_length / 2, room_width / 2, room_height]
# })

# Update wall details
def calculate_wall(index, length, width, height, thickness):
    if index == 1:  # Wall 1
        return {
            "location": [-(thickness / 2), width / 2, height / 2],
            "scale": [(thickness / 2), (width / 2) + 0.1, (height / 2)],
            "rotation": [0, 0, 0]
        }
    elif index == 2:  # Wall 2
        return {
            "location": [length / 2, width + (thickness / 2), height / 2],
            "scale": [(length / 2) + 0.1, thickness / 2, height / 2],
            "rotation": [0, 0, 0]
        }
    elif index == 3:  # Wall 3
        return {
            "location": [length + (thickness / 2), width / 2, height / 2],
            "scale": [(thickness / 2), (width / 2) + 0.1, height / 2],
            "rotation": [0, 0, 0]
        }
    elif index == 4:  # Wall 4
        return {
            "location": [length / 2, -(thickness / 2), height / 2],
            "scale": [(length / 2) + 0.1, thickness / 2, height / 2],
            "rotation": [0, 0, 0]
        }

# Update wall details in master_bedroom.json
for i, wall in enumerate(master_bedroom_data["walls"], start=1):
    wall.update(calculate_wall(i, room_length, room_width, room_height, wall_thickness))


# Update cutouts for door and window
def calculate_rotation(wall_index):
    rotations = {
        1: [0, 0, 1.5708],
        2: [0, 0, 3.14159],
        3: [0, 0, 4.71239],
        4: [0, 0, 0]
    }
    return rotations.get(wall_index, [0, 0, 0])

# Update wall details in master_bedroom.json
for i, wall in enumerate(master_bedroom_data["walls"], start=1):
    wall.update(calculate_wall(i, room_length, room_width, room_height, wall_thickness))

# Update floor and ceiling details
master_bedroom_data["floor"].update({
    "dimensions": [room_length + 0.2, room_width + 0.2, 0.001],
    "location": [room_length / 2, room_width / 2, 0]
})
master_bedroom_data["ceiling"].update({
    "scale": [room_length + 0.2, room_width + 0.2, 0.001],
    "location": [room_length / 2, room_width / 2, room_height]
})

# Update cutouts for doors, windows, and openings
def calculate_cutout_common(start_point, width, height, wall_index):
    if wall_index == 1:
        return {
            "location": [-(wall_thickness / 2), start_point + (width / 2), height / 2],
            "scale": [wall_thickness / 2, width / 2, height / 2]
        }
    elif wall_index == 2:
        return {
            "location": [start_point + (width / 2), room_width + (wall_thickness / 2), height / 2],
            "scale": [width / 2, wall_thickness / 2, height / 2]
        }
    elif wall_index == 3:
        return {
            "location": [room_length + (wall_thickness / 2), start_point + (width / 2), height / 2],
            "scale": [wall_thickness / 2, width / 2, height / 2]
        }
    elif wall_index == 4:
        return {
            "location": [start_point + (width / 2), -(wall_thickness / 2), height / 2],
            "scale": [width / 2, wall_thickness / 2, height / 2]
        }

# Rotation calculation based on wall index
def calculate_rotation(wall_index):
    rotations = {
        1: [0, 0, 1.5708],
        2: [0, 0, 3.14159],
        3: [0, 0, 4.71239],
        4: [0, 0, 0]
    }
    return rotations.get(wall_index, [0, 0, 0])

# Update walls
for i, wall in enumerate(master_bedroom_data["walls"], start=1):
    wall.update(calculate_wall(i, room_length, room_width, room_height, wall_thickness))

# Update cutouts for doors and windows
master_bedroom_data["cutouts"] = []
for door in output_data["DoorDetails"]:
    cutout = calculate_cutout_common(
        door["StartPoint"] / 1000,
        float(door["DoorWidth"]) / 1000,
        float(door["DoorHeight"]) / 1000,
        door["WallNo"]
    )
    cutout.update({"name": "DoorCutout", "wall_name": f"Wall_{door['WallNo']}"})
    master_bedroom_data["cutouts"].append(cutout)

for window in output_data["WindowDetails"]:
    cutout = calculate_cutout_common(
        window["StartPoint"] / 1000,
        float(window["WindowWidth"]) / 1000,
        float(window["WindowHeight"]) / 1000,
        window["WallNo"]
    )
    cutout["location"][2] += float(window["SillHeight"]) / 1000
    cutout.update({"name": "WindowCutout", "wall_name": f"Wall_{window['WallNo']}"})
    master_bedroom_data["cutouts"].append(cutout)

# Update door and window placements
for dw, cutout in zip(master_bedroom_data["doors_windows"], master_bedroom_data["cutouts"]):
    dw.update({
        "location": cutout["location"],
        "scale": [1, 1, 1],
        "rotation": calculate_rotation(int(cutout["wall_name"][-1])),
        "wall_name": cutout["wall_name"]
    })


# Function to calculate skirting location and scale for walls
def calculate_skirting(wall_index, length, width, wall_thickness):
    if wall_index == 1:  # Skirting Wall 1
        return {
            "location": [-(wall_thickness / 2), width / 2, skirting_height ],
            "scale": [(wall_thickness / 2)+0.05, (width / 2)+0.05, skirting_height ]
        }
    elif wall_index == 2:  # Skirting Wall 2
        return {
            "location": [length / 2, width + (wall_thickness / 2), skirting_height],
            "scale": [(length / 2)+0.05, (wall_thickness / 2)+0.05, skirting_height ]
        }
    elif wall_index == 3:  # Skirting Wall 3
        return {
            "location": [length + (wall_thickness / 2), width / 2, skirting_height ],
            "scale": [(wall_thickness / 2)+0.05, (width / 2)+0.05, skirting_height ]
        }
    elif wall_index == 4:  # Skirting Wall 4
        return {
            "location": [length / 2, -(wall_thickness / 2), skirting_height ],
            "scale": [(length / 2)+0.05, (wall_thickness / 2)+0.05, skirting_height ]
        }

# Function to calculate skirting cutouts for doors, windows, and openings
def calculate_cutout(start_point, width, wall_index, is_opening=False, sill_height=0):
    """
    Calculates location and scale for skirting cutouts.
    Parameters:
        - start_point: The start point of the cutout along the wall.
        - width: The width of the door/window (for not opening) or opening.
        - wall_index: The wall number where the cutout is located.
        - is_opening: Boolean indicating if the cutout is an opening.
        - sill_height: Height of the sill for windows (default: 0).
    """
    if not is_opening:  # Door/Window scenario
        if wall_index == 1:
            location = [-(wall_thickness / 2), start_point + (width / 2), skirting_height]
            scale = [(wall_thickness / 2) +0.05, (width / 2) - 0.05, skirting_height]
        elif wall_index == 2:
            location = [start_point + (width / 2), room_width + (wall_thickness / 2), skirting_height]
            scale = [(width / 2) - 0.05, (wall_thickness / 2) + 0.05, skirting_height]
        elif wall_index == 3:
            location = [room_length + (wall_thickness / 2), start_point + (width / 2), skirting_height]
            scale = [(wall_thickness / 2) + 0.05, (width / 2) - 0.05, skirting_height]
        elif wall_index == 4:
            location = [start_point + (width / 2), -(wall_thickness / 2), skirting_height]
            scale = [(width / 2) -0.05, (wall_thickness / 2) + 0.05, skirting_height]
    else:  # Opening scenario
        if wall_index == 1:
            location = [-(wall_thickness / 2), start_point + (width / 2), skirting_height]
            scale = [(wall_thickness / 2) + 0.05, (width / 2) , skirting_height]
        elif wall_index == 2:
            location = [start_point + (width / 2), room_width + (wall_thickness / 2), skirting_height]
            scale = [(width / 2) , (wall_thickness / 2) + 0.05, skirting_height]
        elif wall_index == 3:
            location = [room_length + (wall_thickness / 2), start_point + (width / 2), skirting_height]
            scale = [(wall_thickness / 2) + 0.05, (width / 2), skirting_height]
        elif wall_index == 4:
            location = [start_point + (width / 2), -(wall_thickness / 2), skirting_height]
            scale = [(width / 2) , (wall_thickness / 2) + 0.05, skirting_height]
    return {"location": location, "scale": scale}

# Update skirting fragments and cutouts
for i, skirting in enumerate(master_bedroom_data["skirtings"], start=1):
    skirting.update(calculate_skirting(i, room_length, room_width, wall_thickness))

    # Add cutouts for doors, windows, and openings
    skirting["cutouts"] = []
    for door in output_data["DoorDetails"]:
        if door["WallNo"] == i:
            cutout = calculate_cutout(
                float(door["StartPoint"]) / 1000,
                float(door["DoorWidth"] )/ 1000,
                door["WallNo"],
                is_opening=False
            )
            skirting["cutouts"].append(cutout)
    for window in output_data["WindowDetails"]:
        if window["WallNo"] == i:
            cutout = calculate_cutout(
                float(window["StartPoint"]) / 1000,
                float(window["WindowWidth"]) / 1000,
                window["WallNo"],
                is_opening=False,
                sill_height=float(window["SillHeight"]) / 1000
            )
            skirting["cutouts"].append(cutout)
    for opening in output_data.get("Openings", []):  # If openings exist in the data
        if opening["WallNo"] == i:
            cutout = calculate_cutout(
                float(opening["StartPoint"]) / 1000,
                float(opening["Width"]) / 1000,
                opening["WallNo"],
                is_opening=True
            )
            skirting["cutouts"].append(cutout)

# Save the updated JSON
with open(output_file, "w") as file:
    json.dump(master_bedroom_data, file, indent=4)

print(f"Updated JSON saved as {output_file}")
