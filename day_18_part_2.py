"""Solution to advent of code day 18 part 1 https://adventofcode.com"""

# Define input file name
FILE_NAME = "day_18_data.txt"

# Define directions
# directions = {"U": (1, 0), "D": (-1, 0), "L": (0, -1), "R": (0, 1)}
directions = {3: (1, 0), 1: (-1, 0), 2: (0, -1), 0: (0, 1)}


def add_tup(t1, t2):
    """Adds tuples as if they were vectors."""
    if not t1:
        return ()
    return (t1[0] + t2[0],) + add_tup(t1[1:], t2[1:])


def tup_mult(t1, c):
    """Scalar multiplication of a tuple."""
    return (t1[0] * c, t1[1] * c)


def find_moves():
    """Reads file and returns list of directions."""
    moves = []
    with open(FILE_NAME, "r", -1, "UTF-8") as file:
        for line in file:
            hex_code = line.split(" ")[2].strip().strip("()").strip("#")
            moves.append((int(hex_code[5]), int(hex_code[:5], 16)))
    return moves


def find_perimeter(moves):
    """Returns list of perimeter points."""
    perimeter = []
    pos = (0, 0)
    for move in moves:
        direction = directions[move[0]]
        for _ in range(1, int(move[1]) + 1):
            perimeter.append(pos)
            pos = add_tup(pos, direction)
    return perimeter


def find_vertices(moves):
    """Returns list of vertex points of polygon."""
    vertices = []
    pos = (0, 0)
    for move in moves:
        direction = directions[move[0]]
        vertices.append(pos)
        pos = add_tup(pos, tup_mult(direction, int(move[1])))
    return vertices


def shoelace_area(vertices):
    """Implements the shoelace formula to return the area."""
    area = 0
    num_vertices = len(vertices)
    for i, vertex in enumerate(vertices):
        area += (
            vertex[1] * vertices[(i + 1) % num_vertices][0]
            - vertices[(i + 1) % num_vertices][1] * vertex[0]
        )
    return area / 2


def main():
    """Calculates area within loop traced by moves in file."""
    moves = find_moves()
    vertices = find_vertices(moves)

    print(
        "total: ", abs(shoelace_area(vertices)) + len(find_perimeter(moves)) / 2 + 1
    )  # 63806916814808 correct answer


if __name__ == "__main__":
    main()
