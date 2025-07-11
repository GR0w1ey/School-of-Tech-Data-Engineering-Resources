name_counts = {

}

try:
  with open('repeated_names.txt', 'r+') as file_object:
    names = [name.strip() for name in file_object.readlines()]
    for name in names:
      if name_counts.get(name):
        name_counts[name] += 1
      else:
        name_counts[name] = 1

  with open('names_and_counts.txt', 'w') as file_object:
    for name in name_counts:
      file_object.write(f"Name: {name}, Count: {name_counts[name]}\n")
      
except FileNotFoundError as FNFE:
  print(f"File not found {FNFE}")
