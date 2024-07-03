rows = 1
# while rows <=5:
#     columns = 1
#     while columns <=rows:
#         print("*", end="")
#         columns+=1
#     print()
#     rows+=1
# rows = 1
max_rows = 5  # Assuming you want a pyramid with 5 rows
while rows <= max_rows:
    spaces = max_rows - rows
    while spaces > 0:
        print(" ", end="")
        spaces -= 1
    columns = 1
    while columns <= (2 * rows - 1):
        print("*", end="")
        columns += 1
    print()
    rows += 1