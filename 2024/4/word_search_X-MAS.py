# word_search_X-MAS.py
def main():
    # read values in
    with open('input.txt', 'r') as file:
        values = file.read()
    # split the values into a two-dimensional array
    values = [list(line) for line in values.split('\n') if line]
    x = 0
    y = 0
    number_of_xmases = 0
    letters_in_x = []
    for y in range(len(values)):
        for x in range(len(values[y])):
            if values[y][x] == 'A':
                #up-left
                if x >= 1 and y >= 1:
                    letters_in_x.append(values[y-1][x-1])
                    #up-right
                    if x <= len(values[y])-2 and y >= 1:
                        letters_in_x.append(values[y-1][x+1])
                        #down-left
                        if x >= 1 and y <= len(values)-2:
                            letters_in_x.append(values[y+1][x-1])
                            #down-right
                            if x <= len(values[y])-2 and y <= len(values)-2:
                                letters_in_x.append(values[y+1][x+1])
                                #check for X-MAS
                                if (letters_in_x.count('M') == 2 and 
                                    letters_in_x.count('S') == 2 and 
                                    letters_in_x != ['M', 'S', 'S', 'M'] and 
                                    letters_in_x != ['S', 'M', 'M', 'S']):
                                    number_of_xmases += 1
                letters_in_x = []
    print(f"Number of XMASes found: {number_of_xmases}")
if __name__ == "__main__":
    main()