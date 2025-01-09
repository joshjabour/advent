# check_safety.py

def is_level_safe(reducedValues):
    is_safe = True
    # check values in each level
    for i in range(len(reducedValues)):
        current_value = int(reducedValues[i])
        next_value = int(reducedValues[i+1]) if len(reducedValues) > i + 1 else None
        # check whether going up or down
        if i == 0:
            if current_value < next_value:
                is_going_up = True
            elif current_value > next_value:
                is_going_up = False
            else:
                is_safe = False
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
    return is_safe

def main():
    # read values in
    with open('input.txt', 'r') as file:
        values = file.read()
    # split values into levels
    levels = values.split("\n")
    number_of_safe_levels = 0
    for level in levels:
        is_safe = False
        i = 0
        # split level into values
        values = level.split()
        while is_safe == False and i < len(values):
            # level with one value removed
            reducedValues = values[:i] + values[i+1:]
            is_safe = is_level_safe(reducedValues)
            i += 1
        if is_safe:
            number_of_safe_levels += 1
    print(number_of_safe_levels)
if __name__ == "__main__":
    main()