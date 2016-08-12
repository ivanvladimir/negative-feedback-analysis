# Codification

import numpy as np
import scipy.stats as stats
import scipy.special as special

codes = {
    "change object/discard" : 0,
    "Change position" : 1,
    "Put one object more" : 2,
    "null" : 3
}

neutral =np.array([0,1,2,1,2,1,3,2,3,1,2,1,1,1,3])
sad=np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,0])
angry=np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,0])


print "=================================== Analysing table V (Pos effect)"
print
print "Total interventions (neutral feedback) :", neutral.shape[0]
print "Total interventions (sad feedback):", sad.shape[0]
print
print "=== Calculating Fisher exact table" 
neutral_pos=len(neutral[neutral < 2])
neutral_neg=len(neutral[neutral > 1])
sad_pos=len(sad[sad < 2])
sad_neg=len(sad[sad > 1])
angry_pos=len(angry[angry < 2])
angry_neg=len(angry[angry > 1])
print "                   POS     NEG"
print "neutral  feedback    {0}     {1}".format(neutral_pos, neutral_neg)
print "sad feedback         {0}     {1}".format(sad_pos, sad_neg)
print "angry feedback       {0}     {1}".format(angry_pos, angry_neg)
print
print "=== Calculating independence (Fisher exact test)" 
oddsradio,pvalue=stats.fisher_exact([[neutral_pos,neutral_neg],[sad_pos,sad_neg]])
print "p value (neutral v sad  )=", pvalue,
if pvalue < 0.01:
    print "(independent)"
else:
    print "(not independent)"
oddsradio,pvalue=stats.fisher_exact([[neutral_pos,neutral_neg],[angry_pos,angry_neg]])
print "p value (neutral v angry)=", pvalue,
if pvalue < 0.01:
    print "(independent)"
else:
    print "(not independent)"
oddsradio,pvalue=stats.fisher_exact([[sad_pos,sad_neg],[angry_pos,angry_neg]])
print "p value (sad v angry)=", pvalue,
if pvalue < 0.01:
    print "(independent)"
else:
    print "(not independent)"


print "=== Calcularing probability (assuming Hypergeometric distribution)"
K=len(neutral)
N=len(neutral)+len(sad)
k=neutral_pos
N_k=len(sad)
N=len(neutral)+len(sad)
n_k=sad_pos
n=neutral_pos+sad_pos
prob =  special.binom(K,k)*special.binom(N_k,n-k)*1.0/special.binom(N,n)
print "Probability (sad vs neutral):", prob
print 
K=len(neutral)
N=len(neutral)+len(angry)
k=neutral_pos
N_k=len(angry)
N=len(neutral)+len(angry)
n_k=angry_pos
n=neutral_pos+angry_pos
prob =  special.binom(K,k)*special.binom(N_k,n-k)*1.0/special.binom(N,n)
print "Probability (angry vs neutral):", prob
print 
print "=== Calculating power"
print "library(statmod)"
print "power.fisher.test({0},{1},{2},{3},alpha=0.01)".format(neutral_pos*1.0/len(neutral),sad_pos*1.0/len(sad),len(neutral),len(sad))

print "Defaults (0.01) = 0.6"
print "Defaults (0.05) = 0.9"

neutral_times =np.array([14,20,2,13,3,7,23,3,23,7,6,4,5,11,23])
sad_times=np.array([4,4,2,12,22,9,6,12,1,3,14,2,4,2,1])
angry_times=np.array([3,6,5,4,6,6,13,3,3,6,1,8,5,8,5])

print "=================================== Analysing time (Pos effect)"
print
print "Total times (neutral feedback) :", neutral_times.shape[0]
print "Total times(sad feedback)      :", sad_times.shape[0]
print "Total times(angry feedback)    :", angry_times.shape[0]
print
print "=== Calculating independence (Unpaired t-test)" 
pvalue,ts = stats.ttest_ind(neutral_times, sad_times)
print "Neutral vs sad"
print "p value =", pvalue,
if pvalue < 0.01:
    print "(independent)"
else:
    print "(not independent)"



print "=== Calculating independence (Unpaired t-test)" 
pvalue,ts = stats.ttest_ind(neutral_times, sad_times)
print "Neutral vs sad"
print "p value =", pvalue,
if pvalue < 0.01:
    print "(independent)"
else:
    print "(not independent)"

print "If we assume unequal variances than the t-statistic is {1} and the p-value is {0}.".format(pvalue,ts),
if pvalue < 0.01:
    print "(independent)"
else:
    print "(not independent)"

print "Neutral vs angry"
pvalue,ts = stats.ttest_ind(neutral_times, angry_times)
print "p value =", pvalue,
if pvalue < 0.01:
    print "(independent)"
else:
    print "(not independent)"

print "If we assume unequal variances than the t-statistic is {1} and the p-value is {0}.".format(pvalue,ts),
if pvalue < 0.01:
    print "(independent)"
else:
    print "(not independent)"

print "sad vs angry"
pvalue,ts = stats.ttest_ind(sad_times, angry_times)
print "p value =", pvalue,
if pvalue < 0.01:
    print "(independent)"
else:
    print "(not independent)"

print "If we assume unequal variances than the t-statistic is {1} and the p-value is {0}.".format(pvalue,ts),
if pvalue < 0.01:
    print "(independent)"
else:
    print "(not independent)"


