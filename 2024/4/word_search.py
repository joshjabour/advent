# word_search.py
def main():
    # read values in
    with open('input.txt', 'r') as file:
        values = file.read()
    # split the values into a two-dimensional array
    values = [list(line) for line in values.split('\n') if line]
    x = 0
    y = 0
    number_of_xmases = 0
    for y in range(len(values)):
        for x in range(len(values[y])):
            if values[y][x] == 'X':
                #left
                if x >= 3 and values[y][x-1] == 'M' and values[y][x-2] == 'A' and values[y][x-3] == 'S':
                    number_of_xmases += 1
                    # print(f"l  found at {x}, {y}")
                #right
                if x <= len(values[y])-4 and values[y][x+1] == 'M' and values[y][x+2] == 'A' and values[y][x+3] == 'S':
                    number_of_xmases += 1
                    # print(f"r  found at {x}, {y}")
                #up
                if y >= 3 and values[y-1][x] == 'M' and values[y-2][x] == 'A' and values[y-3][x] == 'S':
                    number_of_xmases += 1
                    # print(f"u  found at {x}, {y}")
                #down
                if y <= len(values)-4 and values[y+1][x] == 'M' and values[y+2][x] == 'A' and values[y+3][x] == 'S':
                    number_of_xmases += 1
                    # print(f"d  found at {x}, {y}")
                #up-left
                if x >= 3 and y >= 3 and values[y-1][x-1] == 'M' and values[y-2][x-2] == 'A' and values[y-3][x-3] == 'S':
                    number_of_xmases += 1
                    # print(f"ul found at {x}, {y}")
                #up-right
                if x <= len(values[y])-4 and y >= 3 and values[y-1][x+1] == 'M' and values[y-2][x+2] == 'A' and values[y-3][x+3] == 'S':
                    number_of_xmases += 1
                    # print(f"ur found at {x}, {y}")
                #down-left
                if x >= 3 and y <= len(values)-4 and values[y+1][x-1] == 'M' and values[y+2][x-2] == 'A' and values[y+3][x-3] == 'S':
                    number_of_xmases += 1
                    # print(f"dl found at {x}, {y}")
                #down-right
                if x <= len(values[y])-4 and y <= len(values)-4 and values[y+1][x+1] == 'M' and values[y+2][x+2] == 'A' and values[y+3][x+3] == 'S':
                    number_of_xmases += 1
                    # print(f"dr found at {x}, {y}")
    print(f"Number of XMASes found: {number_of_xmases}")
if __name__ == "__main__":
    main()