def all_eq(a):
    m = max(len(x) for x in a)
    return [x + "_" * (m - len(x)) for x in a]
