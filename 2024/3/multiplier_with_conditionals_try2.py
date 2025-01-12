# multiplier_with_conditionals_try2.py
import re
def main():
    # read values in
    with open('input.txt', 'r') as file:
        values = file.read()
    output = 0
    # find all the mul()s
    matches = re.findall("mul\(\d{1,3},\d{1,3}\)", values)

    #for each mul() match, find the index of that match and look backward to see if there was a do() or don't()
    #if there was a don't(), then we don't want to include that mul() in the calculation
    #if there was a do(), then we do want to include that mul() in the calculation
    #if there was no don't() or do(), then we want to include that mul() in the calculation
    filtered_matches = []
    for match in matches:
        index = values.find(match)
        before_match = values[:index]
        if "don't()" in before_match:
            last_dont = before_match.rfind("don't()")
        else:
            last_dont = -1
        if "do()" in before_match:
            last_do = before_match.rfind("do()")
        else:
            last_do = -1

        if last_do > last_dont:
            filtered_matches.append(match)
        elif last_dont == -1 and last_do == -1:
            filtered_matches.append(match)

    matches = filtered_matches



    # calculate
    for match in filtered_matches:
        #get the numbers from the string
        numbers = re.findall("\d{1,3}", match)
        #multiply the numbers
        result = int(numbers[0]) * int(numbers[1])
        #print(result)
        output += result
        print(match)
    print(output) # 222819041 was too high. 72954280 was too low. 73328706 was too low.
if __name__ == "__main__":
    main()