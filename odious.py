import sys

def is_odious(num):
    number_one = '1'
    ones = ""
    bin_num = str(bin(num))

    for numbers in bin_num:
        if number_one in numbers:
            ones += number_one
    
    if not len(ones) % 2 == 0:
        return True
    else:
        return False
try:
    user_number = int(sys.argv[1])
    result = is_odious(user_number)
    print(result)

except ValueError:
    print('Use an integer')
    exit()

except IndexError: 
    print("Forgot to put a number \n usage python odious.py <number>")
    exit(1)




