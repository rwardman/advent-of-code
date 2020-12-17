import re

data = open("day4.txt", "r").read().split("\n\n")

requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

credentials = data[4]

def isCredentialsValid(credentials):
  isValid = True
  for field in requiredFields:
    lookingFor = field + ":"
  
    validity = True
    if lookingFor in credentials:
      validity = True
    else:
      validity = False

    isValid = validity & isValid
  return isValid

validPassports = 0
for iterator in range(0, len(data)):
  credentials = data[iterator]
  if isCredentialsValid(credentials):
    validPassports += 1

print("Valid passports: ", validPassports)
