from collections import defaultdict, deque

def get_input_data(filename: str):
    stacks: defaultdict[int, deque[str]] = defaultdict(deque)
    moves: list[(int, (int, int))] = []

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        stack_input = []
        move_input = []
        part_2: bool = False
        for line in lines:
            if line.strip() == "":
                part_2 = True
                continue
            if part_2:
                move_input.append(line.strip())
            else:
                stack_input.append(line[:-1])

        for line in stack_input[:-1]:
            for i in range(0, len(line) - 2, 4):
                current_stack_element = line[i: i + 3].strip()
                if current_stack_element != "":
                    stacks[i // 4].appendleft(current_stack_element[1])
        
        for line in move_input:
            parts = line.split()
            moves.append((int(parts[1]), (int(parts[3]) - 1, int(parts[5]) - 1)))

        return stacks, moves

def solution_part_1(stacks: dict[int, deque[str]], moves: list[(int, (int, int))]):
    for move in moves:
        for _ in range(move[0]):
            stacks[move[1][1]].append(stacks[move[1][0]].pop())
    top_elements: list[str] = []
    for i in range(len(stacks)):
        top_elements.append(stacks[i].pop())
    return "".join(top_elements)

def solution_part_2(stacks: dict[int, deque[str]], moves: list[(int, (int, int))]):
    tmp_stack: deque[str] = deque()
    for move in moves:
        for _ in range(move[0]):
            tmp_stack.append(stacks[move[1][0]].pop())
        for _ in range(move[0]):
            stacks[move[1][1]].append(tmp_stack.pop())
    top_elements: list[str] = []
    for i in range(len(stacks)):
        top_elements.append(stacks[i].pop())
    return "".join(top_elements)

if __name__ == "__main__":
    print(solution_part_1(*get_input_data("puzzle_data.txt")))
    print(solution_part_2(*get_input_data("puzzle_data.txt")))