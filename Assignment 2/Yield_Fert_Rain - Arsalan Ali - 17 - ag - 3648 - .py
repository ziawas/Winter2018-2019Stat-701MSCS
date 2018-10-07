"""  Assignment 2 : MS(CS) - Stats 701 : Yield | Fertilizer | Rainfall
Student name: Arsalan Ali , Registration no. 2017-ag-3648 , Degree and Session : MS(CS) 2017-2019 """

# Note: I have written this entire code myself except the graph plotting
# The graphs i included were taken from your (Sir's) work
# and i checked a tutorial too to understand how they work and modified as needed.


# mpl_toolkits is for the actual 3D-plotting of our data-set , it's so cool,  it looks gray but it works
from mpl_toolkits.mplot3d import Axes3D

# It's for the normal graph plotting we do , nothi'n too special
from matplotlib import pyplot as plt

# My man numpy sure does all the stats
import numpy as np

# Panda's basically.....an animal, we use it to view data in a neat manner
import pandas as pd

# You can't have Science without Maths right? Just added it since i had to use Positive-Square Root for SE
import math as math

# Consider it a shortcut for Stats ( Pre-defined methods ), which i only applied in the end for the 3D graph
from statsmodels.formula.api import ols

# Anova Vanova, what would be the world without ya?
from statsmodels.stats.anova import anova_lm

from scipy import stats

# Original Data without any Conversion of Scales
'''Yield = np.array([40, 50, 50, 70, 65, 65, 80])  # It's in Bushel scale
Fertilizer = np.array([100, 200, 300, 400, 500, 600, 700])   # It's in Pound scale
Rainfall = np.array([10, 20, 10, 30, 20, 20, 30])  # It's in Inches scale'''


# Data in Converted form. Assuming the Crop we are working on is Wheat

# Converted from Bushel to KG
Yield = np.array([40*27.2155 , 50*27.2155 , 50*27.2155 , 70*27.2155 , 65*27.2155 , 65*27.2155 , 80*27.2155 ])

# Converted from Pounds to KG
Fertilizer = np.array([45.3592, 90.7185, 136.078, 181.437, 226.796, 272.155, 317.515])

# Converted from Inches to Millimeters
Rainfall = np.array([254, 508, 254, 762, 508, 508, 762])

# Number of Observations
n = Yield.size
print("\nNumber of Observations : n = ", n)

# Man , why are you so mean?
Y_bar = sum(Yield) / Yield.size
F_bar = sum(Fertilizer) / Fertilizer.size
R_bar = sum(Rainfall) / Rainfall.size

print("\nYield Mean : Y = ", Y_bar)
print("Fertilizer Mean : X1 = ", F_bar)
print("Rainfall Mean : X2 = ", R_bar)

# Let's deviate from the mean mood please
x1 = Fertilizer - F_bar
x2 = Rainfall - R_bar
y = Yield - Y_bar

print("\nx1 =", x1)
print("x2 =", x2)
print("Y =", y)

# Summing up our deviations gets us nowhere, you know that right?
Σx1 = np.sum(x1)
Σx2 = np.sum(x2)
Σy = np.sum(y)

# Doubling and them summing up the deviations , now we're talking
x1_square = np.sum((x1) ** 2)
x2_square = np.sum((x2) ** 2)
y_square = np.sum((y) ** 2)

# Just some formulas in order to get all the Betas
Σx1y = np.sum((x1 * y))
Σx1_square = np.sum((x1) ** 2)
Σx2_square = np.sum((x2) ** 2)
Σx2y = np.sum((x2 * y))
Σx1x2 = np.sum((x1 * x2))

Σx1y_Σx2_square = Σx1y * Σx2_square
Σx2y_Σx1x2 = Σx2y * Σx1x2
Σx1_square_Σx2_square = Σx1_square * Σx2_square
Σx1x2_square = (Σx1x2) ** 2

Beta1 = (Σx1y_Σx2_square - Σx2y_Σx1x2) / (Σx1_square_Σx2_square - Σx1x2_square)
print("\nBeta1 = ", Beta1)

Beta2 = ((Σx2y * Σx1_square) - (Σx1y * Σx1x2)) / (Σx1_square_Σx2_square - Σx1x2_square)
print("Beta2 = ", Beta2)

Beta0 = Y_bar - (Beta1 * F_bar) - (Beta2 * R_bar)
print("Beta0 = ", Beta0)

# Number of parameters e.g, All the Betas
k = 3
print("\nNumber of Parameters B0, B1, B2 : k = ", k)

# Our dearly Y wearing a Hat. The Y-predicted
Y_hat = Beta0 + Beta1 * Fertilizer + Beta2 * Rainfall
ΣY_hat = np.sum(Beta0 + Beta1 * Fertilizer + Beta2 * Rainfall)
print("\nSum of All Y-hat values = ", ΣY_hat)

print("\nY = {} + {}X1 + {}X2".format(Beta0, Beta1, Beta2))

# Here comes the big league
TSS = np.sum((Yield - Y_bar) ** 2)
MSS = np.sum((Y_hat - Y_bar) ** 2)
RSS = np.sum((Yield - Y_hat) ** 2)

print("\nTotal Sum of Squares : TSS = ", TSS)
print("Model Sum of Squares : MSS = ", MSS)
print("Residual Sum of Squares : RSS = ", RSS)

# The one and only Regression Co-efficient
R_square = MSS / TSS
print("\nR_square = ", R_square)

# Mean Square Error coming through.....clear the wayyyyy
MSE = RSS / (n - k)
print("\nMeans Square Error : MSE = ", MSE)

# Beta1's secret
V_Beta1 = MSE * ((Σx2_square) / (Σx1_square_Σx2_square - Σx1x2_square))
SE_Beta1 = math.sqrt(V_Beta1)
print("\nVariance of Beta1 = ", V_Beta1)
print("Standard Error of Beta1 : SE(B1) = ", SE_Beta1)

# Beta2's secret
V_Beta2 = MSE * ((Σx1_square) / (Σx1_square_Σx2_square - Σx1x2_square))
SE_Beta2 = math.sqrt(V_Beta2)
print("\nVariance of Beta2 = ", V_Beta2)
print("Standard Error of Beta2 : SE(B2) = ", SE_Beta2)

# Just some dudes needed for Beta0's top top secret...Ooooooo
F_bar_square = F_bar ** 2
R_bar_square = R_bar ** 2
F_bar_R_bar = F_bar * R_bar

# Biggest secret of all from Beta0's side
V_Beta0 = MSE * ((1 / n) + ((F_bar_square * Σx2_square + R_bar_square * Σx1_square - 2 * F_bar_R_bar * (Σx1x2)) / (
        Σx1_square_Σx2_square - Σx1x2_square)))
SE_Beta0 = math.sqrt(V_Beta0)
print("\nVariance of Beta0 = ", V_Beta0)
print("Standard Error of Beta0 : SE(B0) = ", SE_Beta0)

# Gonna catch em all , come here you all datassss
data_frame = pd.DataFrame(
    {
        "Yield": Yield
        , "Fertilizer": Fertilizer
        , "Rainfall": Rainfall

    }
)

# It will turn it into a 3D Graph
ax = plt.figure().gca(projection='3d')

# It will take the values of Y,X1,X2 and turn them into X,Y,Z Axis
ax.scatter(
    data_frame["Fertilizer"]
    , data_frame["Rainfall"]
    , data_frame["Yield"]
    , color="blue"
    , marker="o"
    , alpha=1
)

# Title of the graph
ax.set_title(
    "Relation of Wheat Yield with Fertilizer and Rainfall\n \n (Pounds/Bushel Converted into KG and Inches into mm) \n("
    "Arsalan Ali 2017-ag-3648)")

# This code will simply label the 3 Axis we just created
ax.set_xlabel("Fertilizer ( Kilogram )", color="red")
ax.set_ylabel("Rainfall ( Millimeter )", color="purple")
ax.set_zlabel("Yield ( Kilogram )", color="blue")

# We all know what this does , right? So skip it
plt.show()

# Now here's the part where our imported statsmodels comes in play
Reg = ols(formula="Yield ~ Fertilizer + Rainfall", data=data_frame)

Fit2 = Reg.fit()
print("\n", Fit2.summary())
print("\n", anova_lm(Fit2))

# Again plotting our Dear 3D-Graph
ax = plt.figure().gca(projection='3d')

# Creating Axis X,Y,Z out of our Data Y,X1,X2
ax.scatter(
    data_frame["Fertilizer"]
    , data_frame["Rainfall"]
    , data_frame["Yield"]
    , color="blue"
    , marker="o"
    , alpha=1
)

# Title of the graph
ax.set_title('Regression Line/Shape in 3D \n (Pounds/Bushel Converted into KG and Inches into mm)')

# Again labelling the Axis we just created , writing duplicate code is a/an headache
ax.set_xlabel("Fertilizer ( Kilogram )", color="red")
ax.set_ylabel("Rainfall ( Millimeter )", color="purple")
ax.set_zlabel("Yield ( Kilogram )", color="blue")


# Parameters to create Shape/Grid using Fertilizer and Rainfall Data
x_surf = Fertilizer
y_surf = Rainfall

# The purpose of meshgrid is to create a rectangular grid out of an array of x and y values
x_surf, y_surf = np.meshgrid(x_surf, y_surf)

# To combine X and Y in order to generate Z for the surface
exog = pd.core.frame.DataFrame({
    "Fertilizer": x_surf.ravel()
    , "Rainfall": y_surf.ravel()
})

# Generating Predicted values for the shape
out = Fit2.predict(exog=exog)

# Generating the actual Shape now on Graph
ax.plot_surface(
    x_surf
    , y_surf
    , out.values.reshape(x_surf.shape)
    , rstride=1
    , cstride=1
    , color="None"
    , alpha=0.4
)
# We all know what this does , right? The End of our Assignment comes here.
plt.show()
