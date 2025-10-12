def reverse_sort_dictionary(dict):
    keys = list(dict.keys())

    for i in range(len(keys)):
        max_index = i
        for j in range(i+1, len(keys)):
            if keys[j] > keys[max_index]:
                max_index = j
        keys[i], keys[max_index] = keys[max_index], keys[i]
    result = [(name, dict[name][0]) for name in keys]
    return result      