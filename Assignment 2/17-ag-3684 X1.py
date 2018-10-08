# MS(CS)  2017-AG-3684 
# ASSIGNMENT NO 2
#LIbraries needed
from scipy import stats
import numpy as np
from matplotlib import pyplot as plt
import statsmodels.api as sm
from mpl_toolkits.mplot3d import Axes3D
from statsmodels.formula.api import ols
import pandas as pd
#GET DATA FROM EXCEL FILE
fg=pd.read_csv("adt.csv")
fg.head()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X1 = np.array([ 0,0,10,10,20,20])
X2 = np.array([0,0,100,100,400,400])
Y=np.array([5,7,15,17,9,8])
Reg2 = ols(formula = "Y ~ X1 + X2", data = fg)
rt = Reg2.fit()
print(fg)
print(rt.params)
gt=np.array(rt.fittedvalues)
num_items = len(Y)
mean = sum(Y) / num_items
differences = [Y - mean for Y in Y]
sq_differences = [d ** 2 for d in differences]
ol = np.sum(sq_differences)
print('The  TOTAL sum of square(TSS) is =',ol)
d = np.array([gt - 10.16])
jk = np.array([d ** 2 for d in d])
ok = np.sum(jk)
print('The REGRESSION SUM OF SQUARE (RSS)is =',ok)
differences = [Y - gt]
sq_differences = [d ** 2 for d in differences]
ssd = np.sum(sq_differences)
print('The ERROR sum of square is(ESS) =.',ssd)
print("R SQUARE COEFFICIENT OF DETERMINATION")
print("R SQUARE VALUE IS=",ok/ol)
#Summary of Whole Data
print(rt.summary())
print ("ANOVA TABLE FOR GIVEN DATA")
mod = ols('Y ~ X1 + X2', data=fg).fit()
aov_table = sm.stats.anova_lm(mod, typ=2)
print(aov_table)
#ONe Sample T Test
print("ONE SAMPLE T TEST")
one=stats.ttest_1samp(X1, 0.0)
print(one)
one=stats.ttest_1samp(X2, 0.0)
print(one)
one=stats.ttest_1samp(Y, 0.0)
print(one)
#SCAtter PLOT
ax.scatter(X1,X2,Y,c='blue',marker='o')
ax.set_xlabel("X1")
ax.set_ylabel("X2")
ax.set_zlabel("Y")
plt.show()