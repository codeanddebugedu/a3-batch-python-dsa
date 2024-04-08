def end_corona(recovers, new_cases, active_cases):
    count = 0
    while active_cases > 0:
        active_cases -= recovers
        active_cases += new_cases
        count += 1
    return count
