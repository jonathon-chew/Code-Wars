 def accum(s):
    # your code
    newString = []
    for i, everyLetter in enumerate(s):
        newString.append((everyLetter * (i+1)).capitalize())
    return '-'.join(newString)
