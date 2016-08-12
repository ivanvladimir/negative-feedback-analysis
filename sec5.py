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
    h_1=np.bincount(q_1,None,6)[min:max]
    h_2=np.bincount(q_2,None,6)[min:max]
    h_3=np.bincount(q_3,None,6)[min:max]
    print "Data"
    r_c_table=np.array([h_1,h_2,h_3])
    print r_c_table
    res= stats.chi2_contingency(r_c_table)
    print """
Test statistic     : {0}
P-value            : {1}
Degrees of freedom : {2}
Expected           : {3} """.format(*res)

exp1={
    'q1':[1,1,1,1,1,3,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,3],
    'q2':[2,3,2,2,3,2,3,3,5,2,3,3,3,3,2,3,3,3,3,2,2,2,2],
    'q5_d':[0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,1,0,1,0,0,0,0],
    'q5_s':[1,1,3,4,4,0,1,1,0,0,0,1,2,1,2,2,2,0,0,1,2,1,1]
}

exp2={
    'q1':[1,1,3,1,1,2,1,1,1,2,3,1,1,1,1,1,1,1,1,1,1,3,3],
    'q2':[4,3,3,2,2,2,3,  3,3,3,2,2,2,3,3,3,3,2,2,2,2,3],
    'q5_d':[0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1],
    'q5_s':[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1]
}

exp3={
    'q1':[1,1,1,2,2,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    'q2':[2,2,2,3,4,4,3,2,1,3,3,3,3,3,3,2,2,3,4,3,3,3,2],
    'q5_d':[0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0],
    'q5_s':[0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,1,1,1,1,1]
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


