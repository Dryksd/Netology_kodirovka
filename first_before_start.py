# -*- coding: utf-8 -*-
import start
import collections

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

    return (collections.Counter(average).most_common(10))

print(done())