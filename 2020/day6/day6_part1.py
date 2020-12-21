data = open("day6.txt", "r").read().split("\n\n")

total = 0
for group in range(0, len(data)):
  answers = data[group].split("\n")
  numberInGroup = len(answers)
  allCharacters = ''.join(answers)
  uniqueAnswers = set(allCharacters)
  numberOfUniqueAnswers = len(uniqueAnswers)
  
  total += numberOfUniqueAnswers

print(total)