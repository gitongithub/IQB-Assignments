import numpy


def global_alignment(a, gap):
    # initializing the 0th row and column with gap penalties
    for i in range(1, n + 1):
        a[i][0] = (i * gap)
    for i in range(1, m + 1):
        a[0][i] = (i * gap)
    # for all the rest of the cells checking if match/mismatch and then computing the best score
    # after considering match/mismatch or gap in either of the sequences
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if seq2[i - 1] == seq1[j - 1]:
                a[i][j] = max(a[i - 1][j - 1] + match, a[i - 1][j] + gap, a[i][j - 1] + gap)
            else:
                a[i][j] = max(a[i - 1][j - 1] + mismatch, a[i - 1][j] + gap, a[i][j - 1] + gap)


def local_alignment(a, gap):
    # initializing the 0th row and column with 0
    for i in range(1, n + 1):
        a[i][0] = 0
    for i in range(1, m + 1):
        a[0][i] = 0
    # for all the rest of the cells checking if match/mismatch and then computing the best score
    # after considering match/mismatch or gap in either of the sequences
    # However, no cell is assigned the value of less than 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if seq2[i - 1] == seq1[j - 1]:
                a[i][j] = max(0, a[i - 1][j - 1] + match, a[i - 1][j] + gap, a[i][j - 1] + gap)
            else:
                a[i][j] = max(0, a[i - 1][j - 1] + mismatch, a[i - 1][j] + gap, a[i][j - 1] + gap)


def find_global_alignment(a, gap, path1, path2, i, j, count):
    # if the last step was due to a match/mismatch we will directly reach the top left cell and so
    #we can print our path
    if i==0 and j==0:
        for k in range(count):
            print(path1[count - k - 1], end=" ")
        print()
        for k in range(count):
            if path1[count - k - 1] == path2[count- k - 1]:
                print("|", end=" ")
            else:
                print(" ", end=" ")
        print()
        for k in range(count):
            print(path2[count - k - 1], end=" ")
        print()
        print()
        return
    if i == 0:
        path1[count ] = seq1[j - 1]
        path2[count ] = '-'
        for k in range(1, j ):
            path1[count + k ] = seq1[j - k - 1]
            path2[count + k ] = '-'
        for k in range(count + j):
            print(path1[count + j - k - 1], end=" ")
        print()
        for k in range(count + j):
            if path1[count + j - k - 1] == path2[count + j - k - 1]:
                print("|", end=" ")
            else:
                print(" ", end=" ")
        print()
        for k in range(count + j):
            print(path2[count + j - k - 1], end=" ")
        print()
        print()
        return
    if j == 0:
        path1[count ] = '-'
        path2[count ] = seq2[i - 1]
        for k in range(1, i + 1):
            path1[count + k ] = '-'
            path2[count + k ] = seq2[i - k - 1]

        for k in range(count + i):
            print(path1[count +i-k -1], end=" ")
        print()
        for k in range(count + i):
            if path1[count + i - k - 1] == path2[count +i -k - 1]:
                print("|", end=" ")
            else:
                print(" ", end=" ")
        print()
        for k in range(count + i):
            print(path2[count +i -k -1], end=" ")
        print()
        print()
        return
    # checking for a match/mismatch and then doing a recursive call after making valid jump to
    # left, up, diagonally up any(>0) which gives valid solution
    # before recursive call, store the alignment step in the path
    if i - 1 >= 0 and j - 1 >= 0 and seq2[i - 1] == seq1[j - 1] and a[i - 1][j - 1] + match == a[i][j]:
        path1[count] = seq1[j - 1]
        path2[count] = seq2[i - 1]
        find_global_alignment(a, gap, path1, path2, i - 1, j - 1, count + 1)
    elif i - 1 >= 0 and j - 1 >= 0 and seq2[i - 1] != seq1[j - 1] and a[i - 1][j - 1] + mismatch == a[i][j]:
        path1[count] = seq1[j - 1]
        path2[count] = seq2[i - 1]
        find_global_alignment(a, gap, path1, path2, i - 1, j - 1, count + 1)
    if i - 1 >= 0 and a[i - 1][j] + gap == a[i][j]:
        path1[count] = '-'
        path2[count] = seq2[i - 1]
        find_global_alignment(a, gap, path1, path2, i - 1, j, count + 1)
    if j - 1 >= 0 and a[i][j - 1] + gap == a[i][j]:
        path1[count] = seq1[j - 1]
        path2[count] = '-'
        find_global_alignment(a, gap, path1, path2, i, j - 1, count + 1)


def find_local_alignment(a, gap, path1, path2, i, j, count):
    # when a 0 valued cell is reached that gives us an optimal path, however we still continue our
    # backtracking algorithm to check if there is a valid move from this 0 and if there is, it will
    # give us more paths
    if a[i][j] == 0:
        for k in range(count):
            print(path1[count - k - 1], end=" ")
        print()
        for k in range(count):
            if path1[count - k - 1] == path2[count - k - 1]:
                print("|", end=" ")
            else:
                print(" ", end=" ")
        print()
        for k in range(count):
            print(path2[count - k - 1], end=" ")
        print()
        print()
        if i - 1 >= 0 and j - 1 >= 0 and seq2[i - 1] == seq1[j - 1] and a[i - 1][j - 1] + match == a[i][j]:
            path1[count] = seq1[j - 1]
            path2[count] = seq2[i - 1]
            find_local_alignment(a, gap, path1, path2, i - 1, j - 1, count + 1)
        elif i - 1 >= 0 and j - 1 >= 0 and seq2[i - 1] != seq1[j - 1] and a[i - 1][j - 1] + mismatch == a[i][j]:
            path1[count] = seq1[j - 1]
            path2[count] = seq2[i - 1]
            find_local_alignment(a, gap, path1, path2, i - 1, j - 1, count + 1)
        if i - 1 >= 0 and a[i - 1][j] + gap == a[i][j]:
            path1[count] = '-'
            path2[count] = seq2[i - 1]
            find_local_alignment(a, gap, path1, path2, i - 1, j, count + 1)
        if j - 1 >= 0 and a[i][j - 1] + gap == a[i][j]:
            path1[count] = seq1[j - 1]
            path2[count] = '-'
            find_local_alignment(a, gap, path1, path2, i, j - 1, count + 1)
        return
    # checking for a match/mismatch and then doing a recursive call after making valid jump to
    # left, up, diagonally up any(>0) which gives valid solution
    # before recursive call, store the alignment step in the path
    if i - 1 >= 0 and j - 1 >= 0 and seq2[i - 1] == seq1[j - 1] and a[i - 1][j - 1] + match == a[i][j]:
        path1[count] = seq1[j - 1]
        path2[count] = seq2[i - 1]
        find_local_alignment(a, gap, path1, path2, i - 1, j - 1, count + 1)
    elif i - 1 >= 0 and j - 1 >= 0 and seq2[i - 1] != seq1[j - 1] and a[i - 1][j - 1] + mismatch == a[i][j]:
        path1[count] = seq1[j - 1]
        path2[count] = seq2[i - 1]
        find_local_alignment(a, gap, path1, path2, i - 1, j - 1, count + 1)
    if i - 1 >= 0 and a[i - 1][j] + gap == a[i][j]:
        path1[count] = '-'
        path2[count] = seq2[i - 1]
        find_local_alignment(a, gap, path1, path2, i - 1, j, count + 1)
    if j - 1 >= 0 and a[i][j - 1] + gap == a[i][j]:
        path1[count] = seq1[j - 1]
        path2[count] = '-'
        find_local_alignment(a, gap, path1, path2, i, j - 1, count + 1)


if __name__ == '__main__':
    # defining sequences, their lengths and the scoring scheme
    seq1 = 'ATCAGAGTA'
    seq2 = 'TTCAGTA'
    match = 2
    mismatch = -1
    gap_pen = -1
    n = len(seq2)
    m = len(seq1)
    # initializing storage variables
    path1 = [0 for i in range(m + n)]
    path2 = [0 for i in range(m + n)]
    g_matrix = numpy.zeros((n + 1, m + 1), dtype='int')
    l_matrix = numpy.zeros((n + 1, m + 1), dtype='int')
    # function calls for creation of the matrices for q1 and q2
    global_alignment(g_matrix, gap_pen)
    local_alignment(l_matrix, gap_pen)
    print("Question 1:")
    print()
    print("Dynamic Programming matrix for global alignment is:")
    print()
    print(end="          ")
    print(" ".join(["{:<{mx}}".format(ele, mx=5) for ele in seq1]))
    k = 0
    # printing the formatted global alignment matrix
    for row in g_matrix:
        if len(seq2) >= k > 0:
            print(seq2[k - 1], end="  ")
        k += 1
        if k == 1:
            print("   ", end="")
        print(" ".join(["{:<{mx}}".format(ele, mx=5) for ele in row]))
    print()
    print("Following are the optimal alignment(s) with a best score of", g_matrix[n][m], ":")
    print()
    # function call for getting optimal solutions
    find_global_alignment(g_matrix, gap_pen, path1, path2, n, m, 0)
    cur_max = 0

    for i in range(n + 1):
        for j in range(m + 1):
            cur_max = max(cur_max, l_matrix[i][j])
    print("Question 2:")
    print()
    print("Dynamic Programming matrix for local alignment is:")
    print()
    print(end="         ")
    print(" ".join(["{:<{mx}}".format(ele, mx=5) for ele in seq1]))
    k = 0
    # printing the formatted local alignment matrix
    for row in l_matrix:
        if len(seq2) >= k > 0:
            print(seq2[k - 1], end="  ")
        k += 1
        if k == 1:
            print("   ", end="")
        print(" ".join(["{:<{mx}}".format(ele, mx=5) for ele in row]))
    print()
    print("Following are the optimal alignment(s) with a best score of", cur_max, ":")
    print()
    # function call(s) for getting optimal solutions
    for i in range(n + 1):
        for j in range(m + 1):
            if l_matrix[i][j] == cur_max:
                find_local_alignment(l_matrix, gap_pen, path1, path2, i, j, 0)
    # updating value of gap penalty for q4
    gap_pen = -2
    # function calls for creation of the matrices for q4
    global_alignment(g_matrix, gap_pen)
    local_alignment(l_matrix, gap_pen)
    print("Question 4:")
    print()
    print("Dynamic Programming matrix for global alignment is:")
    print()
    print(end="          ")
    print(" ".join(["{:<{mx}}".format(ele, mx=5) for ele in seq1]))
    k = 0
    # printing the formatted global alignment matrix
    for row in g_matrix:
        if len(seq2) >= k > 0:
            print(seq2[k - 1], end="  ")
        k += 1
        if k == 1:
            print("   ", end="")
        print(" ".join(["{:<{mx}}".format(ele, mx=5) for ele in row]))
    print()
    print("Following are the optimal alignment(s) with a best score of", g_matrix[n][m], ":")
    print()
    # function call for getting optimal solutions
    find_global_alignment(g_matrix, gap_pen, path1, path2, n, m, 0)
    cur_max = 0
    for i in range(n + 1):
        for j in range(m + 1):
            cur_max = max(cur_max, l_matrix[i][j])
    print("Dynamic Programming matrix for local alignment is:")
    print()
    print(end="         ")
    print(" ".join(["{:<{mx}}".format(ele, mx=5) for ele in seq1]))
    k = 0
    # printing the formatted local alignment matrix
    for row in l_matrix:
        if len(seq2) >= k > 0:
            print(seq2[k - 1], end="  ")
        k += 1
        if k == 1:
            print("   ", end="")
        print(" ".join(["{:<{mx}}".format(ele, mx=5) for ele in row]))
    print()
    print("Following are the optimal alignment(s) with a best score of", cur_max, ":")
    print()
    # function call(s) for getting optimal solutions
    for i in range(n + 1):
        for j in range(m + 1):
            if l_matrix[i][j] == cur_max:
                find_local_alignment(l_matrix, gap_pen, path1, path2, i, j, 0)
