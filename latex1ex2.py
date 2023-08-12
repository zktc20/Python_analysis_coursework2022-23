#stats and latex
#part 2 analysis but with 2nd fresh data set

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

first_df=(pd.read_csv('C:/Users/ztcpo/Desktop/LABORATORY/LATEXCOMP/latex2raw.csv'))

df=first_df.iloc[range(0,40)]


#linear least fit square
xval=df['Data Set 2: x/ m']*10**6
yval=df['Data Set 2: F / N']*10**9
ystd=df['Data Set 2: Std F / N']*10**9

xsquared=xval**2
xy=xval*yval

sumx=np.sum(df['Data Set 2: x/ m'])*10**6
sumy=np.sum(df['Data Set 2: F / N'])*10**9
sum_xsquared=np.sum(xsquared)
sum_xy=np.sum(xy)
N=40

slope_m= ((N*sum_xy)-(sumx*sumy))/((N*sum_xsquared)-((sumx)**2))

intercept=(sumy-(slope_m*sumx))/N

print('This is the SPRING CONSTANT:',slope_m)
print("Intercept:",intercept)

linearregress=(slope_m*xval) + intercept

fig = plt.figure(figsize=(12,10))                          
ax = fig.add_subplot(1,1,1)


ax.set_ylabel('Force / nN',fontsize=30)
ax.set_xlabel('Distance / $\mu$m',fontsize=30)
ax.xaxis.set_ticks(np.arange(0,250,50))
ax.errorbar(xval,yval,yerr=ystd,color='k',marker='o',markersize=10,linestyle='none',capsize=3)
ax.plot(xval,linearregress,color='black')
ax.tick_params(axis='both', labelsize=25)
ax.set_xlim(left=0,right=200)



ax.legend(fontsize=25)
ax.plot()

plt.savefig('fig2ztc')
