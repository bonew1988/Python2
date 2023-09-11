from chess import chess


def main():
    queens_positions = [
        (0, 0),
        (6, 1),
        (4, 2),
        (7, 3),
        (1, 4),
        (3, 5),
        (5, 6),
        (2, 7)
    ]

    if chess.are_queens_attacking_each_other(queens_positions):
        print("Ферзи нападают друг на друга.")
    else:
        print("Ферзи не нападают друг на друга.")

    successful_arrangements, num_attempts = chess.find_non_attacking_arrangements(
        4)

    print("\nУспешные позиции:")
    for arrangement in successful_arrangements:
        print(arrangement)

    print("\nКоличество попыток:", num_attempts)


if __name__ == "__main__":
    main()
