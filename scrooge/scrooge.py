def calculate_years(principal, interest, tax, desired):
    # raise NotImplementedError("TODO: calculate_years")
    p = principal
    ir = float(1 + interest)
    tr = float(1 + tax)
    y = 0
    while p < desired:
        p = (p * ir) / tr
        y += 1
    return y

print(calculate_years(1000, .5, .2, 10000))