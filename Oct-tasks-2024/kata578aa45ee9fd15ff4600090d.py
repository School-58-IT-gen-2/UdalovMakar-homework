def sort_array(source_array):
    odd = list(filter(lambda x: x % 2 != 0, source_array))
    odd = list(sorted(odd))
    n = 0
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = odd[n]
            n += 1
    return source_array