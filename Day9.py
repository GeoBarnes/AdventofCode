import re

file_name = "day9data.txt"

# Read sequences from file
def sequences(file_n):
    sequences = []
    with open(file_n,"r") as file:
        for line in file:
            sequences.append([int(s) for s in re.findall(r'[-]?[0-9]+', line)])
    return sequences

def get_sequence_diffs(sequence):
    derivative_sequence = []
    seq_len = len(sequence)
    for i in range(seq_len - 1):
        derivative_sequence.append(sequence[i+1] - sequence[i])
    return derivative_sequence

def reduce_sequence(sequence):
    final_values = []
    derivative_sequence = sequence
    while not all(v == 0 for v in derivative_sequence):
        final_values.append(derivative_sequence[-1])
        derivative_sequence = get_sequence_diffs(derivative_sequence)
    return(final_values)

def reduce_sequence_part_2(sequence):
    first_values = []
    derivative_sequence = sequence
    while not all(v == 0 for v in derivative_sequence):
        first_values.append(derivative_sequence[0])
        derivative_sequence = get_sequence_diffs(derivative_sequence)
    return(first_values)

original_sequences = sequences(file_name)

total_part_1 = 0
for sequence in original_sequences:
    total_part_1 += sum(reduce_sequence(sequence))

print('total_part_1: ', total_part_1) # = 1696140818 (part 1)

total_part_2 = 0
for sequence in original_sequences:
    seq_val = 0
    first_elements = reduce_sequence_part_2(sequence)
    for i, val in enumerate(first_elements):
        seq_val += val*(-1)**(i) 
    total_part_2 += seq_val

print('total_part_2: ', total_part_2) # = 1152 (part_2)