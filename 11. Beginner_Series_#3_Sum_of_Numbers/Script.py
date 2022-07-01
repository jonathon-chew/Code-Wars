 def get_sum(a,b):
    #good luck!
    answer = 0
    if a > b:
        for everyNumber in range(b, a + 1):
            answer = answer + everyNumber
        return answer
    elif a < b:
        for everyNumber in range(a, b + 1):
            answer = answer + everyNumber
        return answer
    elif a == b:
        return a
