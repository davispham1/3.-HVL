import sys
from HVL import hvl, backtrack


def main():
    lines = [line.strip() for line in sys.stdin if line.strip()]

    K = int(lines[0])
    vals = {}

    for i in range(1, K + 1):
        ch, val = lines[i].split()
        vals[ch] = int(val)

    A = lines[K + 1]
    B = lines[K + 2]

    M = hvl(vals, A, B)
    subseq = backtrack(M, vals, A, B)

    print(M[len(A)][len(B)])
    print(subseq)



if __name__ == "__main__":
    main()