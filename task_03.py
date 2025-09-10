import random
import timeit
from insertion_sort import insertion_sort
from merge_sort import merge_sort


def test_algorithms(sizes):
    for n in sizes:
        sample_list = [random.randint(0, 100000) for _ in range(n)]
        print(f"\n--- Тест для n = {n} ---")

        # Insertion Sort (O(n^2))
        insertion_time = timeit.timeit(lambda: insertion_sort(sample_list[:]), number=1)
        print(f"Час виконання (вставки): {insertion_time:.6f} сек")

        # Merge Sort (O(n log n))
        merge_time = timeit.timeit(lambda: merge_sort(sample_list[:]), number=1)
        print(f"Час виконання (злиття): {merge_time:.6f} сек")

        # Timsort (O(n log n), але з оптимізаціями)
        timsort_time = timeit.timeit(lambda: sorted(sample_list[:]), number=1)
        print(f"Час виконання (Timsort): {timsort_time:.6f} сек")


if __name__ == "__main__":
    sizes = [10, 100, 1000, 10000, 50000]
    test_algorithms(sizes)
