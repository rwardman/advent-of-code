data = open("day5.txt", "r").read().splitlines()

def determineSeatLocation(seat):
  row = seat[:7]
  column = seat[7:]

  rowPosition = calculatePoisitionForCode(row, 0, 127, "F", "B")
  columnPosition = calculatePoisitionForCode(column, 0, 7, "L", "R")


  seatId = rowPosition * 8 + columnPosition

  return seatId


def calculatePoisitionForCode(code, start, end, lowerHalfCharacter, upperHalfCharacter):
  lastCharacterPosition = len(code) - 1

  rangeStart = start
  rangeEnd = end

  for character in code[0:lastCharacterPosition]:
    currentRange = sorted([rangeStart, rangeEnd])
    number, remainder = divmod(currentRange[1] - currentRange[0], 2)
    
    # Lower Half
    if (character == lowerHalfCharacter):
      rangeEnd = rangeEnd - (number + remainder)
    
    # Upper half
    elif (character == upperHalfCharacter):
      rangeStart = rangeStart + number + remainder
  

  if (code[lastCharacterPosition] == lowerHalfCharacter):
    return rangeStart
  else:
    return rangeEnd


seatIds = []
for iterator in range(0, len(data)):
  seat = data[iterator]
  seatId = determineSeatLocation(seat)
  seatIds.append(seatId)


print(max(seatIds))


def findMissing(list): 
  start = list[0] 
  end = list[-1] 
  return sorted(set(range(start, end + 1)).difference(list)) 


print(findMissing(sorted(seatIds)))
