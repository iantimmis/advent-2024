def get_example_data():
    return [3,4,2,1,3,3], [4,3,5,3,9,3]

def read_input_data():
    location_ids_group_1 = []
    location_ids_group_2 = []

    with open("day1_data.txt", "r") as file:
        for line in file:
            group_1_id, group_2_id = map(int, line.split())
            location_ids_group_1.append(group_1_id)
            location_ids_group_2.append(group_2_id)
    return location_ids_group_1, location_ids_group_2

def solve_part_1(location_ids_group_1, location_ids_group_2):
    # Distance between sorted groups
    location_ids_group_1.sort()
    location_ids_group_2.sort()

    distances_between_groups = [
        abs(g1_id - g2_id)
        for (g1_id, g2_id) in zip(location_ids_group_1, location_ids_group_2)
    ]

    return sum(distances_between_groups)

def solve_part_2(group1_ids, group2_ids):
    similarity_score = 0

    group2_id_counts = {}
    for g2_id in group2_ids:
        group2_id_counts[g2_id] = group2_id_counts.get(g2_id, 0) + 1

    for g1_id in group1_ids:
        similarity_score += group2_id_counts.get(g1_id, 0) * g1_id

    return similarity_score

if __name__ == "__main__":
    group1_ids, group2_ids = read_input_data()

    answer1 = solve_part_1(group1_ids, group2_ids)
    print(f"Day 1 (Part 1) solution: {answer1}")
    

    answer2 = solve_part_2(group1_ids, group2_ids)
    print(f"Day 1 (Part 2) solution: {answer2}")