rows = 5
for i in range(1, rows + 1):
    print(" " *(rows - i) + "*" * i)

rows = 5 
for i in range(1, rows + 1):
     print(" " *(rows - i) + "*" * i)

for i in range (rows - 1, 0, -1):
    print(" " *(rows - i) + "*" * i)

rows = 8
cols = 8
for i in range(rows):
    for j in range(cols):
        if (i + j) % 2 == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()


n = 5 
for i in range(n):
    print("" * (n - i - 1) + "*" * (2 * i + 1))

lista = [ 'Python', 'Java', 'C++', 'JavaScript', 'Ruby', 'PHP', 'Go', 'Swift', 'Kotlin', 'Rust']
for i in range(len(lista)):
    print(f"{i+1}. {lista[i]}")
