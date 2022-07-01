 def positive_sum(arr):
    # Your code here
    answer = 0
    for everyNumber in arr:
        if everyNumber > 0:
            answer = answer + everyNumber
    return answer
