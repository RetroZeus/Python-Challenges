def double_letters(string):
    repeated = None
    for i in range(len(string)):
        try:
            if string[i] == string[i+1]:
                repeated = True
                break
            else:
                repeated = False
        except IndexError:
            pass
    return repeated

""" 
Challenge was to put a string which has same letter next to it. For example in the string 'HELLO' > 2 'L's are coming adjacent to each other.
Meanwhile 'Nono' has no same letters adjacent to it.

examples:
double_letters('nono') : False
double_letters('noon') : True

"""
