def series_resistance(lst):
    total = 0
    for i in lst:
        total += i
    unit = "ohms" if total > 1 else "ohm"
    return f"{total} {unit}"
    # unit = "s" if total > 1 else ""
    # return "{} ohm{}".format(total, unit)
