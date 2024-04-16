# This program checks for all fizzes (numbers which are equal to 3 or the previous number plus 3)
# and for buzzes (numbers equal to 5 or the previous number plus 5)

fizzes = [3]
buzzes = [5]

for i in range(1, 101):
  str = ''
  if (i == fizzes[-1] + 3 or i == 3):
    fizzes.append(i)
    str += "Fizz"
    if (i == buzzes[-1] + 5 or i == 5):
      buzzes.append(i)
      str += "Buzz"
    
  elif (i == buzzes[-1] + 5 or i == 5):
    buzzes.append(i)
    str += "Buzz"
  
  
  print("Number: ",i)
  print("Fizzes: ",fizzes)
  print("Buzzes: ",buzzes)
  print(str, "\n")