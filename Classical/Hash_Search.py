"""
Hash-based search using dict.
Shows absolute timings for dict lookups (hit/miss) and linear scans (hit/miss).
"""

from typing import Iterable, List
import time
import random


def build_index_dict(keys: Iterable):
    """Return a dictionary that maps key to index."""
    return {k: i for i, k in enumerate(keys)}


def linear_search(arr: List, target):
    """Return index of target in arr or -1 if not found (simple linear scan)."""
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1


def time_func(fn, repeats: int):
    """Time calling fn() repeats times; return average time per call (seconds)."""
    t0 = time.perf_counter()
    for _ in range(repeats):
        fn()
    t1 = time.perf_counter()
    total = t1 - t0
    return total / repeats


def demo_hash_vs_linear(sizes: List[int], repeats_dict: int = 2000, repeats_linear: int = 50):
    """
    For each array size in sizes:
      - build array of ints [0 .. n-1]
      - build dict index
      - measure dict.get() for a hit and a miss (average time per call)
      - measure linear_search() for a hit and a miss (average time per call)
    """
    rng = random.Random(0)
    
    print("\n")
    # dict timings in micro-seconds, linear in milli-seconds
    # n is the number of items in the dataset (the size of the list/dict)
    print(f"{'n':>10} | {'dict_hit (us)':>13} | {'dict_miss (us)':>14} | "
          f"{'lin_hit (ms)':>12} | {'lin_miss (ms)':>13}")
    
    print("-" * 75)

    for n in sizes:
        data = list(range(n))
        idx = build_index_dict(data)

        hit = n - 1 if n > 0 else None
        miss = n + 12345

        # dict timings (use get which returns -1 if missing)
        dict_hit_avg = time_func(lambda: idx.get(hit, -1), repeats_dict)
        dict_miss_avg = time_func(lambda: idx.get(miss, -1), repeats_dict)

        # linear timings (fewer repeats for linear)
        lin_hit_avg = time_func(lambda: linear_search(data, hit), max(1, repeats_linear))
        lin_miss_avg = time_func(lambda: linear_search(data, miss), max(1, repeats_linear))

        # Convert units for readability
        dict_hit_us = dict_hit_avg * 1e6
        dict_miss_us = dict_miss_avg * 1e6
        lin_hit_ms = lin_hit_avg * 1e3
        lin_miss_ms = lin_miss_avg * 1e3

        print(f"{n:10,} | {dict_hit_us:13.3f} | {dict_miss_us:14.3f} | "
              f"{lin_hit_ms:12.3f} | {lin_miss_ms:13.3f}")


if __name__ == "__main__":
    sizes_to_test = [1_000, 10_000, 100_000, 300_000]
    
    # play with repeats as needed to show timing differences
    demo_hash_vs_linear(sizes_to_test, repeats_dict=1000, repeats_linear=1000) 

    # demo examples
    items = ["apple", "banana", "cherry"] #["item 0", "item 1", "item 2", ...]
    index_map = build_index_dict(items)
    print("\nExample dictionary index:" , index_map)
    key = "banana" 
    print(f"Lookup '{key}' = index {index_map.get(key, -1)} ")
    print("\n")