def get_input_data(filename: str):
    with open(filename) as f:
        return list(map(str.strip, f.readlines()))


def solution_part_1(input_data: list[list[str]]):
    priority_sum = 0
    for rucksack in input_data:
        mid = len(rucksack.strip()) // 2
        left, right = rucksack.strip()[:mid], rucksack.strip()[mid:]
        common = set(left).intersection(set(right)).pop()
        if common.islower():
            priority_sum += (ord(common) - 96)
        else:
            priority_sum += (ord(common) - 64 + 26)
    return priority_sum

def solution_part_2(input_data: list[list[str]]):
    badge_sum = 0
    for i in range(0, len(input_data), 3):
        r_1, r_2, r_3 = input_data[i], input_data[i + 1], input_data[i + 2]
        badge = set(r_1).intersection(set(r_2)).intersection(set(r_3)).pop()
        if badge.islower():
            badge_sum += (ord(badge) - 96)
        else:
            badge_sum += (ord(badge) - 64 + 26)
    return badge_sum


if __name__ == "__main__":
    print(solution_part_1(get_input_data("puzzle_input.txt")))
    print(solution_part_2(get_input_data("puzzle_input.txt")))