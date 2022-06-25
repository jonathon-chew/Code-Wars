 def filter_list(l):
    filtered_list = []
    for i in l:
        if type(i) == int:
            filtered_list.append(i)
    return filtered_list
