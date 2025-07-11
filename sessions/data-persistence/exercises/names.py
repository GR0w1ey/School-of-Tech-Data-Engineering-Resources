names = []
with open("names.txt", "r") as file:
  lines = file.readlines()
  for line in lines:
    names.append(line.strip())
  print(names)
