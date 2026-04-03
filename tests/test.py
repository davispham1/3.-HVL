import time
import os
import sys
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath("src"))

from HVL import hvl, backtrack

files = [f"tests/test{i}.in" for i in range(1, 11)]
sizes = []
times = []

for file in files:
    with open(file, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    K = int(lines[0])
    vals = {}

    for i in range(1, K + 1):
        ch, val = lines[i].split()
        vals[ch] = int(val)

    A = lines[K + 1]
    B = lines[K + 2]

    sizes.append(max(len(A), len(B)))

    runs = 20
    total = 0

    for _ in range(runs):
        start = time.perf_counter()
        M = hvl(vals, A, B)
        subseq = backtrack(M, vals, A, B)
        end = time.perf_counter()
        total += end - start

    avg_time = total / runs
    times.append(avg_time)

print("Input Size    Runtime")
for i in range(10):
    print(f"{sizes[i]:<13}{times[i]:.8f}")

plt.plot(sizes, times, marker="o")
plt.xlabel("Input Size")
plt.ylabel("Seconds")
plt.title("HVLCS Runtime")
plt.grid(True)
plt.savefig("runtime_graph.png")
plt.show()