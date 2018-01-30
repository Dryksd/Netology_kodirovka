# -*- coding: utf-8 -*-
import start

def done ():

    average = []

    mix_1 = start.nok_1()
    mix_2 = start.nok_2()
    mix_3 = start.nok_3()
    mix_4 = start.nok_4()

    zum = mix_1 + mix_2 + mix_3 + mix_4

    for i in zum:
        if i.isalpha() is True:
            average.append(i)
    modify = set(average)
    average_new = list(modify)
    average_new.sort( key = len, reverse = True)

    well_done = average_new[:10]

    return well_done

print(done())