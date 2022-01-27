import sys

def get_ascii(string):
    odd_value = []
    even_value = []

    for each in string:
        if ord(each) % 2 == 0:
            even_value.append(2*ord(each))
        else:
            odd_value.append(ord(each))

    if odd_value != [] and even_value != []:
        return sum(odd_value) + sum(even_value)

    elif odd_value == []:
        return even_value

    elif even_value == []:
        return odd_value
    else:
        print('Something went wrong')

try:
    args = sys.argv[1]
    print(get_ascii(args))  

except IndexError:
    print('Usage python ascii.py <string>')