"""Add docstring here"""
FILE_NAME = "day14data.txt"


def transpose(matrix):
    """Tranposes a list of lists as if it were a matrix."""
    return list(map(list, zip(*matrix)))


def between(limit_1, limit_2, pos):
    """Returns true is pos between limit_1 and limit_2, otherwise false."""
    if limit_1 < pos < limit_2 or limit_2 < pos < limit_1:
        return True
    else:
        return False


def read_file(file_n):
    """Reads pattern in file and outputs the 2d array."""
    with open(file_n, "r", -1, "UTF-8") as file:
        file_pattern = []
        for line in file:
            row = []
            for char in line.strip():
                row.append(char)
            file_pattern.append(row)
    return file_pattern


def rock_locs(row):
    """Reads a row of an array and returns a list of the round rock indices
    and a list of the fixed rock indices."""
    fixed_rocks = [-1]
    round_rocks = []
    for index, char in enumerate(row):
        if char == "#":
            fixed_rocks.append(index)
        if char == "O":
            round_rocks.append(index)
    return round_rocks, fixed_rocks


def tilt_north(round_rocks, fixed_rocks):
    """Tilt single row of rocks to the north."""
    round_rocks_tilt = []
    for round_rock in round_rocks:
        catch_rock = max(list(filter(lambda x: x < round_rock, fixed_rocks)))
        buffer_size = len(
            list(filter(lambda x: between(catch_rock, round_rock, x), round_rocks))
        )
        round_rocks_tilt.append(catch_rock + buffer_size + 1)
    return round_rocks_tilt


def main():
    """Reads file, slides rocks north, calculates total moment of round
    rocks."""
    pattern = transpose(read_file(FILE_NAME))
    total_moment = 0
    for line in pattern:
        round_rocks, fixed_rocks = rock_locs(line)
        total_moment += 100 * len(round_rocks) - sum(
            tilt_north(round_rocks, fixed_rocks)
        )
    print("total moment: ", total_moment)


if __name__ == "__main__":
    main()
