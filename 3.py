# -*- coding: utf-8 -*-
"""
@author: Trajan
"""
# Use Hungary Algorithm to get transformed matrix
def hungary(matrix_ori):
    matrix = matrix_ori.copy()
    # step 1
    for i in range(len(matrix)):
        matrix[i] = [k-min(matrix[i]) for k in matrix[i]]
    # step 2
    for i in range(len(matrix)):
        colmin = min([matrix[k][i] for k in range(len(matrix))])
        for k in range(len(matrix)):
            matrix[k][i] -= colmin
    line_count = 0
    while (line_count < len(matrix)):
        # step 3
        line_count = 0
        row_zero_count = [] # The number of zeros in each row.
        col_zero_count = [] # The number of zeros in each column.
        for i in range(len(matrix)):
            row_zero_count.append(matrix[i].count(0))
        for i in range(len(matrix)):
            col_zero_count.append([matrix[k][i] for k in range(len(matrix))].count(0))
        delete_count_of_row = [] # the lines through rows.
        delete_count_of_col = [] # the lines through columns.
        zero_add_zero = [] # zeros to be the only one in its column and row.
        zero_add_one = [] # zeros to be the only one in its column or row.
        zero_add_two = [] # other zeros
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == 0:
                    if row_zero_count[i] == 1 and col_zero_count[j] == 1:
                        zero_add_zero.append([i,j])
                    elif row_zero_count[i] == 1 or col_zero_count[j] == 1:
                        zero_add_one.append([i,j])
                    else:
                        zero_add_two.append([i,j])
        if zero_add_zero:
            for add in zero_add_zero:
                if (add[1] not in delete_count_of_col) and (add[0] not in delete_count_of_row):
                    if row_zero_count[add[0]] >= col_zero_count[add[1]]:
                        delete_count_of_row.append(add[0])
                        for i in range(len(matrix)):
                            if matrix[add[0]][i] == 0:
                                col_zero_count[i] -= 1
                    elif row_zero_count[add[0]] < col_zero_count[add[1]]:
                        delete_count_of_col.append(add[1])
                        for i in range(len(matrix)):
                            if matrix[i][add[1]] == 0:
                                row_zero_count[i] -= 1
        if zero_add_one:
            for add in zero_add_one:
                if (add[1] not in delete_count_of_col) and (add[0] not in delete_count_of_row):
                    if row_zero_count[add[0]] >= col_zero_count[add[1]]:
                        delete_count_of_row.append(add[0])
                        for i in range(len(matrix)):
                            if matrix[add[0]][i] == 0:
                                col_zero_count[i] -= 1
                    elif row_zero_count[add[0]] < col_zero_count[add[1]]:
                        delete_count_of_col.append(add[1])
                        for i in range(len(matrix)):
                            if matrix[i][add[1]] == 0:
                                row_zero_count[i] -= 1
        if zero_add_two:
            for add in zero_add_two:
                if (add[1] not in delete_count_of_col) and (add[0] not in delete_count_of_row):
                    if row_zero_count[add[0]] >= col_zero_count[add[1]]:
                        delete_count_of_row.append(add[0])
                        for i in range(len(matrix)):
                            if matrix[add[0]][i] == 0:
                                col_zero_count[i] -= 1
                    elif row_zero_count[add[0]] < col_zero_count[add[1]]:
                        delete_count_of_col.append(add[1])
                        for i in range(len(matrix)):
                            if matrix[i][add[1]] == 0:
                                row_zero_count[i] -= 1
        left_mat = [x for i, x in enumerate(matrix) if i not in delete_count_of_row]
        for i in range(len(left_mat)):
            left_mat[i] = [x for i, x in enumerate(left_mat[i]) if i not in delete_count_of_col]
        # step 4
        line_count = len(delete_count_of_row) + len(delete_count_of_col)    
        if line_count == len(matrix):
            break
        # step 5
        if 0 not in sum(left_mat,[]):
            row_sub = list(set(range(len(matrix))) - set(delete_count_of_row))
            min_value = min(sum(left_mat,[])) # the smallest value in the rest of the matrix
            for i in row_sub:
                for k in range(len(matrix)):
                    matrix[i][k] -= min_value
            for i in delete_count_of_col:
                for k in range(len(matrix)):
                    matrix[k][i] += min_value
    return matrix

# Use the transformed matrix to get the assignment, similar to step3.
def assignment(matrix):
    row_zero_count = []
    for i in range(len(matrix)):
        row_zero_count.append(matrix[i].count(0))
    col_zero_count = []
    for i in range(len(matrix)):
        col_zero_count.append([matrix[k][i] for k in range(len(matrix))].count(0))
    path = []
    while len(path)<len(matrix):
        for i in range(len(matrix)):
            if row_zero_count[i] == 1:
                col_zero_count[matrix[i].index(0)] -= 1
                row_zero_count[i] = 0
                if [i, matrix[i].index(0)] not in path:
                    path.append([i, matrix[i].index(0)])
        for i in range(len(matrix)):
            if col_zero_count[i] == 1:
                row_zero_count[[matrix[k][i] for k in range(len(matrix))].index(0)] -= 1
                col_zero_count[i] = 0
                if [[matrix[k][i] for k in range(len(matrix))].index(0),i] not in path:
                    path.append([[matrix[k][i] for k in range(len(matrix))].index(0),i])
    return path 

if __name__ == "__main__":
    matrix = [
    [7, 53, 183, 439, 863, 497, 383, 563,79, 973, 287, 63,343, 169, 583],
    [627, 343, 773, 959, 943, 767, 473, 103, 699, 303, 957, 703, 583, 639, 913],
    [447, 283, 463, 29, 23, 487, 463, 993, 119, 883, 327, 493, 423, 159, 743],
    [217, 623, 3, 399, 853, 407, 103, 983, 89, 463, 290, 516, 212, 462, 350],
    [960, 376, 682, 962, 300, 780, 486, 502, 912, 800, 250, 346, 172, 812, 350],
    [870, 456, 192, 162, 593, 473, 915, 45, 989, 873, 823, 965, 425, 329, 803],
    [973, 965, 905, 919, 133, 673, 665, 235, 509, 613, 673, 815, 165, 992, 326],
    [322, 148, 972, 962, 286, 255, 941, 541, 265, 323, 925, 281, 601, 95, 973],
    [445, 721, 11, 525, 473, 65, 511, 164, 138, 672, 18, 428, 154, 448, 848],
    [414, 456, 310, 312, 798, 104, 566, 520, 302, 248, 694, 976, 430, 392, 198],
    [184, 829, 373, 181, 631, 101, 969, 613, 840, 740, 778, 458, 284, 760, 390],
    [821, 461, 843, 513, 17, 901, 711, 993, 293, 157, 274, 94, 192, 156, 574],
    [34, 124, 4, 878, 450, 476, 712, 914, 838, 669, 875, 299, 823, 329, 699],
    [815, 559, 813, 459, 522, 788, 168, 586, 966, 232,308, 833,251, 631, 107],
    [813, 883, 451, 509, 615, 77, 281, 613, 459, 205, 380, 274, 302, 35, 805]
    ]
    
#    import time
#    start = time.time()
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = 1000-matrix[i][j]
            
    zero_matrix = hungary(matrix)
    path = assignment(zero_matrix)
    
    add = 0
    for p in path:
        add += matrix[p[0]][p[1]]
    print("The largest value is:", 15000-add)
#    end = time.time()
#    print("Run time: ",end-start)
