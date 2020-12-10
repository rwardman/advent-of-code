data = open("day2.txt", "r").read().split()

Part 1

def isPasswordValid(input):
  rule = input[0].split("-")
  minValue = int(rule[0])
  maxValue = int(rule[1])
  
  letter = input[1][0]
  password = input[2]

  timesLetterAppears = int(password.count(letter))

  if minValue <= timesLetterAppears <= maxValue:
    return True
  return False

validPasswords = 0

start = 0
end = 3
for i in range(0, int(len(data)/3)): 
  input = data[start:end]
  if isPasswordValid(input):
    validPasswords += 1
  start += 3
  end += 3

print("Part 1", validPasswords)

# Part 2

def isPasswordValid(input):
  rule = input[0].split("-")
  firstPosition = int(rule[0])
  secondPosition = int(rule[1])
  letter = input[1][0]
  
  password = input[2]

  existsAtFirst = password[firstPosition - 1] == letter
  existsAtSecond = password[secondPosition - 1] == letter

  return (existsAtFirst or existsAtSecond ) and not(existsAtFirst and existsAtSecond) 
  
  
validPasswords = 0

start = 0
end = 3
for i in range(0, int(len(data)/3)): 
  input = data[start:end]
  if isPasswordValid(input):
    validPasswords += 1
  start += 3
  end += 3

print("Part 2", validPasswords)
