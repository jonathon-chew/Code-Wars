 def solution(s):
    n = 2
    if len(s)%2==0:
        return [s[i:i + n] for i in range(0, len(s), n)]
    else:
        s = s + "_"
        return [s[i:i + n] for i in range(0, len(s), n)]
