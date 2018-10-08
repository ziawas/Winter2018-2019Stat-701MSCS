# MS(CS)  2017-AG-3684 
# ASSIGNMENT NO 2
#LIBRARIES DETAIL
from scipy import stats
import numpy as np
from matplotlib import pyplot as plt
import statsmodels.api as sm
from mpl_toolkits.mplot3d import Axes3D
from statsmodels.formula.api import ols
import pandas as pd

#1 way to combine data
#Upload excel file
#fg=pd.read_csv("add.csv")
#fg.head()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
CPU = np.array([ 28, 27, 33, 44, 50, 60, 65])
RAMS = np.array([5,5,7,8,4,2,7,])
REG=np.array([40,50,50,70,65,65,80])
#Second Way to Combine data
fg = pd.DataFrame({
        "CPU": CPU
        , "RAM SIZE": RAMS
        , "REGISTER SIZE": REG }
)
print("Data for Multiple Linear Regression")
print(fg)
Reg2 = ols(formula = "CPU ~ RAMS + REG", data = fg)
rt = Reg2.fit()
print("Values of regression coefficients and intercept")
print(rt.params)
gt=np.array(rt.fittedvalues)

#MEAN VALUE OF CPU
num_items = len(CPU)
mean = sum(CPU) / num_items
print("Y bar VAlue is=",mean)

#TOTAL SUM OF SQUARE
differences = [CPU - mean for CPU in CPU]
sq_differences = [d ** 2 for d in differences]
ghj = np.sum(sq_differences)
print('The  TOTAL sum of square(TSS) is =',ghj)

#REGRESSION SUM OF SQUARE
d = np.array([gt - 43.85])
jk = np.array([d ** 2 for d in d])
hjk = np.sum(jk)
print('The REGRESSION SUM OF SQUARE (RSS)is =',hjk)

#ERROR SUM OF SQUARE
differences = [CPU - gt]
sq_differences = [d ** 2 for d in differences]
ssd = np.sum(sq_differences)
print('The ERROR sum of square is(ESS) =.',ssd)

#R SQUARE COEFFICIENT OF DETERMINATION
print("R Square Value")
ik=hjk/ghj
print("R Square is=",ik)

#Summary of Whole Data
print(rt.summary())

print ("ANOVA TABLE FOR GIVEN DATA")
mod = ols('CPU ~ RAMS + REG', data=fg).fit()
aov_table = sm.stats.anova_lm(mod, typ=2)
print(aov_table)

#ONe Sample T Test
print("One Sample T Test ")
one=stats.ttest_1samp(RAMS, 0.0)
print(one)
one=stats.ttest_1samp(REG, 0.0)
print(one)
one=stats.ttest_1samp(CPU, 0.0)
print(one)

#Scatter Plot
ax.scatter(RAMS,REG,CPU,c='blue',marker='o')
ax.set_xlabel("RAM SIZE")
ax.set_ylabel("REGISTER SIZE")
ax.set_zlabel("CPU")
plt.show()
#PLOT Histogram
fg.hist(bins=50, figsize=(20,15))
plt.savefig("attribute_histogram_plots")
plt.show()

