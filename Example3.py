from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import math as math
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

Data_Transfer_Rate = np.array([500, 700, 150, 175, 980, 180])
Number_of_Signals = np.array([0, 70, 105, 100, 205, 200])
Number_of_Nodes = np.array([0, 0, 100, 100, 400, 400])

#Total Number of Observations
n = Data_Transfer_Rate.size
print("\nNumber of Observations : n = ",n)

#Finding mean
Data_Transfer_Rate_mean = sum(Data_Transfer_Rate)/Data_Transfer_Rate.size
Number_of_Signals_mean = sum(Number_of_Signals)/Number_of_Signals.size
Number_of_Nodes_mean = sum(Number_of_Nodes)/Number_of_Nodes.size

print("\nMean for Data transfer rate = ",Data_Transfer_Rate_mean)
print("Mean for number of signals = ",Number_of_Signals_mean)
print("Mean for number of nodes = ",Number_of_Nodes_mean)

#Calculating x1, x2, y
x1 = Number_of_Signals - Number_of_Signals_mean
x2 = Number_of_Nodes - Number_of_Nodes_mean
y = Data_Transfer_Rate - Data_Transfer_Rate_mean

print("\nx1 =",x1)
print("x2 =",x2)
print("Y =",y)

#Calculating Sum
Σx1 = np.sum(x1)
Σx2 = np.sum(x2)
Σy = np.sum(y)

#Calculating Squares
x1_sq = np.sum((x1)**2)
x2_sq = np.sum((x2)**2)
y_sq = np.sum((y)**2)

Σx1y = np.sum((x1*y))
Σx1_sq = np.sum((x1)**2)
Σx2_sq = np.sum((x2)**2)
Σx2y = np.sum((x2*y))
Σx1x2 = np.sum((x1*x2))

Σx1y_Σx2_sq = Σx1y*Σx2_sq
Σx2y_Σx1x2 = Σx2y*Σx1x2
Σx1_sq_Σx2_sq = Σx1_sq*Σx2_sq
Σx1x2_sq = (Σx1x2)**2

#Calculating the value of beta1
B1 = (Σx1y_Σx2_sq - Σx2y_Σx1x2) / (Σx1_sq_Σx2_sq - Σx1x2_sq)
print("\nBeta1 = ",B1)

#Calculating the value of beta2
B2 = ( (Σx2y*Σx1_sq) - (Σx1y*Σx1x2) ) / (Σx1_sq_Σx2_sq - Σx1x2_sq)
print("Beta2 = ",B2)

#Calculating the value of beta0
B0 = Data_Transfer_Rate_mean - (B1*Number_of_Signals_mean) - (B2*Number_of_Nodes_mean)
print("Beta0 = ",B0)

#Total parameters
k = 3
print("\nNumber of Parameters B0, B1, B2 : k = ",k)

#Calculated Y
Y_hat = B0 + B1*Number_of_Signals + B2*Number_of_Nodes


print("\nY_hat = {} + {}X1 + {}X2".format(B0,B1,B2))

#Calculating coefficient of determination
TSS = np.sum((Data_Transfer_Rate - Data_Transfer_Rate_mean)**2)
MSS = np.sum((Y_hat - Data_Transfer_Rate_mean)**2)
RSS = np.sum((Data_Transfer_Rate - Y_hat)**2)

print("\nTotal Sum of Squares : TSS = ",TSS)
print("Model Sum of Squares : MSS = ",MSS)
print("Residual Sum of Squares : RSS = ",RSS)

R_sq = MSS/TSS
print("\nR_square = ",R_sq)

#Calculating mean square error
MSE = RSS/(n-k)
print("\nMeans Square Error : MSE = ",MSE)

#Calculating Variances
V_B1 = MSE *( (Σx2_sq) / (Σx1_sq_Σx2_sq - Σx1x2_sq) )
SE_B1 = math.sqrt(V_B1)
print("\nVariance of Beta1 = ",V_B1)
print("Standard Error of Beta1 : SE(B1) = ",SE_B1)

V_B2 = MSE *( (Σx1_sq) / (Σx1_sq_Σx2_sq - Σx1x2_sq) )
SE_B2 = math.sqrt(V_B2)
print("\nVariance of Beta2 = ",V_B2)
print("Standard Error of Beta2 : SE(B2) = ",SE_B2)

Number_of_Signals_mean_sq = Number_of_Signals_mean**2
Number_of_Nodes_mean_sq = Number_of_Nodes_mean**2
Number_of_Signals_mean_Number_of_Nodes_mean = Number_of_Signals_mean*Number_of_Nodes_mean

V_B0 = MSE * ((1/n) + ((Number_of_Signals_mean_sq*Σx2_sq + Number_of_Nodes_mean_sq*Σx1_sq - 2*Number_of_Signals_mean_Number_of_Nodes_mean*(Σx1x2))/(Σx1_sq_Σx2_sq - Σx1x2_sq)))
SE_B0 = math.sqrt(V_B0)
print("\nVariance of Beta0 = ",V_B0)
print("Standard Error of Beta0 : SE(B0) = ",SE_B0)

#Plotting graph and ANOVA table
data_frame = pd.DataFrame(
    {
        "Y": Data_Transfer_Rate
        , "X1": Number_of_Signals
        , "X2": Number_of_Nodes
    }
)

Reg = ols(formula="Data_Transfer_Rate ~ Number_of_Signals + Number_of_Nodes", data=data_frame)
Fit2 = Reg.fit()
print("\n", Fit2.summary())
print("\n", anova_lm(Fit2))




fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter(
    data_frame["X1"]
    , data_frame["X2"]
    , data_frame["Y"]
    , color="green"
    , marker="o"
    , alpha=1
)
ax.set_xlabel("X1")
ax.set_ylabel("X2")
ax.set_zlabel("Y")

plt.show()




