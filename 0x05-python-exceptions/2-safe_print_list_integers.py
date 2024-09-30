#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    size = 0

    for r in range(x):
        try:
            print("{:d}".format(my_list[r]), end='')
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            size += 1

    print()
    return (size)
