def num_layers(n):
    final = 0.0005
    for i in range(n):
        final += final

    return str(final) + "m"
