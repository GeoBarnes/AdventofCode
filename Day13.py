file_name = "day13data.txt"

# Read each pattern into a 2d array
def read_file(file_n):
    patterns = []
    with open(file_n, 'r') as file:
        pattern = []
        for line in file:
            # If line is empty then start reading a new pattern
            if not line.strip():
                patterns.append(pattern)
                pattern = []
            else:
                row = []
                for char in line.strip():
                    row.append(char)
                pattern.append(row)
        patterns.append(pattern)
    return patterns


def column(matrix, i):
    return [row[i] for row in matrix]


def is_mirror_row(pattern, mirror_row):
    j = 0
    is_mirror_row = True
    try:
        while pattern[mirror_row + j] and (mirror_row - 1 - j) >= 0:
            if pattern[mirror_row + j] != pattern[mirror_row - 1 - j]:
                is_mirror_row = False
            j += 1
    except:
        pass
    return is_mirror_row
            

def is_mirror_col(pattern, mirror_col):
    j = 0
    is_mirror_col = True
    try:
        while column(pattern, mirror_col + j ) and (mirror_col - 1 - j) >= 0 :
            if column(pattern, mirror_col + j ) != column(pattern, mirror_col - 1 - j):
                is_mirror_col = False
            j += 1
    except:
        pass
    return is_mirror_col


# main
patterns = read_file(file_name)

note_summary = 0

for pattern in patterns:
    for i in range(len(pattern)-1):
        if pattern[i] == pattern[i+1]:
            if is_mirror_row(pattern, i+1):
                note_summary += (i+1)*100
    for i in range(len(pattern[0])-1):
        if column(pattern, i) == column(pattern, i+1):
            if is_mirror_col(pattern, i+1):
                note_summary += i+1
            
print('note summary: ', note_summary) # part 1: 37025