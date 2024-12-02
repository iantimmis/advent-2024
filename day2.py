def get_example_data():
    return [[7,6,4,2,1], [1,2,7,8,9], [9,7,6,2,1], [1,3,2,4,5], [8,6,4,4,1], [1,3,6,7,9]]

def read_input_data():
    data = []

    with open("day2_data.txt", "r") as file:
        for line in file:
            data.append(list(map(int, line.split())))

    return data

def solve_part_1(data):
    def get_sign(delta):
        return 1 if delta > 0 else 0 if delta == 0 else -1
    
    safe_reports = 0

    for report in data:
        sign = None
        prev = None
        
        for (i, level) in enumerate(report):
            if prev is None:
                prev = level
                continue
            
            delta = level - prev
            delta_sign = get_sign(delta)

            if sign is None:
                sign = delta_sign
                
            if delta_sign == 0 or sign != delta_sign:
                break

            if abs(delta) < 1 or abs(delta) > 3:
                break

            prev = level

            if i == len(report) - 1:
                safe_reports += 1

    return safe_reports


def solve_part_2(data):
    def get_sign(delta):
        return 1 if delta > 0 else 0 if delta == 0 else -1
    
    def check_report(report):
        sign = None
        prev = None
        
        for (i, level) in enumerate(report):
            if prev is None:
                prev = level
                continue
            
            delta = level - prev
            delta_sign = get_sign(delta)

            if sign is None:
                sign = delta_sign
                
            if delta_sign == 0 or sign != delta_sign:
                return False

            if abs(delta) < 1 or abs(delta) > 3:
                return False

            prev = level

            if i == len(report) - 1:
                return True
            
    safe_reports = 0

    for (i, report) in enumerate(data):
        safe = check_report(report)

        if not safe:
            for level in range(len(report)):
                report_copy = report[:]
                report_copy.pop(level)
                safe = check_report(report_copy)
                if safe:
                    break
        if safe:
            safe_reports += 1

    return safe_reports

if __name__ == "__main__":
    data = read_input_data()

    answer1 = solve_part_1(data)
    print(f"Day 2 (Part 1) solution: {answer1}")    

    answer2 = solve_part_2(data)
    print(f"Day 2 (Part 2) solution: {answer2}")
