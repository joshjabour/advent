# check_safety.py

def main():
    # read values in
    with open('input.txt', 'r') as file:
        values = file.read()
    # split values into levels
    levels = values.split("\n")
    print("length =", len(levels))
    number_of_safe_levels = 0
    for level in levels:
        # split level into values
        values = level.split()
        is_safe = True
        # check values in each level
        for i in range(len(values)):
            current_value = int(values[i])
            next_value = int(values[i+1]) if len(values) > i + 1 else None
            # check whether going up or down
            if i == 0:
                if next_value is not None:
                    if current_value < next_value:
                        is_going_up = True
                    elif current_value > next_value:
                        is_going_up = False                
                    else:
                        is_safe = False
                        break
                else:
                    break
            # check if the difference is safe
            if next_value is not None:
                if is_going_up:
                    difference = next_value - current_value
                else:
                    difference = current_value - next_value
                if difference > 3 or difference <= 0:
                    is_safe = False
                    break
        if is_safe:
            number_of_safe_levels += 1
    print(number_of_safe_levels)
if __name__ == "__main__":
    main()