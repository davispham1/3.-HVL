def hvl(vals, A, B):
    n = len(A)
    m = len(B)

    M = [[0 for j in range(m + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] != B[j - 1]:
                M[i][j] = max(M[i-1][j], M[i][j-1])
            else:
                M[i][j] = max(M[i-1][j], M[i][j-1], M[i-1][j-1] + vals[A[i - 1]])

    return M

def backtrack(M, vals, A, B):
    n = len(A)
    m = len(B)

    i = n
    j = m
    subseq = []

    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1] and M[i][j] == M[i - 1][j - 1] + vals[A[i - 1]]:
            subseq.append(A[i - 1])
            i -= 1
            j -= 1
        elif M[i][j] == M[i - 1][j]:
            i -= 1
        else:
            j -= 1

    subseq.reverse()
    subseq = "".join(subseq)

    return subseq