#using data set 2 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

first_df=(pd.read_csv('C:/Users/ztcpo/Desktop/LABORATORY/LATEXCOMP/latex2raw.csv'))

df=first_df.iloc[range(0,40)]
#finding the spring constant of a spring from experimental data with associated error.

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

#finding the equilibrium position of the spring, or the spring position when the force on it is zero.
#Now need to figure out x at F=0
#-c=kx
x_0=intercept/(slope_m*-1)


def line(x, slope_m, intercept):          # Set up the linear fitting - don't ammend
    return slope_m*x + intercept       

popt, pcov = curve_fit(line,xval,yval)
slope = popt[0]
intercept = popt[1]
err_slope = np.sqrt(float(pcov[0][0]))
err_intercept = np.sqrt(float(pcov[1][1]))

print('Slope: {0:.10f} +- {1:.10f}'.format(slope, err_slope))
print('Intercept: {0:.10f} +- {1:.10f}'.format(intercept, err_intercept))

#Uncertainty in x_0
unc1=((err_intercept)/slope_m)**2
unc2=((intercept/(slope_m**2))*(err_slope))**2
unc_x_0=np.sqrt(unc1+unc2)

print("Equilibrium spring position:",x_0,"+-",unc_x_0)
