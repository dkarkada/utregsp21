import numpy as np #line:1
def read_data_key (O000O00O000O0O0OO ):#line:3
    OO0OO000OO0O0OOOO =[]#line:4
    OOO000OOOOOO00O00 =[]#line:5
    for OO0OO0OO00OO0OOO0 in O000O00O000O0O0OO :#line:6
        O0O000O0000O00OO0 =OO0OO0OO00OO0OOO0 .split ()#line:7
        OO0O0O0OO0O0OO0O0 =[float (O0OOOO0O0OO0O0O00 )for O0OOOO0O0OO0O0O00 in O0O000O0000O00OO0 [:4 ]]#line:8
        OO0OO000OO0O0OOOO .append (OO0O0O0OO0O0OO0O0 )#line:9
        OOOO0O0O0O0O0000O =O0O000O0000O00OO0 [4 ]if len (O0O000O0000O00OO0 )>4 else ""#line:10
        OOO000OOOOOO00O00 .append (OOOO0O0O0O0O0000O )#line:11
    return OO0OO000OO0O0OOOO ,OOO000OOOOOO00O00 #line:12
def k_means_key (OOO00OOOOOO0O000O ,OO0O00O00OO0O0O00 ):#line:14
    OOO00OOOOOO0O000O =np .array (OOO00OOOOOO0O000O )#line:15
    O0OO000OOO0OOOO00 =np .zeros ((11 ,2 ,2 ))#line:16
    O0OO000OOO0OOOO00 [0 ,:,:]=OO0O00O00OO0O0O00 #line:17
    O00000O00O00000OO =np .zeros (shape =len (OOO00OOOOOO0O000O ))#line:19
    for O0000OOOOO0OO00OO in range (10 ):#line:20
        OOO0O0O00O0OO0O00 ,OO00O00O0000O0OO0 =O0OO000OOO0OOOO00 [O0000OOOOO0OO00OO ]#line:21
        for O00OO0O00O0OOO00O ,OOO00O0OO00O0O0OO in enumerate (OOO00OOOOOO0O000O ):#line:22
            OO000O000O0O0OOO0 =np .linalg .norm (OOO00O0OO00O0O0OO -OOO0O0O00O0OO0O00 )>np .linalg .norm (OOO00O0OO00O0O0OO -OO00O00O0000O0OO0 )#line:23
            O00000O00O00000OO [O00OO0O00O0OOO00O ]=int (OO000O000O0O0OOO0 )#line:24
        O0OO000OOO0OOOO00 [O0000OOOOO0OO00OO +1 ,0 ,:]=np .mean (OOO00OOOOOO0O000O [O00000O00O00000OO ==0 ],axis =0 )#line:25
        O0OO000OOO0OOOO00 [O0000OOOOO0OO00OO +1 ,1 ,:]=np .mean (OOO00OOOOOO0O000O [O00000O00O00000OO ==1 ],axis =0 )#line:26
    return O0OO000OOO0OOOO00 #line:28
def feature_statistics_key (O0OOO00OOO0O00O0O ):#line:30
    def OO00OO000OO00O000 (O0OOO00OOO0OOOO0O ):#line:31
        O0OOO00OOO0OOOO0O =np .array (sorted (O0OOO00OOO0OOOO0O ))#line:32
        O0000O0O0O0000OO0 =len (O0OOO00OOO0OOOO0O )#line:33
        if O0000O0O0O0000OO0 %2 ==0 :#line:34
            return 1 /2 *(O0OOO00OOO0OOOO0O [O0000O0O0O0000OO0 //2 -1 ]+O0OOO00OOO0OOOO0O [O0000O0O0O0000OO0 //2 ])#line:35
        return O0OOO00OOO0OOOO0O [O0000O0O0O0000OO0 //2 ]#line:36
    O0OOO00OOO0O00O0O =np .array (O0OOO00OOO0O00O0O )#line:38
    O0OO0O0000O00OOO0 =OO00OO000OO00O000 (O0OOO00OOO0O00O0O )#line:39
    O0OOO0O000OOO00O0 =OO00OO000OO00O000 (O0OOO00OOO0O00O0O [O0OOO00OOO0O00O0O <O0OO0O0000O00OOO0 ])#line:40
    O0OO0000OO0O0000O =OO00OO000OO00O000 (O0OOO00OOO0O00O0O [O0OOO00OOO0O00O0O >O0OO0O0000O00OOO0 ])#line:41
    OO0O0O0000O0OO000 =np .abs (O0OOO00OOO0O00O0O -np .mean (O0OOO00OOO0O00O0O ))#line:42
    O000O0O00O00O0O0O =np .sum (OO0O0O0000O0OO000 >2 *np .std (O0OOO00OOO0O00O0O ))#line:43
    return (O0OO0O0000O00OOO0 ,O0OOO0O000OOO00O0 ,O0OO0000OO0O0000O ,O000O0O00O00O0O0O )#line:44
def get_cluster_features ():#line:46
	O0OO00O0OO0O00OOO =[]#line:47
	O0OO00O0OO0O00OOO .append ([list (np .linspace (1 ,2 ,2 ))])#line:48
	O0OO00O0OO0O00OOO .append ([list (np .linspace (1 ,2 ,51 ))])#line:49
	O0OO00O0OO0O00OOO .append ([[1.1 ,1.3 ,1.12 ,1.01 ,8.5 ,1.02 ,1.0 ,0.96 ,1.23 ]])#line:50
	O000OOOOO0O00OOO0 =np .random .default_rng (123 )#line:51
	OO0OO00OOO00OO0O0 =list (O000OOOOO0O00OOO0 .normal (3.4 ,0.3 ,256 ))+[5.1 ,4.98 ,4.61 ,0.23 ]#line:52
	O0OO00O0OO0O00OOO .append ([OO0OO00OOO00OO0O0 ])#line:53
	OO0OO00OOO00OO0O0 =list (O000OOOOO0O00OOO0 .normal (6.4 ,0.3 ,251 ))+[5.1 ,4.98 ,4.61 ,0.23 ]#line:54
	O0OO00O0OO0O00OOO .append ([OO0OO00OOO00OO0O0 ])#line:55
	return O0OO00O0OO0O00OOO #line:56