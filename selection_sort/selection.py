def selection_sort(unsorted):
    """
    """
    if type(unsorted) is not list:
        raise TypeError('input argument must be list')

    for i in range(len(unsorted)):
        min_val = i

        for temp in range(i + 1, len(unsorted)):
            if unsorted[temp] < unsorted[min_val]:
                min_val = temp
        unsorted[i], unsorted[min_val] = unsorted[min_val], unsorted[i]
    return unsorted
