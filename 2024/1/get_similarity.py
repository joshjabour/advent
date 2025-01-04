# get_similarity.py

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

    # calculate sum of similarity
    similarity_sum = 0
    for n in values_left_side:
        similarity_sum += int(n) * values_right_side.count(n)
    print(similarity_sum)
if __name__ == "__main__":
    main()