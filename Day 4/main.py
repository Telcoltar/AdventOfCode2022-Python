class Section:
    
    def __init__(self, lower_bound: int, higher_bound: int) -> None:
        self.lower_bound = lower_bound
        self.higher_bound = higher_bound

    def __str__(self) -> str:
        return f"{self.lower_bound}-{self.higher_bound}"

    def __eq__(self, __o: object) -> bool:
        if (isinstance(__o, Section)):
            return self.lower_bound == __o.lower_bound and self.higher_bound == __o.higher_bound
        return False

    def has_intersection_with(self, other: "Section"):
        lower_bound = max(self.lower_bound, other.lower_bound)
        higher_bound = min(self.higher_bound, other.higher_bound)
        return lower_bound <= higher_bound

    @classmethod
    def intersection(cls, first: "Section", second: "Section"):
        lower_bound = max(first.lower_bound, second.lower_bound)
        higher_bound = min(first.higher_bound, second.higher_bound)
        if (lower_bound > higher_bound):
            raise ValueError("No intersection")
        return cls(lower_bound, higher_bound)

def get_input_data(filename: str):
    section_list: list[tuple[Section, Section]] = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f.readlines():
            first, second = line.split(",")
            first = Section(*map(int, first.split("-")))
            second = Section(*map(int, second.split("-")))
            section_list.append((first, second))
    return section_list


def solution_part_1(section_list: list[tuple[Section, Section]]):
    full_overlaps = 0
    for first, second in section_list:
        if first.has_intersection_with(second):
            intersection = Section.intersection(first, second)
            if intersection == first or intersection == second:
                full_overlaps += 1
    return full_overlaps

def solution_part_2(section_list: list[tuple[Section, Section]]):
    oveerlaps = 0
    for first, second in section_list:
        if first.has_intersection_with(second):
            oveerlaps += 1
    return oveerlaps


if __name__ == "__main__":
    print(solution_part_1(get_input_data("puzzle_input.txt")))
    print(solution_part_2(get_input_data("puzzle_input.txt")))