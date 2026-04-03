# 3 Highest Value Longest Common Sequence

Davis Pham 38499319

to compile/build run:
# 3.-HVL


To run the program on an input file:
python3 src/main.py < tests/test1.in

To run example:
python3 src/main.py < example/example.in

To run the runtime test:
python3 tests/test.py

Assumptions:

The input is:
K
x1 v1
x2 v2
...
xK vK
A
B

outputs:
the maximum value of a common subsequence of A and B
optimal subsequence for that value

Question 1:
Input Size    Runtime
25           0.00010564
30           0.00013674
35           0.00018222
40           0.00024248
45           0.00030106
50           0.00037034
55           0.00044688
60           0.00052218
65           0.00061188
70           0.00071085
The runtime increases steadily as input size grows, which matches the expected O(nm)
The graph is saved as runtime_graph.png.

Question 2: Recurrence Equation:
```
Let M[i][j] represent the maximum value of a common subsequence.

Base if either string has length 0, then there is no common subsequence and value is 0
M[0][j] = 0 and M[i][0] = 0

Recurrence:
when A[i - 1] != B[j - 1] : M[i][j] = max(M[i - 1][j], M[i][j - 1])

when A[i - 1] == B[j - 1]:
M[i][j] = max(M[i - 1][j], M[i][j - 1], M[i - 1][j - 1] + vals[A[i - 1]])

This recurrence is correct because the optimal solution must come from one of these cases.
If the characters are different, they cannot both be used at that position.
If they are the same, the solution can either use the match or ignore it.

```

Question 3:

create table M of size (n + 1) x (m + 1)
The first row and first column are 0 for the base cases.
Then the algorithm loops through every pair of indices i and j.
At each position, it compares the current characters of the two strings.
It then uses the recurrence to fill in M[i][j]. the maximum value is stored in M[n][m]:
```
    for i from 1 to n:
        for j from 1 to m:
            if A[i - 1] != B[j - 1]:
                M[i][j] = max(M[i - 1][j], M[i][j - 1])
            else:
                M[i][j] = max(M[i - 1][j], M[i][j - 1], M[i - 1][j - 1] + vals[A[i - 1]])

    return M[n][m]
```

backtracking starts at M[n][m] and moves backward through the table to make subseq

The runtime for filling the table is O(nm).
there are (n + 1)(m + 1) entries and each one computes in constant time
The backtracking takes O(n + m).
so total runtime is still O(nm).
