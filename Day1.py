ints=[0,1,2,3,4,5,6,7,8,9]
int_strings=['one','two','three','four','five','six','seven','eight','nine']
int_dic = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

# Gets first digit in line along with position
def first_dig(the_iterable):
    pos = -1
    for i in the_iterable:
        pos = pos + 1
        try:
            if int(i) in ints:
                return (int(i), pos)
        except:
            pass

# Gets last digit in line along with position
def last_dig(the_iterable):
    pos = len(the_iterable)
    for i in the_iterable[::-1]:
        pos = pos - 1
        try:
            if int(i) in ints:
                return (int(i), pos)
        except:
            pass

# Gets first digit string in line along with its starting position
# Converts digit string to integer
def first_dig_string(the_iterable):
    string_digits = []
    for int_string in int_strings:
        try:
            pos = the_iterable.index(int_string)
            string_digits.append((int_dic.get(int_string), pos))
        except:
            pass
    first_pos = []
    if string_digits:
        first_pos = min([(j, i) for i, j in string_digits])[::-1]
    return first_pos
 
# Gets last digit string in line along with its starting position
# Converts digit string to integer
def last_dig_string(the_iterable):
    string_digits = []
    for int_string in int_strings:
        try:
            # This uses rindex so that the last occurance of each integer string is found
            pos = the_iterable.rindex(int_string)
            string_digits.append((int_dic.get(int_string), pos))
        except:
            pass
    last_pos = []
    if string_digits:
        last_pos = max([(j, i) for i, j in string_digits])[::-1]
    return last_pos

# Finds the correct calibration for each line (first digit/digit string composed with the last)
def get_calibration(the_iterable):
    if first_dig_string(the_iterable):
        cal_val_1 = min([first_dig(the_iterable)[::-1], first_dig_string(the_iterable)[::-1]])[1]
    else:
        cal_val_1 = first_dig(the_iterable)[0]
    if last_dig_string(the_iterable):
        cal_val_2 = max([last_dig(the_iterable)[::-1], last_dig_string(the_iterable)[::-1]])[1]
    else:
        cal_val_2 = last_dig(the_iterable)[0]
    return int(str(cal_val_1) + str(cal_val_2))

total = 0

file=open("day1data.txt","r")

for line in file:
    calibration = get_calibration(line)
    total = total + calibration

    #total = total + get_calibration(line)

print("Total = ", total)

file.close()