#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        add = 0
        try:
            add = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError, TypeError, IndexError) as er:
            if isinstance(er, ZeroDivisionError):
                print("division by 0")
            elif isinstance(er, TypeError):
                print("wrong type")
            elif isinstance(er, IndexError):
                print("out of range")
        finally:
            new_list.append(add)
    return new_list
