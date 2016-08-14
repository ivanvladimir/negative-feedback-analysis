# Codification

import numpy as np
import scipy.stats as stats
import scipy.special as special

def summary_q(q):
    h=np.bincount(q)
    for c,v in zip(range(len(h)),h):
        print "{0}: {1}".format(c,v)

def summary(exp):
    print "Question q1"
    summary_q(exp['q1'])
    print "Question q2"
    summary_q(exp['q2'])

def mix_q5(exp):
    exp['q5']=[]
    l=exp['q5']
    for i in range(len(exp['q5_s'])):
        if exp['q5_s'][i]==0 and exp['q5_d'][i]==0:
            l.append(0)
        elif exp['q5_d'][i]==1:
            l.append(1)
        elif exp['q5_s'][i]!=5:
            l.append(exp['q5_s'][i]+1)


def chi2(q_1,q_2,q_3,min=0,max=10):
    h_1=np.bincount(q_1,None,10)[min:max]
    h_2=np.bincount(q_2,None,10)[min:max]
    h_3=np.bincount(q_3,None,10)[min:max]
    print "Data"
    r_c_table=np.array([h_1,h_2,h_3])
    print r_c_table
    r_c_table=r_c_table[:, (r_c_table != 0).sum(axis=0) >= 1]
    print r_c_table
    res= stats.chi2_contingency(r_c_table)
    print """
Test statistic     : {0}
P-value            : {1}
Degrees of freedom : {2}
Expected           : {3} """.format(*res)

def ttest(exp1,exp2,exp3):
    print "=== exp1 vs exp2" 
    ts, pvalue = stats.ttest_ind(exp1, exp2,equal_var=False)
    print "p value =", pvalue
    print "=== exp1 vs exp3" 
    ts, pvalue = stats.ttest_ind(exp1, exp3,equal_var=False)
    print "p value =", pvalue
    print "=== exp2 vs exp3" 
    ts, pvalue = stats.ttest_ind(exp2, exp3,equal_var=False)
    print "p value =", pvalue,



def scale2class(l):
    ll=[]
    for val in l:
        if val>=5:
            ll.append(1)
        else:
            ll.append(0)
    return ll

exp1={
    'q1':[1,1,1,1,1,3,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,3],
    'q2':[2,3,2,2,3,2,3,3,5,2,3,3,3,3,2,3,3,3,3,2,2,2,2],
    'q5_d':[0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,1,0,1,0,0,0,0],
    'q5_s':[1,1,3,4,4,0,1,1,0,0,0,1,2,1,2,2,2,0,0,1,2,1,1],
    'q7_agreable'   :[9,7,8,9 ,6 ,10,8 ,8,10,9,10,8,4 ,7,10,8 ,10,8,8 ,10,8,10,6],
    'q7_curious'    :[3,4,4,10,10,7 ,8 ,8,10,7,2 ,5,8 ,8,8 ,8 ,10,4,8 ,10,4,10,4],
    'q7_traquile'   :[9,2,6,6 ,8 ,3 ,8 ,6,8 ,9,4 ,3,2 ,5,8 ,4 ,8 ,6,4 ,4 ,6,10,6],
    'q7_extovertive':[0,9,8,8 ,8 ,5 ,10,6,10,7,10,1,6 ,6,8 ,10,10,6,4 ,10,6,8 ,4],
    'q7_reponsable' :[5,4,0,6 ,10,7 ,10,10,8,8 ,7,6 ,1,10,8,8 ,8 ,8 ,2,10,6 ,8,7 ,8]
}

exp2={
    'q1':[1,1,3,1,1,2,1,1,1,2,3,1,1,1,1,1,1,1,1,1,1,3,3],
    'q2':[4,3,3,2,2,2,3,  3,3,3,2,2,2,3,3,3,3,2,2,2,2,3],
    'q5_d':[0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1],
    'q5_s':[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1],
    'q7_agreable'   :[8,8,6,4,10,8 ,10,10,10,8 ,8 ,10,0 ,7,10,0 ,9,8,4,8, 4,2,9],
    'q7_curious'    :[4,8,8,5,4 ,2 ,6 , 4, 8,10,6 ,0 ,0 ,7,0 ,6 ,6,8,3,8, 8,0,9],
    'q7_traquile'   :[4,6,4,3,10,8 ,10,8 ,6 ,8, 6 ,10,0 ,9,8 ,10,5,4,4,10,2,6,7],
    'q7_extovertive':[4,4,6,3,6 ,5 ,6 ,6 ,6 ,6, 4 ,0 ,0 ,3,8 ,0, 7,8,4,6 ,4,2,8],
    'q7_reponsable' :[8,8,8,5,10,10,8 ,6 ,4 ,8, 10,0 ,0 ,9,0 ,6 ,8,6,4,8 ,2,0,6] 
}

exp3={
    'q1':[1,1,1,2,2,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    'q2':[2,2,2,3,4,4,3,2,1,3,3,3,3,3,3,2,2,3,4,3,3,3,2],
    'q5_d':[0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0],
    'q5_s':[0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,1,1,1,1,1],
    'q7_agreable'   :[6,4,8 ,8 ,2 ,10,9,6,1,6 ,10,7,8 ,10,9,5,0,10,10,10,10,7,8],
    'q7_curious'    :[8,8,4 ,6 ,8 ,10,0,4,2,10,8 ,9,10,8 ,8,7,0,10,10,10, 6,7,10],
    'q7_traquile'   :[8,4,10,10,3 ,10,0,6,1, 4,4 ,9,4 ,6 ,7,5,0,10, 6, 8,10,9,6],
    'q7_extovertive':[4,2,6 ,3 ,9 ,10,0,9,1, 2,8 ,0,8 ,4 ,7,7,8, 8, 8, 2,10,7,10],
    'q7_reponsable' :[6,0,10,6 ,10,10,0,4,9, 2,8 ,0,8 ,8 ,3,3,0, 8, 8, 8, 2,7,8] 
}

print "Summary experiment 1"
summary(exp1)

print "Summary experiment 2"
summary(exp2)

print "Summary experiment 3"
summary(exp3)

print "\n\nChi square Q1"
chi2(exp1["q1"],exp2['q1'],exp3['q1'],1,4)

print "\n\nChi square Q2"
chi2(exp1["q2"],exp2['q2'],exp3['q2'],1)

print "\n\nChi square Q5 D"
chi2(exp1["q5_d"],exp2['q5_d'],exp3['q5_d'],0,2)

print "\n\nChi square Q5 S"
chi2(exp1["q5_s"],exp2['q5_s'],exp3['q5_s'],0,4)

mix_q5(exp1)
mix_q5(exp2)
mix_q5(exp3)

print "\n\nChi square Q5 Both"
chi2(exp1["q5"],exp2['q5'],exp3['q5'],0,4)

print "\n\nChi square Q7 agreable"
ttest(exp1["q7_agreable"],
     exp2['q7_agreable'],
     exp3['q7_agreable'])

print "\n\nChi square Q7 curious"
ttest(exp1["q7_curious"],
     exp2['q7_curious'],
     exp3['q7_curious'])

print "\n\nChi square Q7 tranquile"
ttest(exp1["q7_traquile"],
     exp2['q7_traquile'],
     exp3['q7_traquile'])

print "\n\nChi square Q7 extrovertive"
ttest(exp1["q7_extovertive"],
     exp2['q7_extovertive'],
     exp3['q7_extovertive'])


print "\n\nChi square Q7 responsible"
ttest(exp1["q7_reponsable"],
     exp2['q7_reponsable'],
     exp3['q7_reponsable'])



