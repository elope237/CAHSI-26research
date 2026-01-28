import math
import matplotlib.pyplot as plt


# Linear search (average-case)
def steps_linear_avg(n: int) -> float:
    return (n + 1) / 2

# Binary search (average-case)
def steps_binary_avg(n: int) -> int:
    return math.ceil(math.log2(n)) if n > 1 else 1

# Hash table (Python dict) average-case
def steps_hash_avg(_: int) -> int:
    return 1  # average O(1)


def main():
    Ns = [10, 30, 100, 300, 1_000, 3_000, 10_000, 30_000, 100_000, 300_000, 1_000_000]

    # ---- Ledger (table) ----
    ledger = [
        {"Method": "Brute force (linear search)", "Big-O": "O(n)"},
        {"Method": "Binary search",               "Big-O": "O(log n)"},
        {"Method": "Hash dict lookup",            "Big-O": "O(1)"},
    ]

    print("\nLedger:")
    print(f"{'Method':30} | {'Big-O':8}")
    print("-" * 43)
    for row in ledger:
        print(f"{row['Method'][:30]:30} | {row['Big-O']:8}")

    # ---- Compute average step curves ----
    lin_avg = [steps_linear_avg(n) for n in Ns]
    bin_avg = [steps_binary_avg(n) for n in Ns]
    hsh_avg = [steps_hash_avg(n) for n in Ns]

    # ---- Plot ----
    plt.figure(figsize=(9, 5))
    plt.plot(Ns, lin_avg, marker="o", label="Brute force (linear search) O(n)")
    plt.plot(Ns, bin_avg, marker="o", label="Binary search O(log n)")
    plt.plot(Ns, hsh_avg, marker="o", label="Hash dict O(1)")

    plt.xscale("log")
    #plt.xlim(1, max(Ns))
    plt.yscale("log")
    plt.minorticks_off()  # REMOVE mid / minor tick markers
    plt.xlabel("N (number of size)")
    plt.ylabel("Steps (comparisons)")
    plt.title("Steps vs N")
    plt.grid(True, alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
