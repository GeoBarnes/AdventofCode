"""Solution to advent of code day 15 part 1 https://adventofcode.com"""

FILE_NAME = "day_15_data.txt"


def read_file(file_n):
    """Reads initialisation sequence in file and outputs as list."""
    with open(file_n, "r", -1, "UTF-8") as file:
        seq = file.readline().split(",")
    return seq


def convert_to_ascii(code):
    """Converts string of chars to a list of their ASCII values."""
    ascii_vals = []
    for char in code:
        ascii_vals.append(ord(char))
    return ascii_vals


def apply_hash(ascii_code):
    """Returns value to be assigned to ascii code."""
    current_val = 0
    for val in ascii_code:
        current_val += val
        current_val = (current_val * 17) % 256
    return current_val


def main():
    """Reads sequence from file, converts each code in the sequence to ASCII
    and sums the converted values of each code."""
    total = 0
    for code in read_file(FILE_NAME):
        total += apply_hash(convert_to_ascii(code))
    print("total: ", total)  # = 517551 part 1


if __name__ == "__main__":
    main()
