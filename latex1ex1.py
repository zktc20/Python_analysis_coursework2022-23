import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

first_df=(pd.read_csv('C:/Users/ztcpo/Desktop/LABORATORY/LATEXCOMP/latex3raw.csv'))

df_3=((first_df.iloc[range(0,3)])*10**3)
df_5=((first_df.iloc[range(0,5)])*10**3)
df_10=((first_df.iloc[range(0,10)])*10**3)
df_50=((first_df.iloc[range(0,50)])*10**3)
df_100=((first_df.iloc[range(0,100)])*10**3)

mean_3=(df_3['Data Set 1: Current / A']).mean()
mean_5=(df_5['Data Set 1: Current / A']).mean()
mean_10=(df_10['Data Set 1: Current / A']).mean()
mean_50=(df_50['Data Set 1: Current / A']).mean()
mean_100=(df_100['Data Set 1: Current / A']).mean()
wholemean=(first_df['Data Set 1: Current / A']*10**3).mean()

meanerr=(first_df['Data Set 1: Uncertainty / A']).mean()

print("These are the Mean Values mA")
print(mean_3)
print(mean_5)
print(mean_10)
print(mean_50)
print(mean_100)
print(wholemean)

std_3=df_3['Data Set 1: Current / A'].std()
std_5=df_5['Data Set 1: Current / A'].std()
std_10=df_10['Data Set 1: Current / A'].std()
std_50=df_50['Data Set 1: Current / A'].std()
std_100=df_100['Data Set 1: Current / A'].std()
stdwhole=(first_df['Data Set 1: Current / A']*10**3).std()

print("These are the Standard Deviations mA")
print(std_3)
print(std_5)
print(std_10)
print(std_50)
print(std_100)
print(stdwhole)

print("These are the Standard Errors of Means mA")
print(std_3/(np.sqrt(3)))
print(std_5/(np.sqrt(5)))
print(std_10/(np.sqrt(10)))
print(std_50/(np.sqrt(50)))
print(std_100/(np.sqrt(100)))
print(stdwhole/(np.sqrt(10000)))

measurement_number=np.arange(0,50,1)
fig = plt.figure(figsize=(16,11
                          ))
ax = fig.add_subplot(1,1,1)



ax.set_ylabel('Current /mA',fontsize=40)
ax.set_xlabel('Measurement Number',fontsize=40)
ax.xaxis.set_ticks(np.arange(0,60,10))
ax.yaxis.set_ticks(np.arange(60, 90, 2))
ax.errorbar(measurement_number,df_50['Data Set 1: Current / A'],yerr=df_50['Data Set 1: Uncertainty / A'],color='k',marker='o',markersize=12,linestyle='none',capsize=10)
ax.tick_params(axis='both', labelsize=35)

ax.legend()
ax.plot()

plt.savefig('fig1ztc_latex3')

power=(((wholemean*10**-3)**2)*100)
error = np.sqrt(2*((100*((stdwhole*10**-3)/(np.sqrt(10000))))**2))

print("Power and Associated Error kW")
print(power*10**3)
print(error*10**3)