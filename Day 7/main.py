from typing import Iterable, Optional
from collections import deque

class Node:

    def __init__(self) -> None:
        self.files: list[(int, str)] = []
        self.parent: Optional["Node"] = "/"
        self.children: dict[str, "Node"] = {}
        self.size = 0

def get_input_data(filename: str):
    with open(filename) as f:
        return map(lambda line: line.strip(), f.readlines())

def solution_part_1(input_data: Iterable[str]):
    root = build_tree(input_data)
    return sum(node.size for node in directories_le_threshold(100_000, root))

def solution_part_2(input_data: Iterable[str]):
    root = build_tree(input_data)
    total_space = 70_000_000
    update_size = 30_000_000
    used_space = root.size
    free_space = total_space - used_space
    needed_space = update_size - free_space
    nodes_with_enough_space = directories_ge_threshold(needed_space, root)
    nodes_with_enough_space.sort(key=lambda node: node.size)
    return nodes_with_enough_space[0].size


def build_tree(input_data: Iterable[str]) -> Node:
    next(input_data)
    root = Node()
    current = root
    for line in input_data:
        # print(line, current.files, current.parent)
        if line.startswith("dir"):
            dir_name = line.split()[1].strip()
            new_node = Node()
            new_node.parent = current
            current.children[dir_name] = new_node
        elif line.startswith("$"):
            command = line.split()[1].strip()
            if command == "ls":
                continue
            else:
                dir_name = line.split()[2].strip()
                if dir_name == "..":
                    current = current.parent
                else:
                    current = current.children[dir_name]
        else:
            size, name = line.split()
            current.files.append((int(size), name))
    calculate_sizes(root)
    return root
        

def print_tree(root: Node):
    if len(root.children) == 0:
        print(root.files)
    else:
        for child_dir, child_node in root.children.items():
            print(child_dir, child_node.size)
            print_tree(child_node)
        print(root.files)

def calculate_sizes(root: Node):
    if len(root.children) == 0:
        root.size = sum([t[0] for t in root.files])
    else:
        for child in root.children.values():
            calculate_sizes(child)
        root.size = sum([t[0] for t in root.files])
        root.size += sum([node.size for node in root.children.values()])

def directories_le_threshold(threshold: int, root: Node) -> list[Node]:
    nodes: list[Node] = []
    backlog = deque()
    backlog.append(root)
    current: Node = root
    while len(backlog) != 0:
        current = backlog.popleft()
        backlog.extend(current.children.values())
        if current.size <= threshold:
            nodes.append(current)
    return nodes

def directories_ge_threshold(threshold: int, root: Node) -> list[Node]:
    nodes: list[Node] = []
    backlog = deque()
    backlog.append(root)
    current: Node = root
    while len(backlog) != 0:
        current = backlog.popleft()
        backlog.extend(current.children.values())
        if current.size >= threshold:
            nodes.append(current)
    return nodes



if __name__ == "__main__":
    print(solution_part_1(get_input_data("puzzle_input.txt")))
    print(solution_part_2(get_input_data("puzzle_input.txt")))
