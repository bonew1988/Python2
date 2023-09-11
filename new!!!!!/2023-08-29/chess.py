import random

__all__ = ['are_queens_attacking_each_other',
           'generate_random_queens_positions', 'find_non_attacking_arrangements']


FIND_LIMIT = 10000000


def are_queens_attacking_each_other(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or \
               abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return True
    return False


def generate_random_queens_positions():
    queens = [(i + 1, random.randint(1, 8)) for i in range(8)]
    return queens


def find_non_attacking_arrangements(num_arrangements=4):
    successful_arrangements = []
    attempts = 0

    while len(successful_arrangements) < num_arrangements and attempts < FIND_LIMIT:
        queens = generate_random_queens_positions()
        if not are_queens_attacking_each_other(queens):
            successful_arrangements.append(queens)
        attempts += 1

    return successful_arrangements, attempts
