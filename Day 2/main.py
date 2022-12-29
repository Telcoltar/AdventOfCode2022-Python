from enum import Enum, auto
from typing import Callable

class Symbol(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

class Outcome(Enum):
    WIN = 6
    LOOSE = 0
    DRAW = 3

input_symbol_map = {
    "A": Symbol.ROCK,
    "B": Symbol.PAPER,
    "C": Symbol.SCISSORS
}

output_symbol_map = {
    "X": Symbol.ROCK,
    "Y": Symbol.PAPER,
    "Z": Symbol.SCISSORS
}

outcome_map = {
    "X": Outcome.LOOSE,
    "Y": Outcome.DRAW,
    "Z": Outcome.WIN
}

def get_fitting_symbol(outcome: Outcome, first: Symbol):
    match outcome:
        case Outcome.DRAW:
            return first
        case Outcome.WIN:
            return Symbol((first.value % 3) + 1)
        case Outcome.LOOSE:
            return Symbol(((first.value - 2) % 3) + 1)

def compare_symbols(first: Symbol, second: Symbol):
    if first == second:
        return 3
    if (first.value % 3) + 1 == second.value:
        return 6
    return 0

def decoder_part_1(input_strings: tuple[str, str]) -> tuple[Symbol, Symbol]:
    return (input_symbol_map[input_strings[0]], output_symbol_map[input_strings[1]])

def decoder_part_2(input_strings: tuple[str, str]) -> tuple[Symbol, Outcome]:
    return (input_symbol_map[input_strings[0]], outcome_map[input_strings[1]])

def read_input(filename: str, decoder: Callable[[tuple[str, str]], tuple[Symbol, Symbol | Outcome]]) -> list[tuple[Symbol, Symbol | Outcome]]:
    pairs: list[tuple[Symbol, Symbol]] = []
    with open(filename, encoding="UTF-8") as f:
        for line in f.readlines():
            first_part, second_part = map(
                lambda s: s.strip(),
                line.split()
            )
            pairs.append(decoder((first_part, second_part)))
    return pairs

def solution_part_1(input_data: list[tuple[Symbol, Symbol]]):
    points = 0
    for first, second in input_data:
        # print(first, second, compare_symbols(first, second), second.value)
        points += second.value
        points += compare_symbols(first, second)
    return points

def solution_part_2(input_data: list[tuple[Symbol, Symbol]]):
    points = 0
    for first, outcome in input_data:
        points += get_fitting_symbol(outcome, first).value
        points += outcome.value
    return points

if __name__ == "__main__":
    print(solution_part_1(read_input("puzzle_input.txt", decoder_part_1)))
    print(solution_part_2(read_input("puzzle_input.txt", decoder_part_2)))
    # print(compare_symbols(Symbol.ROCK, Symbol.ROCK))
    # print(compare_symbols(Symbol.ROCK, Symbol.PAPER))
    # print(compare_symbols(Symbol.ROCK, Symbol.SCISSORS))
    # print(compare_symbols(Symbol.PAPER, Symbol.ROCK))
    # print(compare_symbols(Symbol.PAPER, Symbol.PAPER))
    # print(compare_symbols(Symbol.PAPER, Symbol.SCISSORS))
    # print(compare_symbols(Symbol.SCISSORS, Symbol.ROCK))
    # print(compare_symbols(Symbol.SCISSORS, Symbol.PAPER))
    # print(compare_symbols(Symbol.SCISSORS, Symbol.SCISSORS))
