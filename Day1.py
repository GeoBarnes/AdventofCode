file=open("data.txt","r")

ints=[0,1,2,3,4,5,6,7,8,9]

def first_dig(the_iterable):
    for i in the_iterable:
        try:
            if int(i) in ints:
                return i
        except:
            pass

def get_calibration(the_iterable):
    cal_val_1=first_dig(the_iterable)
    cal_val_2=first_dig(the_iterable[::-1])
    return int(cal_val_1 + cal_val_2)

total = 0

for line in file:
    calibration = get_calibration(line)
    #print(line)
    #print(calibration)
    total = total + calibration

print("Total = ", total)


file.close()