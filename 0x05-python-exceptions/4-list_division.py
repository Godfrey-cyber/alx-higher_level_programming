#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    current_list = []
    for x in range(list_length):
        try:
        outcome = my_list_1[i] / my_list_2[x]
        except ZeroDivisionError:
            print("division by 0")
            outcome = 0
        except TypeError:
            print("wrong type")
            outcome = 0
        except IndexError:
            print("out of range")
            outcome = 0
        finally:
            current_list.append(outcome)

    return (current_list)
