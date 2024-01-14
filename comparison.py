import timeit
import random


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи,
    # додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def insertion_sort(lst):
    lst = lst[:]  # lst = lst.copy()
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


if __name__ == "__main__":
    data_small = [random.randint(0, 100) for _ in range(100)]
    data_medium = [random.randint(0, 1000) for _ in range(1000)]
    data_large = [random.randint(0, 10000) for _ in range(10000)]

    time_small_insertion = timeit.timeit(
        lambda: insertion_sort(data_small[:]), number=5
    )
    time_small_merge = timeit.timeit(lambda: merge_sort(data_small[:]), number=5)
    time_small_timsort_sorted = timeit.timeit(lambda: sorted(data_small[:]), number=5)
    time_small_timsort_sort = timeit.timeit(lambda: data_small[:].sort(), number=5)

    time_medium_insertion = timeit.timeit(
        lambda: insertion_sort(data_medium[:]), number=5
    )
    time_medium_merge = timeit.timeit(lambda: merge_sort(data_medium[:]), number=5)
    time_medium_timsort_sorted = timeit.timeit(lambda: sorted(data_medium[:]), number=5)
    time_medium_timsort_sort = timeit.timeit(lambda: data_medium[:].sort(), number=5)

    time_large_insertion = timeit.timeit(
        lambda: insertion_sort(data_large[:]), number=5
    )
    time_large_merge = timeit.timeit(lambda: merge_sort(data_large[:]), number=5)
    time_large_timsort_sorted = timeit.timeit(lambda: sorted(data_large[:]), number=5)
    time_large_timsort_sort = timeit.timeit(lambda: data_large[:].sort(), number=5)

    print(
        f"{'| Algorithm': <20} | {'Time small data': <20} | {'Time medium data': <20} | {'Time large data': <20}"
    )
    print(f":{'-'*19} | :{'-'*19} | :{'-'*19} | :{'-'*19}")
    print(
        f"{'| Insertion sort': <20} | {time_small_insertion:<20.5f} | {time_medium_insertion:<20.5f} | {time_large_insertion:<20.5f}"
    )
    print(
        f"{'| Merge sort': <20} | {time_small_merge:<20.5f} | {time_medium_merge:<20.5f} | {time_large_merge:<20.5f}"
    )
    print(
        f"{'| Timsort sorted': <20} | {time_small_timsort_sorted:<20.5f} | {time_medium_timsort_sorted:<20.5f} | {time_large_timsort_sorted:<20.5f}"
    )
    print(
        f"{'| Timsort sort': <20} | {time_small_timsort_sort:<20.5f} | {time_medium_timsort_sort:<20.5f} | {time_large_timsort_sort:<20.5f}"
    )
