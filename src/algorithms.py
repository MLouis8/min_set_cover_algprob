def naive_approx(u_size, s, s_size, seq):
    """implementation of a naive approx for solving minimum set cover problem"""
    taken = s
    for key in s.keys():
        for elem in s[key]
            if elem in seq:
                continue
        taken.pop(key)
    return len(taken)

# TODO finish the naive_approx