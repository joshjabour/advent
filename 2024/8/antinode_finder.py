# antinode_finder.py
import math

def main():    # read values in
    with open('input.txt', 'r') as file:
        grid = file.read()
    
    # split the values into a two-dimensional array
    grid = grid.split('\n')
    grid = [list(x) for x in grid]
    
    # find the non-dots and save their positions
    char_positions = {}  # Dictionary to store positions for each character
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != '.':
                char = grid[y][x]
                if char not in char_positions:
                    char_positions[char] = []  # Initialize empty list for new characters
                char_positions[char].append((x, y))

    antinode_positions = {}  # Dictionary to store antinode positions for each character
    print("there are " + str(len(char_positions)) + " characters")
    debug_counter = 0
    for char in char_positions:
        antinode_positions[char] = []  # Initialize empty list for each character
        debug_counter += 1
        if debug_counter % 10 == 0 and debug_counter != 0:
            print("debug_counter: " + str(debug_counter))
        for pos1 in char_positions[char]:
            for pos2 in char_positions[char]:
                if pos1 != pos2:

                    # get the direction of the vector between the two positions
                    x_dir = pos2[0] - pos1[0]  # Difference in x direction
                    y_dir = pos2[1] - pos1[1]  # Difference in y direction

                    if x_dir > 0:
                        x_dir = 1
                    elif x_dir < 0:
                        x_dir = -1

                    if y_dir > 0:
                        y_dir = 1
                    elif y_dir < 0:
                        y_dir = -1

                    # Calculate the differences in x and y coordinates
                    x_diff = abs(pos2[0] - pos1[0])  # Difference in x direction
                    y_diff = abs(pos2[1] - pos1[1])  # Difference in y direction
                    
                    if x_dir == 1:
                        antinode_x = pos2[0] + x_diff
                    elif x_dir == -1:
                        antinode_x = pos2[0] - x_diff

                    if y_dir == 1:
                        antinode_y = pos2[1] + y_diff
                    elif y_dir == -1:
                        antinode_y = pos2[1] - y_diff

                    # check if the antinode is within the grid
                    if antinode_x >= 0 and antinode_x < len(grid[0]) and antinode_y >= 0 and antinode_y < len(grid):
                        antinode_positions[char].append((antinode_x, antinode_y))

    # count the number of antinode locations
    antinode_positions_set = set()
    for char in antinode_positions:
        for pos in antinode_positions[char]:
            antinode_positions_set.add(pos)

    print(len(antinode_positions_set))

if __name__ == "__main__":
    main()