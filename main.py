# Step 1: Read INPUT.txt and extract data

# Variables to store data
ink_matrix = []  # 2D matrix of dies
orientation = 0
good_die_code = ''
bad_die_code = ''
invalid_die_code = ''

# Open the file and read it
with open("INPUT.txt", "r") as file:
    for line in file:
        line = line.strip()  # remove extra spaces and \n

        # Read orientation
        if line.startswith("ORIENTATION:"):
            orientation = int(line.split(":")[1])

        # Read die codes
        elif line.startswith("GOOD_DIE:"):
            good_die_code = line.split(":")[1]

        elif line.startswith("BAD_DIE:"):
            bad_die_code = line.split(":")[1]

        elif line.startswith("INVALID_DIE:"):
            invalid_die_code = line.split(":")[1]

        # Read the die grid (ROWDATA)
        elif line.startswith("ROWDATA:"):
            row_values = line.replace("ROWDATA:", "").strip().split()
            ink_matrix.append(row_values)

# Print to confirm
print("Orientation:", orientation)
print("Good Die Code:", good_die_code)
print("Bad Die Code:", bad_die_code)
print("Invalid Die Code:", invalid_die_code)
print("\nInk Matrix:")
for row in ink_matrix:
    print(row)
# Step 2: Read MATRIX.csv (0 = invalid, 1 = valid)

matrix = []  # Will hold the 0/1 matrix

with open("MATRIX.csv", "r") as file:
    for line in file:
        row = line.strip().split(",")  # Split on commas
        matrix.append(row)

# Print to confirm
print("\nMatrix:")
for row in matrix:
    print(row)
# Step 3: Rotate Ink Matrix if needed

# Function to rotate a 2D matrix clockwise
def rotate_clockwise(matrix):
    # Transpose + reverse rows = rotate 90 degrees
    rotated = [list(row) for row in zip(*matrix[::-1])]
    return rotated

# Apply rotation based on orientation value
# 0 = no rotation, 90 = rotate once, 180 = twice, 270 = three times
if orientation == 90:
    ink_matrix = rotate_clockwise(ink_matrix)
elif orientation == 180:
    ink_matrix = rotate_clockwise(rotate_clockwise(ink_matrix))
elif orientation == 270:
    ink_matrix = rotate_clockwise(rotate_clockwise(rotate_clockwise(ink_matrix)))

# Confirm final orientation
print("\nInk Matrix after orientation adjustment:")
for row in ink_matrix:
    print(row)
# Step 4: Apply Matrix over Ink file and prepare final result

final_matrix = []  # Resulting wafer map
good_die_count = 0
bad_die_count = 0

for i in range(len(matrix)):
    row = []
    for j in range(len(matrix[0])):
        if matrix[i][j] == '0':
            # Invalid die in matrix
            row.append('000')
        else:
            # Valid die → take value from ink_matrix
            die_value = ink_matrix[i][j]

            # Count good and bad dies
            if die_value == good_die_code:
                good_die_count += 1
            elif die_value == bad_die_code:
                bad_die_count += 1

            row.append(die_value)
    final_matrix.append(row)

# Confirm result
print("\nFinal Output Matrix:")
for row in final_matrix:
    print(row)

print("\nNumber of Good Dies:", good_die_count)
print("Number of Bad Dies:", bad_die_count)
# Step 5: Write output to file

output_filename = "M1T1.txt"

with open(output_filename, "w") as file:
    # Write die counts
    file.write(f"NO OF GOOD DIES:{good_die_count}\n")
    file.write(f"NO OF BAD DIES:{bad_die_count}\n")

    # Write final matrix
    for row in final_matrix:
        row_string = " ".join(row)
        file.write(f"ROWDATA:{row_string}\n")

print(f"\nOutput written to {output_filename}")

