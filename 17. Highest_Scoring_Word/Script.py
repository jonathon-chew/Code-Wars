 def high(x):
    prev = 0
    value = 0
    for i, everyWord in enumerate(x.split()):
        for eachLetter in everyWord:
            value += ord(eachLetter) - 96
            if value > prev:
                prev = value
                answer = everyWord
        value = 0
    return answer
