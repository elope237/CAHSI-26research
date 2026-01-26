import matplotlib.pyplot as plt


def binary_search(arr, target):
    """
    Returns (index, steps).
    index = -1 if not found.
    steps = list of (lo, mid, hi) for visualization.
    """
    lo, hi = 0, len(arr) - 1
    steps = []

    while lo <= hi:
        mid = (lo + hi) // 2
        steps.append((lo, mid, hi))

        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1, steps


def plot_binary_search_steps(arr, target, steps, title="Binary Search Midpoint Selection"):
    # if no steps, nothing to plot
    if not steps:
        print("No steps to plot.")
        return

    x = list(range(len(arr)))
    y = [0] * len(arr)

    # one subplot per step, shared on x-axis
    fig, axes = plt.subplots(len(steps), 1, figsize=(10, max(2, 1.4 * len(steps))), sharex=True)
    if len(steps) == 1:
        axes = [axes]

    for i, (lo, mid, hi) in enumerate(steps):
        ax = axes[i]
        # base dots
        ax.scatter(x, y, s=60)
        # highlight mid
        ax.scatter([mid], [0], s=180, marker="o", label=f"mid={mid} (val={arr[mid]})")
        # highlight range
        ax.axvspan(lo - 0.5, hi + 0.5, alpha=0.15, label=f"search range [{lo},{hi}]")
        # axis
        ax.set_yticks([])
        ax.set_xlim(-0.5, len(arr) - 0.5)
        ax.set_title(f"Step {i+1}: lo={lo}, mid={(lo+hi)//2}, hi={hi}")

        # display values within the current search range
        for xi in range(lo, hi + 1):
            ax.text(xi, 0.02, str(arr[xi]), ha="center", va="bottom", fontsize=9)

        # move legend outside the axes on the right
        ax.legend(loc="center left", bbox_to_anchor=(1.01, 0.5), borderaxespad=0.)

    # title and layout adjustments
    fig.suptitle(f"{title}\nTarget={target}", y=0.98, fontsize=14)
    # make room on the right for the external legends
    fig.subplots_adjust(right=0.82, top=0.94, hspace=0.6)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # demo array and search
    arr = list(range(0, 33, 3))  # [0,3,6,...,30]
    idx, steps = binary_search(arr, 21)
    plot_binary_search_steps(arr, 21, steps)
    print("found index:", idx)
