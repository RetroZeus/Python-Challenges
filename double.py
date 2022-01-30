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

