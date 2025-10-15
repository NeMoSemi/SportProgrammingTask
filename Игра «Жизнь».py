# J. Игра «Жизнь»
# ограничение по времени на тест1 секунда
# ограничение по памяти на тест256 мегабайт
# В некоторых клетках квадрата N×N
#  живут микроорганизмы (не более одного в одной клетке). Каждую секунду происходит следующее:
#
# все микроорганизмы, у которых менее двух соседей, умирают от скуки (соседями называются микроорганизмы, живущие в клетках, имеющих общую сторону или вершину);
# все микроорганизмы, у которых более трех соседей, умирают от перенаселенности;
# на всех пустых клетках, у которых ровно в трех соседних клетках жили микроорганизмы, появляются новые микроорганизмы.
# Все изменения происходят одновременно, то есть для каждой клетки сначала выясняется ее судьба, а затем происходят изменения сразу во всех клетках. Требуется по данной конфигурации определить, во что она превратится через T
#  секунд.
#
# Входные данные
# В первой строке вводятся два натуральных числа — N
#  (1≤N≤10
# ) и T
#  (1≤T≤100
# ). Далее записано N
#  строчек по N
#  чисел, описывающих начальную конфигурацию (0
#  — пустая клетка, 1
#  — микроорганизм). Числа в строках разделены пробелами.
#
# Выходные данные
# Требуется вывести N
#  строк по N
#  чисел — описание конфигурации через T
#  секунд (в том же формате, как и во входных данных).
#
# Примеры
# Входные данныеСкопировать
# 3 1
# 1 0 1
# 1 0 1
# 1 0 1
# Выходные данныеСкопировать
# 0 0 0
# 1 0 1
# 0 0 0
# Входные данныеСкопировать
# 2 2
# 1 1
# 1 1
# Выходные данныеСкопировать
# 1 1
# 1 1
# Входные данныеСкопировать
# 5 10
# 1 0 1 1 0
# 0 1 0 0 0
# 0 0 0 1 0
# 0 0 0 0 0
# 0 1 0 1 0
# Выходные данныеСкопировать
# 0 1 1 0 0
# 0 1 1 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0

def get_neighbors_count(field, r_c_count):
    matrix_of_neighbors = []
    row_count = r_c_count
    column_count = r_c_count
    field_h = field.copy()
    for i in range(r_c_count):
        field_h[i] = [0] + field_h[i] + [0]
    field_h.append([0] * (r_c_count + 2))
    field_h = [[0] * (r_c_count + 2)] + field_h
    for row in range(1, row_count + 1):
        row_matrix = []
        for column in range(1, column_count + 1):
            row_matrix.append(field_h[row - 1][column - 1] + field_h[row - 1][column] +
                              field_h[row - 1][column + 1] + field_h[row][column - 1] +
                              field_h[row][column + 1] + field_h[(row + 1)][column - 1] +
                              field_h[row + 1][column] +
                              field_h[row + 1][column + 1])
        matrix_of_neighbors.append(row_matrix)
    return matrix_of_neighbors


def cells_birth_and_life(field, matrix_of_neighbors, row_count, column_count):
    reborn_matrix = []
    for row in range(row_count):
        row_reborn_matrix = []
        for column in range(column_count):
            if (field[row][column] == 0 and (matrix_of_neighbors[row][column] == 3)) or \
                    (field[row][column] == 1 and (matrix_of_neighbors[row][column] in [2, 3])):
                row_reborn_matrix.append(1)
            else:
                row_reborn_matrix.append(0)
        reborn_matrix.append(row_reborn_matrix)
    return reborn_matrix


n, t = map(int, input().split())
field = [[int(i) for i in input().split()] for _ in range(n)]
for _ in range(t):
    get_neighbors = get_neighbors_count(field, n)
    field = cells_birth_and_life(field, get_neighbors, n, n)
for i in range(n):
    print(*field[i])