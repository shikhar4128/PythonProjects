import random

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "

def parse_input(num):
    if num.strip() in ("1","2","3","4","5","6"):
        return int(num)
    else:
        print("Please enter a valid number between 1 to 6 \n")
        raise SystemExit(1)

def roll_dice(num_dice):
    roll_input=[]
    for i in range(num_dice):
        roll=random.randint(1,6)
        roll_input.append(roll)
    return roll_input

def generate_dice_faces_diagram(dice_values):
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])

    # Generate a list containing the dice faces rows
    dice_faces_rows = []
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)

    # Generate header with the word "RESULTS" centered
    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram

#App's code main block:
#1. Get and validate user input
num_dice_input=input("How many dice you want to roll? [1-6]: ")
num_dice=parse_input(num_dice_input)
# 2. Roll the dice
roll_results=roll_dice(num_dice)
# 3. Generate the ASCII diagram of dice faces
dice_face_diagram = generate_dice_faces_diagram(roll_results)
# 4. Display the diagram
print(f"\n{dice_face_diagram}")

