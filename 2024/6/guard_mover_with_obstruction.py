# guard_mover_with_obstruction.py
def main():
    # get carat position
    def get_carat_position():
        carat_position = None
        for row in range(len(grid)):
            try:
                carat_position = [row, grid[row].index('^')]
                break
            except ValueError:
                pass
        return carat_position

    def simulate_movement_with_barrier(start_row, start_col, barrier_row, barrier_col, start_direction):
        # Create a copy of the grid for simulation
        sim_grid = [row[:] for row in grid]
        if barrier_row is not None and barrier_col is not None:
            sim_grid[barrier_row][barrier_col] = '#'
        
        row, col = start_row, start_col
        direction = start_direction
        path_history = []  # Change to list to track sequence
        visited_states = set()  # Track position+direction states
        
        while True:
            orig_row, orig_col = row, col
            if direction == 0:
                row -= 1
            elif direction == 1:
                col += 1
            elif direction == 2:
                row += 1
            elif direction == 3:
                col -= 1
            
            # Check if we've hit the edge - this means no loop
            if row < 0 or row >= len(sim_grid) or col < 0 or col >= len(sim_grid[row]):
                return False
            
            current_state = (row, col, direction)
            
            # If we've seen this state before, check if it's a true loop
            if current_state in visited_states:
                # Find where this state occurred in our path
                previous_index = path_history.index(current_state)
                # Check if we're truly stuck in a loop by verifying
                # that we can't escape this sequence of moves
                loop_sequence = path_history[previous_index:]
                all_positions = {(r, c) for r, c, d in loop_sequence}
                
                # If the loop sequence contains positions that could lead out,
                # it's not a true trap
                for r, c in all_positions:
                    if (r == 0 or r == len(sim_grid)-1 or 
                        c == 0 or c == len(sim_grid[0])-1):
                        return False
                return True
            
            # Check if we hit a barrier
            if sim_grid[row][col] == '#':
                direction = (direction + 1) % 4
                row, col = orig_row, orig_col
            else:
                visited_states.add(current_state)
                path_history.append(current_state)
                sim_grid[row][col] = '^'
                sim_grid[orig_row][orig_col] = 'X'

    # read values in
    with open('input.txt', 'r') as file:
        grid = file.read()
    
    # split the values into a two-dimensional array
    grid = grid.split('\n')
    grid = [list(x) for x in grid]

    carat_position = get_carat_position()
    count = 0  # Initialize count
    loop_count = 0  # Initialize loop counter
    found_loop_positions = set()  # Track positions where loops were found
    path_positions = set()  # Track the actual path the guard takes

    if carat_position:
        row, col = carat_position
        direction = 0  # 0 = up, 1 = right, 2 = down, 3 = left
        
        while True:
            # Track the actual path
            path_positions.add((row, col))
            
            # Check if placing a barrier in front would create a loop
            next_row, next_col = row, col
            if direction == 0:
                next_row -= 1
            elif direction == 1:
                next_col += 1
            elif direction == 2:
                next_row += 1
            elif direction == 3:
                next_col -= 1
            
            if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                # Only check for loops if:
                # 1. The position hasn't been checked before
                # 2. The position is not already part of our path
                # 3. It's a valid position to place a barrier (. or X)
                if (grid[next_row][next_col] in ['.', 'X'] and 
                    (next_row, next_col) not in found_loop_positions and 
                    (next_row, next_col) not in path_positions):
                    if simulate_movement_with_barrier(row, col, next_row, next_col, direction):
                        loop_count += 1
                        found_loop_positions.add((next_row, next_col))
                        #print(f"Potential loop found at ({next_row}, {next_col})")
            
            # Move the guard
            orig_row, orig_col = row, col
            if direction == 0:
                row -= 1
            elif direction == 1:
                col += 1
            elif direction == 2:
                row += 1
            elif direction == 3:
                col -= 1
            
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]):
                break
                
            if grid[row][col] == '#':
                direction = (direction + 1) % 4
                row, col = orig_row, orig_col
            else:
                if grid[row][col] == '.':
                    count += 1
                grid[row][col] = '^'
                grid[orig_row][orig_col] = 'X'
    
    print(f"Total . covered: {count}")
    print(f"Total potential loops found: {loop_count}") # 1478 is too high

if __name__ == "__main__":
    main()