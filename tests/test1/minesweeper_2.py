def transform(matrix, i, j):

    new_el = 0

    if j - 1 > 0 and matrix[i][j - 1] == "#":  # kolona
        new_el += 1

    if j + 1 < n and matrix[i][j + 1] == "#":  # kolona
        new_el += 1

    if i - 1 > 0 and matrix[i - 1][j] == "#":  # red
        new_el += 1

    if i + 1 < n and matrix[i + 1][j] == "#":  # red
        new_el += 1

    if j - 1 > 0 and i - 1 > 0 and matrix[i - 1][j - 1] == "#":  # dijagonala \
        new_el += 1

    if i + 1 < n and j + 1 < n and  matrix[i + 1][j + 1] == "#":  # dijagonala \
        new_el += 1

    if j + 1 < n and i - 1 > 0 and matrix[i - 1][j + 1] == "#":  # dijagonala /
        new_el += 1

    if i + 1 < n and j - 1 > 0 and matrix[i + 1][j - 1] == "#":  # dijagonala /
        new_el += 1

    return new_el

if __name__ == "__main__":
    n = int(input())
    list_of_lists = []
    p = 0

    while p < n:
        row = str(input())
        my_list = row.split("   ")
        list_of_lists.append(my_list)
        p += 1

    new_list_of_lists = []
    p = 0

    while p < n:
        new_list_of_lists.append([transform(list_of_lists, p, q) if el == "-" else "#" for q, el in enumerate(list_of_lists[p])])
        p += 1

    for new_list in new_list_of_lists:
        my_output = '   '.join(map(str, new_list))
        print(my_output)
