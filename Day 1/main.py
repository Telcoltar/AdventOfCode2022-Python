from typing import List


def read_input(file: str):
    print(f"Open file {file}.")
    with open(file, "r") as f:
        calories: List[List[int]] = []
        current_elf: List[int] = []
        for line in f.readlines():
            if line.strip() == "":
                calories.append(current_elf)
                current_elf = []
                continue
            current_elf.append(int(line.strip()))
        calories.append(current_elf)
    return calories


def solution_part_1(input_data: List[List[int]]):
    return highest_k_sum(input_data, 1)


def solution_part_2(input_data: List[List[int]]):
    return sum(highest_k_sum(input_data, 3))


def highest_k_sum(input_data: List[List[int]], k: int):
    calories_sum_per_elf = []
    for calories_per_elf in input_data:
        calories_sum_per_elf.append(sum(calories_per_elf))
    calories_sum_per_elf.sort(reverse=True)
    return calories_sum_per_elf[:k]


if __name__ == "__main__":
    print(solution_part_1(read_input("input_data.txt")))
    print(solution_part_2(read_input("input_data.txt")))
