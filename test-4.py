
#2
import cProfile


def sbpch_calc():

    i = int(input('До какого числа считать изволите? '))

    inp_set = set(range(2, i+1))

    while inp_set:
        
        search_num = min(inp_set)
        
        print(search_num, end = '\t')

        tmp_set = set(range(search_num, i+1, search_num))

        inp_set -= tmp_set


cProfile.run('sbpch_calc()')

'''

До какого числа считать изволите? 2000
2	3	5	7	11	13	17	19
23	29	31	37	41	43	47	53
59	61	67	71	73	79	83	89
97	101	103	107	109	113	127	131
137	139	149	151	157	163	167	173
179	181	191	193	197	199	211	223
227	229	233	239	241	251	257	263
269	271	277	281	283	293	307	311
313	317	331	337	347	349	353	359
367	373	379	383	389	397	401	409
419	421	431	433	439	443	449	457
461	463	467	479	487	491	499	503
509	521	523	541	547	557	563	569
571	577	587	593	599	601	607	613
617	619	631	641	643	647	653	659
661	673	677	683	691	701	709	719
727	733	739	743	751	757	761	769
773	787	797	809	811	821	823	827
829	839	853	857	859	863	877	881
883	887	907	911	919	929	937	941
947	953	967	971	977	983	991	997
1009	1013	1019	1021	1031	1033	1039	1049
1051	1061	1063	1069	1087	1091	1093	1097
1103	1109	1117	1123	1129	1151	1153	1163
1171	1181	1187	1193	1201	1213	1217	1223
1229	1231	1237	1249	1259	1277	1279	1283
1289	1291	1297	1301	1303	1307	1319	1321
1327	1361	1367	1373	1381	1399	1409	1423
1427	1429	1433	1439	1447	1451	1453	1459
1471	1481	1483	1487	1489	1493	1499	1511
1523	1531	1543	1549	1553	1559	1567	1571
1579	1583	1597	1601	1607	1609	1613	1619
1621	1627	1637	1657	1663	1667	1669	1693
1697	1699	1709	1721	1723	1733	1741	1747
1753	1759	1777	1783	1787	1789	1801	1811
1823	1831	1847	1861	1867	1871	1873	1877
1879	1889	1901	1907	1913	1931	1933	1949
1951	1973	1979	1987	1993	1997	1999

33484 function calls in 11.914 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   11.914   11.914 <string>:1(<module>)
     4263    0.001    0.000    0.001    0.000 rpc.py:153(debug)
      609    0.001    0.000   11.899    0.020 rpc.py:216(remotecall)
      609    0.003    0.000    0.046    0.000 rpc.py:226(asynccall)
      609    0.003    0.000   11.851    0.019 rpc.py:246(asyncreturn)
      609    0.000    0.000    0.000    0.000 rpc.py:252(decoderesponse)
      609    0.001    0.000   11.848    0.019 rpc.py:290(getresponse)
      609    0.001    0.000    0.001    0.000 rpc.py:298(_proxify)
      609    0.007    0.000   11.846    0.019 rpc.py:306(_getresponse)
      609    0.000    0.000    0.000    0.000 rpc.py:328(newseq)
      609    0.004    0.000    0.039    0.000 rpc.py:332(putmessage)
      608    0.001    0.000    0.002    0.000 rpc.py:559(__getattr__)
      609    0.003    0.000    0.005    0.000 rpc.py:57(dumps)
        1    0.000    0.000    0.001    0.001 rpc.py:577(__getmethods)
      608    0.000    0.000    0.000    0.000 rpc.py:601(__init__)
      608    0.001    0.000   11.899    0.020 rpc.py:606(__call__)
     1214    0.000    0.000    0.000    0.000 run.py:420(encoding)
     1214    0.000    0.000    0.000    0.000 run.py:424(errors)
      607    0.004    0.000    3.867    0.006 run.py:441(write)
        1    0.000    0.000    8.040    8.040 run.py:477(readline)
        1    0.002    0.002   11.914   11.914 test-4.py:11(sbpch_calc)
     1218    0.001    0.000    0.001    0.000 threading.py:1306(current_thread)
      609    0.002    0.000    0.003    0.000 threading.py:222(__init__)
      609    0.002    0.000   11.838    0.019 threading.py:270(wait)
      609    0.001    0.000    0.001    0.000 threading.py:81(RLock)
      609    0.000    0.000    0.000    0.000 {built-in method _struct.pack}
      609    0.001    0.000    0.001    0.000 {built-in method _thread.allocate_lock}
     1218    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        1    0.000    0.000   11.914   11.914 {built-in method builtins.exec}
        1    0.000    0.000    8.042    8.042 {built-in method builtins.input}
     1219    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
     1828    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      303    0.004    0.000    0.004    0.000 {built-in method builtins.min}
      303    0.001    0.000    3.866    0.013 {built-in method builtins.print}
      609    0.005    0.000    0.005    0.000 {built-in method select.select}
      609    0.001    0.000    0.001    0.000 {method '_acquire_restore' of '_thread.RLock' objects}
      609    0.000    0.000    0.000    0.000 {method '_is_owned' of '_thread.RLock' objects}
      609    0.000    0.000    0.000    0.000 {method '_release_save' of '_thread.RLock' objects}
      609    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
     1218   11.833    0.010   11.833    0.010 {method 'acquire' of '_thread.lock' objects}
      609    0.000    0.000    0.000    0.000 {method 'append' of 'collections.deque' objects}
      607    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      609    0.003    0.000    0.003    0.000 {method 'dump' of '_pickle.Pickler' objects}
      607    0.000    0.000    0.000    0.000 {method 'encode' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
      608    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
      609    0.000    0.000    0.000    0.000 {method 'getvalue' of '_io.BytesIO' objects}
      609    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
      609    0.023    0.000    0.023    0.000 {method 'send' of '_socket.socket' objects}До какого числа считать изволите? 2000
2	3	5	7	11	13	17	19	23	29	31	37	41	43	47	53	59	61	67	71	73	79	83	89	97	101	103	107	109	113	127	131	137	139	149	151	157	163	167	173	179	181	191	193	197	199	211	223	227	229	233	239	241	251	257	263	269	271	277	281	283	293	307	311	313	317	331	337	347	349	353	359	367	373	379	383	389	397	401	409	419	421	431	433	439	443	449	457	461	463	467	479	487	491	499	503	509	521	523	541	547	557	563	569	571	577	587	593	599	601	607	613	617	619	631	641	643	647	653	659	661	673	677	683	691	701	709	719	727	733	739	743	751	757	761	769	773	787	797	809	811	821	823	827	829	839	853	857	859	863	877	881	883	887	907	911	919	929	937	941	947	953	967	971	977	983	991	997	1009	1013	1019	1021	1031	1033	1039	1049	1051	1061	1063	1069	1087	1091	1093	1097	1103	1109	1117	1123	1129	1151	1153	1163	1171	1181	1187	1193	1201	1213	1217	1223	1229	1231	1237	1249	1259	1277	1279	1283	1289	1291	1297	1301	1303	1307	1319	1321	1327	1361	1367	1373	1381	1399	1409	1423	1427	1429	1433	1439	1447	1451	1453	1459	1471	1481	1483	1487	1489	1493	1499	1511	1523	1531	1543	1549	1553	1559	1567	1571	1579	1583	1597	1601	1607	1609	1613	1619	1621	1627	1637	1657	1663	1667	1669	1693	1697	1699	1709	1721	1723	1733	1741	1747	1753	1759	1777	1783	1787	1789	1801	1811	1823	1831	1847	1861	1867	1871	1873	1877	1879	1889	1901	1907	1913	1931	1933	1949	1951	1973	1979	1987	1993	1997	1999	         33484 function calls in 11.914 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   11.914   11.914 <string>:1(<module>)
     4263    0.001    0.000    0.001    0.000 rpc.py:153(debug)
      609    0.001    0.000   11.899    0.020 rpc.py:216(remotecall)
      609    0.003    0.000    0.046    0.000 rpc.py:226(asynccall)
      609    0.003    0.000   11.851    0.019 rpc.py:246(asyncreturn)
      609    0.000    0.000    0.000    0.000 rpc.py:252(decoderesponse)
      609    0.001    0.000   11.848    0.019 rpc.py:290(getresponse)
      609    0.001    0.000    0.001    0.000 rpc.py:298(_proxify)
      609    0.007    0.000   11.846    0.019 rpc.py:306(_getresponse)
      609    0.000    0.000    0.000    0.000 rpc.py:328(newseq)
      609    0.004    0.000    0.039    0.000 rpc.py:332(putmessage)
      608    0.001    0.000    0.002    0.000 rpc.py:559(__getattr__)
      609    0.003    0.000    0.005    0.000 rpc.py:57(dumps)
        1    0.000    0.000    0.001    0.001 rpc.py:577(__getmethods)
      608    0.000    0.000    0.000    0.000 rpc.py:601(__init__)
      608    0.001    0.000   11.899    0.020 rpc.py:606(__call__)
     1214    0.000    0.000    0.000    0.000 run.py:420(encoding)
     1214    0.000    0.000    0.000    0.000 run.py:424(errors)
      607    0.004    0.000    3.867    0.006 run.py:441(write)
        1    0.000    0.000    8.040    8.040 run.py:477(readline)
        1    0.002    0.002   11.914   11.914 test-4.py:11(sbpch_calc)
     1218    0.001    0.000    0.001    0.000 threading.py:1306(current_thread)
      609    0.002    0.000    0.003    0.000 threading.py:222(__init__)
      609    0.002    0.000   11.838    0.019 threading.py:270(wait)
      609    0.001    0.000    0.001    0.000 threading.py:81(RLock)
      609    0.000    0.000    0.000    0.000 {built-in method _struct.pack}
      609    0.001    0.000    0.001    0.000 {built-in method _thread.allocate_lock}
     1218    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        1    0.000    0.000   11.914   11.914 {built-in method builtins.exec}
        1    0.000    0.000    8.042    8.042 {built-in method builtins.input}
     1219    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
     1828    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      303    0.004    0.000    0.004    0.000 {built-in method builtins.min}
      303    0.001    0.000    3.866    0.013 {built-in method builtins.print}
      609    0.005    0.000    0.005    0.000 {built-in method select.select}
      609    0.001    0.000    0.001    0.000 {method '_acquire_restore' of '_thread.RLock' objects}
      609    0.000    0.000    0.000    0.000 {method '_is_owned' of '_thread.RLock' objects}
      609    0.000    0.000    0.000    0.000 {method '_release_save' of '_thread.RLock' objects}
      609    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
     1218   11.833    0.010   11.833    0.010 {method 'acquire' of '_thread.lock' objects}
      609    0.000    0.000    0.000    0.000 {method 'append' of 'collections.deque' objects}
      607    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      609    0.003    0.000    0.003    0.000 {method 'dump' of '_pickle.Pickler' objects}
      607    0.000    0.000    0.000    0.000 {method 'encode' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
      608    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
      609    0.000    0.000    0.000    0.000 {method 'getvalue' of '_io.BytesIO' objects}
      609    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
      609    0.023    0.000    0.023    0.000 {method 'send' of '_socket.socket' objects}


'''      


    
    
    
