# operator_checker.py
from itertools import product
import operator

# Dictionary mapping operator symbols to functions
ops = {
    '+': operator.add,
    '*': operator.mul,
    '-': operator.sub,
    '/': operator.truediv
}

def generate_operator_list_combos(length):
    # All possible combinations of + and * operators
    operators = ['+', '*']
    # Generate all possible combinations for the given length
    combinations = product(operators, repeat=length)
    # Convert to list of lists for easier handling
    return list(combinations)

def main():    # read values in
    total = 0
    with open('input.txt', 'r') as file:
        equations = file.read()
    
    # split the values into arrays per row
    equations = equations.split('\n')
    for equation in equations:
        # split the equation into parts
        parts = equation.split(':')
        test_value = parts[0]
        numerals = parts[1].strip().split(' ')
        numerals = [int(num) for num in numerals]
        # generate all combinations of '+' and '*' as the operators
        operator_combos = generate_operator_list_combos(len(numerals) - 1)
        for operator_combo in operator_combos:
            #calculate the value of the equation using all operators and numerals
            value = calculate_equation(numerals, operator_combo)
            # print(f"Test value = {test_value}")
            # print(f"Value = {value}")
            # print(f"Numerals = {numerals}")
            # print(f"Operator combo = {operator_combo}")
            if value == int(test_value):
                total += value
                break
    print(f"Total = {total}")

def calculate_equation(numerals, operator_combo):
    #calculate the value of the equation using all operators and numerals
    value = numerals[0]
    for i in range(len(operator_combo)):
        value = ops[operator_combo[i]](value, numerals[i+1])
    return value

if __name__ == "__main__":
    main()