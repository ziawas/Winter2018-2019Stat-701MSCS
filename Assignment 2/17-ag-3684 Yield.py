# MS(CS)  2017-AG-3684 
# ASSIGNMENT NO 2
#liBRARIES IMPORT FOR WORKING
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
Fert = np.array([ 100, 200, 300, 400, 500, 600, 700])
Rainfall = np.array([10,20,10,30,20,20,30])
Yield=np.array([40,50,50,70,65,65,80])
#Second Way to Combine data
fg = pd.DataFrame({
        "Yield": Yield
        , "Fertilizer": Fert
        , "Rainfall": Rainfall }
)
print("Data for Multiple Linear Regression")
print(fg)
Reg2 = ols(formula = "Yield ~ Fert + Rainfall", data = fg)
rt = Reg2.fit()
print("Values of regression coefficients and intercept")
print(rt.params)
gt=np.array(rt.fittedvalues)

#MEAN VALUE OF YIELD
num_items = len(Yield)
mean = sum(Yield) / num_items

#TOTAL SS
differences = [Yield - mean for Yield in Yield]
sq_differences = [d ** 2 for d in differences]
op = np.sum(sq_differences)
print('The  TOTAL sum of square(TSS) is =',op)
#REGRESSION SS
d = np.array([gt - 60])
jk = np.array([d ** 2 for d in d])
ikl = np.sum(jk)
print('The REGRESSION SUM OF SQUARE (RSS)is =',ikl)

#ERROR SS
differences = [Yield - gt]
sq_differences = [d ** 2 for d in differences]
ssd = np.sum(sq_differences)
print('The ERROR sum of square is(ESS) =.',ssd)

#COEFFICIENT OF DETERMINATION
print("R SQUARE COEFFICIENT OF DETERMINATION")
print(ikl/op)

#Summary of Whole Data
print(rt.summary())

print ("ANOVA TABLE FOR GIVEN DATA")
mod = ols('Yield ~ Fert + Rainfall', data=fg).fit()
aov_table = sm.stats.anova_lm(mod, typ=2)
print(aov_table)

#ONe Sample T Test
print("One Sample T Test ")
one=stats.ttest_1samp(Fert, 0.0)
print(one)
one=stats.ttest_1samp(Rainfall, 0.0)
print(one)
one=stats.ttest_1samp(Yield, 0.0)
print(one)

#Scatter Plot
ax.scatter(Fert,Rainfall,Yield,c='blue',marker='o')
ax.set_xlabel("Fertilizer")
ax.set_ylabel("Rainfall")
ax.set_zlabel("Yield")
plt.show()

#PLOT Histogram
fg.hist(bins=50, figsize=(20,15))
plt.savefig("attribute_histogram_plots")
plt.show()


