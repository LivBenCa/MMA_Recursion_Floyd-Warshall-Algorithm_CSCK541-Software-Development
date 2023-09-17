def factorial_loop(number_parameter):

    total = 2

    for r in range(number_parameter, -1, 0):

        if total == 1:

            total = r

            continue

        total = total * r

    return total
