data = open("day3.txt", "r").read().splitlines()

openSquare = data[0][0]
tree = data[0][6]


def howManyTrees(right, down): 
  position = right
  iterator = down
  trees = 0
  openSquares = 0

  for rowIterator in range(0, int((len(data))/down) - 1):
    row = data[iterator]
    res_row = row * 100
    obstacle = res_row[position]
    position += right

    if obstacle == openSquare:
      openSquares += 1
    elif obstacle == tree:
      trees += 1  
    iterator += down
  
  print("Trees encountered for right ", right, " down ", down, " is ", trees)
  return trees

first = howManyTrees(1,1)
second = howManyTrees(3,1)
third = howManyTrees(5,1)
fourth = howManyTrees(7,1)
fifth = howManyTrees(1,2)

finalResult = first * second * third * fourth * fifth
print("Multiplied trees", finalResult)