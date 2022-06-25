 def find_outlier(integers):
    evenArray = []
    oddArray = []
    
    for i in integers:
        if i % 2 == 0:
            evenArray.append(i)
        elif i % 2 != 0:
            oddArray.append(i)

    if len(evenArray) == 1:
        return evenArray[0]
    elif len(evenArray) > 1:
        return oddArray[0]
