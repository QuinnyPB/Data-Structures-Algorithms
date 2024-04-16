
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