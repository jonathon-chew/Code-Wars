 def unique_in_order(iterable):
    answer = []
    prev = None
    for i in iterable[0:]:
        if i != prev:
            answer.append(i)
            prev = i
    return answer
