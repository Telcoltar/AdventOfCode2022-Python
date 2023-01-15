from collections import deque
import time

def solution_part_1(filename: str):
    with open(filename, "r", encoding="utf-8") as f:
        datastream = f.read().strip()
    deque_window = deque(datastream[:4])
    first_marker = 4
    for i, data in enumerate(datastream[4:]):
        if len(set(deque_window)) == 4:
            first_marker += i
            break
        deque_window.popleft()
        deque_window.append(data)
    return first_marker

def solution_part_2(filename: str):
    with open(filename, "r", encoding="utf-8") as f:
        datastream = f.read().strip()
    deque_window = deque(datastream[:14])
    first_marker = 14
    for i, data in enumerate(datastream[14:]):
        if len(set(deque_window)) == 14:
            first_marker += i
            break
        deque_window.popleft()
        deque_window.append(data)
    return first_marker


if __name__ == "__main__":
    start = time.time()
    print(solution_part_2("puzzle_input.txt"))
    print((time.time() - start) * 1000)
