rows = int(input("Insert the rows: "))


for j in range(rows):

  print(" " * (rows - j - 1), end="")
  print("* " * (j + 1))
