# multiplier.py
import re
def main():
    # read values in
    with open('input.txt', 'r') as file:
        values = file.read()
    output = 0
    matches = re.findall("mul\(\d{1,3},\d{1,3}\)", values)
    for match in matches:
        #get the numbers from the string
        numbers = re.findall("\d{1,3}", match)
        #multiply the numbers
        result = int(numbers[0]) * int(numbers[1])
        print(result)
        output += result
    print(output)
if __name__ == "__main__":
    main()