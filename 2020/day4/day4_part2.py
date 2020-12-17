import re

data = open("day4.txt", "r").read().split("\n\n")

requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def assessCredential(field, credentials):
  credential = credentials[4:]

  # Birth Year
  if field == "byr":
    isValidYear = 1920 <= int(credential) <= 2002
    isValidDigits = len(credential) == 4
    return isValidYear and isValidDigits

  # Issue Year
  if field == "iyr":
    isValidYear = 2010 <= int(credential) <= 2020
    isValidDigits = len(credential) == 4
    return  isValidYear and isValidDigits

  # Expiration Year
  if field == "eyr":
    isValidYear = 2020 <= int(credential) <= 2030
    isValidDigits = len(credential) == 4
    return  isValidYear and isValidDigits

  # Height
  if field == "hgt":
    amount = credential[:-2]
    unit = credential[-2:]

    if unit == "cm":
      isValidAmount = 150 <= int(amount) <= 193
      return isValidAmount
    elif unit == "in":
      isValidAmount = 59 <= int(amount) <= 76
      return isValidAmount
    else:
      return False

  # Hair Colour
  if field == "hcl":
    if (re.match("#[0-9a-f]{6}", credential)):
      hasValidHex = True
    else:
      hasValidHex = False
    return hasValidHex

  # Eye Colour
  if field == "ecl":
    validEyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    isValidEyeColor = credential in validEyeColors
    return isValidEyeColor
  
  #Passport ID
  if field == "pid":
    isValidLength = len(credential) == 9
    return isValidLength


def areCredentialsValid(credentials):
  containsRequiredFields = True
  for field in requiredFields:
    fieldNeeded = field + ":"
    if fieldNeeded in credentials:
      validity = True
    else:
      validity = False
    containsRequiredFields = validity and containsRequiredFields
  
  allFieldsareValid = True
  creds = credentials.split()
  for field in requiredFields:
    lookingFor = field + ":"
    for credential in creds: 
      if lookingFor in credential:
        validity = assessCredential(field, credential)
        allFieldsareValid = allFieldsareValid and validity
  
  isValidPassword = containsRequiredFields and allFieldsareValid
  return isValidPassword

validPassports = 0
for iterator in range(0, len(data)):
  credentials = data[iterator]
  if areCredentialsValid(credentials):
    validPassports += 1

print("Valid passports: ", validPassports)
