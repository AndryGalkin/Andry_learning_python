'''
Python 3.8.10

Win 7, x64

'''

from memory_profiler import profile
#import sys
#from resource import *

@profile
def sbpch_calc(inp_data):

    result_list = []

    #i = int(input('До какого числа считать изволите? '))
    i = int(inp_data)

    inp_set = set(range(2, i+1))

    while inp_set:
        
        search_num = min(inp_set)
        result_list.append(search_num)
        #print(search_num, end = '\t')

        tmp_set = set(range(search_num, i+1, search_num))

        inp_set -= tmp_set

    #print(getrusage(RUSAGE_SELF))
    return result_list


#sbpch_calc(2000)


'''

Filename: D:\test-6.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     5     25.1 MiB     25.1 MiB           1   @profile
     6                                         def sbpch_calc(inp_data):
     7                                         
     8     25.1 MiB      0.0 MiB           1       result_list = []
     9                                         
    10                                             #i = int(input('До какого числа считать изволите? '))
    11     25.1 MiB      0.0 MiB           1       i = int(inp_data)
    12                                         
    13     25.2 MiB      0.2 MiB           1       inp_set = set(range(2, i+1))
    14                                         
    15     25.3 MiB      0.0 MiB         304       while inp_set:
    16                                                 
    17     25.3 MiB      0.0 MiB         303           search_num = min(inp_set)
    18     25.3 MiB      0.0 MiB         303           result_list.append(search_num)
    19                                                 #print(search_num, end = '\t')
    20                                         
    21     25.3 MiB      0.1 MiB         303           tmp_set = set(range(search_num, i+1, search_num))
    22                                         
    23     25.3 MiB      0.0 MiB         303           inp_set -= tmp_set
    24                                         
    25                                             #print(getrusage(RUSAGE_SELF))
    26     25.3 MiB      0.0 MiB           1       return result_list

'''

#------------------------------------------------------------------------------


#5
@profile
def chr_ords():
    first_char = (ord(input('Первая буква: ')) - ord("a") + 1)
    last_char = (ord(input('Вторая буква: ')) - ord("a") + 1)

    print(first_char)
    print(last_char)
    print(f'Between: {last_char - first_char} letters')


chr_ords()



Первая буква: a
Вторая буква: Q
1
-15
Between: -16 letters

'''

Filename: D:\test-6.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    33     25.0 MiB     25.0 MiB           1   @profile
    34                                         def chr_ords():
    35     25.0 MiB      0.0 MiB           1       first_char = (ord(input('Первая буква: ')) - ord("a") + 1)
    36     25.0 MiB      0.0 MiB           1       last_char = (ord(input('Вторая буква: ')) - ord("a") + 1)
    37                                         
    38     25.0 MiB      0.0 MiB           1       print(first_char)
    39     25.0 MiB      0.0 MiB           1       print(last_char)
    40     25.0 MiB      0.0 MiB           1       print(f'Between: {last_char - first_char} letters')

'''
