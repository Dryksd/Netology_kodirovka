#import chardet

def nok_1():
    list_1 = []
    with open('newsafr.txt','r', encoding='utf-8') as f:
        for line in f:
            sect = line.split(' ')
            for word in sect:
                if len(word) > 6:
                    list_1.append(word)
    return list_1


def nok_2():
    list_2 = []
    with open('newscy.txt','r', encoding='KOI8-R') as f:
        for line in f:
            sect = line.split(' ')
            for word in sect:
                if len(word) > 6:
                    list_2.append(word)
    return list_2

def nok_3():
    list_3 = []
    with open('newsfr.txt','r', encoding='ISO-8859-5') as f:
        for line in f:
            sect = line.split(' ')
            for word in sect:
                if len(word) > 6:
                    list_3.append(word)
    return list_3

def nok_4():
    list_4 = []
    with open('newsit.txt','r', encoding='windows-1251') as f:
        for line in f:
            sect = line.split(' ')
            for word in sect:
                if len(word) > 6:
                    list_4.append(word)
    return list_4








#enc = chardet.detect(tek
