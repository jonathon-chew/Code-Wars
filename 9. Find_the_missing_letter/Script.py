 def find_missing_letter(chars):
    convertToNumbers = findChr(chars)  
    for j, everyNumber in enumerate(convertToNumbers):
        if convertToNumbers[j] + 1 == convertToNumbers[j+1]:
            continue
        else:
            return chr(everyNumber + 1)

def findChr(chars):
    convertToNumbers = []
    for j, everyCharacter in enumerate(chars):
        for i in range(65, 122):
            if chr(i) == chars[j]:
                convertToNumbers.append(i)
    return convertToNumbers
