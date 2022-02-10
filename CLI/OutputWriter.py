symbols = ["\033[32m {}".format(" "),
           "\033[31m {}".format("1"),
           "\033[31m {}".format("2"),
           "\033[37m {}".format("∎"),
           "\033[33m {}".format("∎"),
           "\033[33m {}".format("#")]

def rows(field):
    counter_1 = 0
    counter_2 = 0
    for row in field:
        if row[0] == 0 or row[0] == 1 or row[0] == 2:
            if counter_2 < 10:
                print(f"{counter_2}  {counter_1}{row}")
                counter_1 += 1
                counter_2 += 1
            else:
                print(f"{counter_2} {counter_1}{row}")
                counter_1 += 1
                counter_2 += 1

        else:
            if counter_2 < 10:
                print(f"{counter_2}   {row}")
                counter_2 += 1
            else:
                print(f"{counter_2}  {row}")
                counter_2 += 1

def horizontal(field):
    a = 1
    if a == 0:
        horizontal(field)
        rows(field)
    else:
        for index, i in enumerate(field):
            for index2, j in enumerate(i):
                print(symbols[j], end="")
            print()
    pass



