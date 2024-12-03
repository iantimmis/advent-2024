import re

def get_example_data():
    return "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

def read_input_data():
    with open("day3_data.txt", 'r', encoding='utf-8') as file:
            return file.read()

def solve_part_1(data: str):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, data)
    valid_expressions = [(int(x), int(y)) for x, y in matches] 
    result = 0
    for (x, y) in valid_expressions:
        result += x * y
    return result

def solve_part_2(data):
    instructions = []

    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.finditer(pattern, data)
    for match in matches:
        start = match.start()
        x, y = match.groups()
        instructions.append((start, (int(x), int(y))))

    pattern = r'do\(\)'
    matches = re.finditer(pattern, data)
    for match in matches:
        start = match.start()
        instructions.append((start, True))

    pattern = r'don\'t\(\)'
    matches = re.finditer(pattern, data)
    for match in matches:
        start = match.start()
        instructions.append((start, False))

    sorted_instructions = sorted(instructions, key=lambda x: x[0])

    result = 0
    enabled = True
    for instruction in sorted_instructions:
        if type(instruction[1]) == tuple:
            if enabled:
                result += instruction[1][0] * instruction[1][1]
        else:
            enabled = instruction[1]
            
    return result

if __name__ == "__main__":
    data = read_input_data()

    answer1 = solve_part_1(data)
    print(f"\nDay 3 (Part 1) solution: {answer1}")    

    answer2 = solve_part_2(data)
    print(f"\nDay 3 (Part 2) solution: {answer2}")
