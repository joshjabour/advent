# multiplier_with_conditionals_try1.py
import re
def main():
    # read values in
    with open('input.txt', 'r') as file:
        values = file.read()
    output = 0
    
    # find strings between do() and don't()
    # Define conditionals
    start_string = "do()" 
    end_string = "don't()" 
    
    # Create the regex pattern 
    pattern = rf"{re.escape(start_string)}(.*?){re.escape(end_string)}"
    
    # Find all matches 
    matches = re.findall(pattern, values)

    # Find the first part of the string until the first do()
    first_part = values[:values.find(start_string)]

    # create one string joining all matches and first_part
    active_values = str(first_part) + "".join(matches)
    # find all the mul()s and calculate
    matches = re.findall("mul\(\d{1,3},\d{1,3}\)", active_values)
    for match in matches:
        #get the numbers from the string
        numbers = re.findall("\d{1,3}", match)
        #multiply the numbers
        result = int(numbers[0]) * int(numbers[1])
        #print(result)
        output += result
        print(match)
    print(output) # 222819041 was too high. 72954280 was too low. 73328706 was too low. This misses some sections, so I reworked this in try2.
if __name__ == "__main__":
    main()