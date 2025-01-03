# get_distances.py

def main():
    # read values in
    with open('Values.txt', 'r') as file:
        values = file.read()
    # split values into list
    values = values.split()

    # split values into left side and right side
    is_left_side = True
    values_left_side = []
    values_right_side = []
    for value in values:
        if is_left_side:
            values_left_side.append(value)
            is_left_side = False
        else:
            values_right_side.append(value)
            is_left_side = True

    # sort left and right sides
    values_left_side.sort()
    values_right_side.sort()
    
    # calculate sum of distances
    distance_sum = 0
    for n in range(len(values_left_side)):
        distance_sum += abs(int(values_left_side.pop())-int(values_right_side.pop()))
    print(distance_sum)
if __name__ == "__main__":
    main()