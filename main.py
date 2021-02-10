import numpy


def global_alignment(a):
    for i in range(1, n + 1):
        a[i][0] = -i
    for i in range(1, m + 1):
        a[0][i] = -i
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if seq2[i - 1] == seq1[j - 1]:
                a[i][j] = max(a[i - 1][j - 1] + match, a[i - 1][j] + gap, a[i][j - 1] + gap)
            else:
                a[i][j] = max(a[i - 1][j - 1] + mismatch, a[i - 1][j] + gap, a[i][j - 1] + gap)


def local_alignment(a):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if seq2[i - 1] == seq1[j - 1]:
                a[i][j] = max(0, a[i - 1][j - 1] + match, a[i - 1][j] + gap, a[i][j - 1] + gap)
            else:
                a[i][j] = max(0, a[i - 1][j - 1] + mismatch, a[i - 1][j] + gap, a[i][j - 1] + gap)


def find_global_alignment(a, path1, path2, i, j, count):
    if i == 0:
        for k in range(1, j+1):
            if(a[0][j-k]==a[0][j-k-1]):
                path1[count + k] = seq1[j-k-1]
                path2[count+k] = '-'
            else:
                return
        for k in range(count + j+1):
            print(path1[count+j-k], end=" ")
        print()
        for k in range(count + j + 1):
            print(path2[count+j-k], end=" ")
        print()
        print()
        return
    if j == 0:
        for k in range(1, i):
            if (a[i-k][0] == a[i-k-1][0]):
                path1[count + k] = '-'
                path2[count+k]=seq2[i-k-1]
            else:
                return

        for k in range(count + i):
            print(path1[count+i-k], end=" ")
        print()
        for k in range(count + i):
            print(path2[count+i-k], end=" ")
        print()
        print()
        return

    path1[count] = a[i][j]
    if i - 1 >= 0 and j - 1 >= 0 and seq2[i - 1] == seq1[j - 1] and a[i - 1][j - 1] + match == a[i][j]:
        path1[count] = seq1[j-1]
        path2[count] = seq2[i-1]
        find_global_alignment(a, path1,path2, i - 1, j - 1, count + 1)
    elif i - 1 >= 0 and j - 1 >= 0 and seq2[i - 1] != seq1[j - 1] and a[i - 1][j - 1] + mismatch == a[i][j]:
        path1[count] = seq1[j - 1]
        path2[count] = seq2[i - 1]
        find_global_alignment(a, path1,path2, i - 1, j - 1, count + 1)
    if i - 1 >= 0 and a[i - 1][j] + gap == a[i][j]:
        path1[count] = '-'
        path2[count] = seq2[i - 1]
        find_global_alignment(a, path1, path2, i - 1, j, count + 1)
    if j - 1 >= 0 and a[i][j - 1] + gap == a[i][j]:
        path1[count] = seq1[j - 1]
        path2[count] = '-'
        find_global_alignment(a, path1, path2, i, j - 1, count + 1)

def find_local_alignment(a, path1, path2, i, j, count):
    if(a[i][j]==0):
        for k in range(count):
            print(path1[count-k-1], end=" ")
        print()
        for k in range(count):
            print(path2[count-k-1], end=" ")
        print()
        print()
        return
    path1[count] = a[i][j]
    if i - 1 >= 0 and j - 1 >= 0 and seq2[i - 1] == seq1[j - 1] and a[i - 1][j - 1] + match == a[i][j]:
        path1[count] = seq1[j-1]
        path2[count] = seq2[i-1]
        find_local_alignment(a, path1,path2, i - 1, j - 1, count + 1)
    elif i - 1 >= 0 and j - 1 >= 0 and seq2[i - 1] != seq1[j - 1] and a[i - 1][j - 1] + mismatch == a[i][j]:
        path1[count] = seq1[j - 1]
        path2[count] = seq2[i - 1]
        find_local_alignment(a, path1,path2, i - 1, j - 1, count + 1)
    if i - 1 >= 0 and a[i - 1][j] + gap == a[i][j]:
        path1[count] = '-'
        path2[count] = seq2[i - 1]
        find_local_alignment(a, path1, path2, i - 1, j, count + 1)
    if j - 1 >= 0 and a[i][j - 1] + gap == a[i][j]:
        path1[count] = seq1[j - 1]
        path2[count] = '-'
        find_local_alignment(a, path1, path2, i, j - 1, count + 1)

if __name__ == '__main__':
    seq1 = 'ATCAGAGTA'
    seq2 = 'TTCAGTA'
    match = 2
    mismatch = -1
    gap = -1
    n = len(seq2)
    m = len(seq1)
    g_matrix = numpy.zeros((n + 1, m + 1), dtype='int')
    global_alignment(g_matrix)
    l_matrix = numpy.zeros((n + 1, m + 1), dtype='int')
    local_alignment(l_matrix)
    print(g_matrix)
    print()
    print(l_matrix)
    path1 = ['' for i in range(m + n)]
    path2 = ['' for i in range(m + n)]
    cur_max=0
    for i in range (n+1):
        for j in range (m+1):
            cur_max=max(cur_max,l_matrix[i][j])
    for i in range (n+1):
        for j in range (m+1):
            if l_matrix[i][j]==cur_max:
                find_local_alignment(l_matrix, path1, path2, i, j, 0)

    find_global_alignment(g_matrix, path1, path2, n, m, 0)













