# merge_sort_recursive.py : Program of sorting using merge sort through recursion.

# lst[low1]...lst[up1] and lst[low2]...lst[up2] merged to temp[low1]...temp[up2]
def merge(lst, temp, low1, up1, low2, up2):
    i = low1
    j = low2
    k = low1

    while i <= up1 and j <= up2:
        if lst[i] <= lst[j]:
            temp[k] = lst[i]
            i += 1
        else:
            temp[k] = lst[j]
            j += 1
        k += 1

    while i <= up1:
        temp[k] = lst[i]
        k += 1
        i += 1

    while j <= up2:
        temp[k] = lst[j]
        k += 1
        j += 1


def copy(lst, temp, low, up):
    i = low
    while i <= up:
        lst[i] = temp[i]
        i += 1


def merge_sort1(lst, temp, low, up):
    if low >= up:  # if only one element
        return

    mid = (low + up) // 2

    merge_sort1(lst, temp, low, mid)        # Sort lst[low]....lst[mid]
    merge_sort1(lst, temp, mid + 1, up)    # Sort lst[mid+1]....lst[up]

    # Merge lst[low]...lst[mid] and lst[mid+1]...lst[up] to temp[low]...temp[up]
    merge(lst, temp, low, mid, mid + 1, up)

    # Copy temp[low]...temp[up] to lst[low]...lst[up]
    copy(lst, temp, low, up)


def merge_sort(lst, n):
    temp = [None] * n
    merge_sort1(lst, temp, 0, n - 1)


if __name__ == '__main__':
    data_list = [8, 5, 89, 30, 42, 92, 64, 4, 21, 56, 3]

    print("Unsorted list is :")
    print(data_list)

    merge_sort(data_list, len(data_list))

    print("Sorted list is :")
    print(data_list)
