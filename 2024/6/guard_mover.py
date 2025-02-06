# guard_mover.py
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

    # read values in
    with open('input.txt', 'r') as file:
        grid = file.read()
    
    # split the values into a two-dimensional array
    grid = grid.split('\n')
    grid = [list(x) for x in grid]

    carat_position = get_carat_position()

    # Count the initial position
    count = 1
    direction = 0 # 0 = up, 1 = right, 2 = down, 3 = left
    if carat_position:
        row, col = carat_position
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
            print("starting from ", [orig_row, orig_col], "attempt move to ", [row, col])
            print(grid)
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]):
                break
            if grid[row][col] == '#':
                direction = (direction + 1) % 4
                row, col = orig_row, orig_col
            else:
                if grid[row][col] == '.':
                    count += 1
                grid[row][col] = '^'
                grid[orig_row][orig_col] = 'X' # reset the original position to a X so we know if we covered it
    print(f"Total . covered: {count}")
if __name__ == "__main__":
    main()