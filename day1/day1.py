data = open("data.txt", "r")

inputs = data.read().split()

for entry in inputs:
  for nextEntry in inputs:
      for thirdEntry in inputs:
        sum = int(entry) + int(nextEntry) + int(thirdEntry)
        if sum == 2020:
          print(entry, nextEntry, thirdEntry)
          print(int(entry) * int(nextEntry) * int(thirdEntry))
        


