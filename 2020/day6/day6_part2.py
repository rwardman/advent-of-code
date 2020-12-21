data = open("day6.txt", "r").read().split("\n\n")

total = 0
for group in range(0, len(data)):
  answers = data[group].split("\n")
  numberInGroup = len(answers)
  allCharacters = ''.join(answers)
  uniqueAnswers = set(allCharacters)
  numberOfUniqueAnswers = len(uniqueAnswers)
  
  if numberInGroup == 1:
    total += numberOfUniqueAnswers

  else:
    subTotal = 0
    characterInEveryAnswer = []

    for character in uniqueAnswers:
      allAnswersContainCharacter = True
      for answer in answers:
        characterInAnswer = character in answer
        allAnswersContainCharacter = allAnswersContainCharacter and characterInAnswer
      characterInEveryAnswer.append(allAnswersContainCharacter)

    sumOfCharactersInEveryAnswer = sum(characterInEveryAnswer)

    total += sumOfCharactersInEveryAnswer
  
  
  total += 0

print(total)