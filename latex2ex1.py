import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

first_df=(pd.read_csv('C:/Users/ztcpo/Desktop/LABORATORY/LATEXCOMP/latex2raw.csv'))

df_3=((first_df.iloc[range(0,3)]))
df_5=((first_df.iloc[range(0,5)]))
df_10=((first_df.iloc[range(0,10)]))
df_50=((first_df.iloc[range(0,50)]))
df_100=((first_df.iloc[range(0,100)]))

weight3=1/((df_3['Data Set 1: Uncertainty / A'])**2)
weight5=1/((df_5['Data Set 1: Uncertainty / A'])**2)
weight10=1/((df_10['Data Set 1: Uncertainty / A'])**2)
weight50=1/((df_50['Data Set 1: Uncertainty / A'])**2)
weight100=1/((df_100['Data Set 1: Uncertainty / A'])**2)
weightall=1/((first_df['Data Set 1: Uncertainty / A'])**2)

#weight x number summed up
sum3=sum(weight3*df_3['Data Set 1: Current / A'])
sum5=sum(weight5*df_5['Data Set 1: Current / A'])
sum10=sum(weight10*df_10['Data Set 1: Current / A'])
sum50=sum(weight50*df_50['Data Set 1: Current / A'])
sum100=sum(weight100*df_100['Data Set 1: Current / A'])
sum_all=sum(weightall*first_df['Data Set 1: Current / A'])

#weighted means
wmean3=sum3/sum(weight3)
wmean5=sum5/sum(weight5)
wmean10=sum10/sum(weight10)
wmean50=sum50/sum(weight50)
wmean100=sum100/sum(weight100)
wmean_all=sum_all/sum(weightall)


#weighted standard error of da mean
std3=1/(np.sqrt(sum(weight3)))
std5=1/(np.sqrt(sum(weight5)))
std10=1/(np.sqrt(sum(weight10)))
std50=1/(np.sqrt(sum(weight50)))
std100=1/(np.sqrt(sum(weight100)))
stdall=1/(np.sqrt(sum(weightall)))

#end of result

print("These are the Weighted Mean plus weighted standard error of the mean:")
print("3:",wmean3*10**3,"+-",std3*10**3,"mA")
print("5:",wmean5*10**3,"+-",std5*10**3,"mA")
print("10:",wmean10*10**3,"+-",std10*10**3,"mA")
print("50:",wmean50*10**3,"+-",std50*10**3,"mA")
print("100:",wmean100*10**3,"+-",std100*10**3,"mA")
print("ALL:",wmean_all*10**3,"+-",stdall*10**3,"mA")