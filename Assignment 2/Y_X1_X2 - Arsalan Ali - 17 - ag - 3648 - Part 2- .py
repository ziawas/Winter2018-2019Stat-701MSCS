"""  Assignment 2 : MS(CS) - Stats 701 : Y | X1 | X2 - Part 2
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

# Importing to take square root of negative/complex numbers
import cmath


# Our Data
My_Y = np.array([5, 7, 15, 17, 9, 11])
My_X1 = np.array([0, 0, 10, 10, 20, 20])
My_X2 = np.array([0, 0, 100, 100, 400, 400])


# Number of Observations
n = len(My_Y)
print("\nNumber of Observations : n = ", n)

# Man , why are you so mean?
Y_bar = sum(My_Y) / n
X1_bar = sum(My_X1) / n
X2_bar = sum(My_X2) / n

print("\nY Mean : Y = ", Y_bar)
print("X1 Mean : X1 = ", X1_bar)
print("X2 Mean : X2 = ", X2_bar)

# Let's deviate from the mean mood please
x1 = My_X1 - X1_bar
x2 = My_X2 - X2_bar
y = My_Y - Y_bar

print("\nX1 =", x1)
print("X2 =", x2)
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

Beta0 = Y_bar - (Beta1 * X1_bar) - (Beta2 * X2_bar)
print("Beta0 = ", Beta0)

# Number of parameters e.g, All the Betas
k = 3
print("\nNumber of Parameters B0, B1, B2 : k = ", k)

# Our dearly Y wearing a Hat. The Y-predicted
Y_hat = Beta0 + Beta1 * My_X1 + Beta2 * My_X2
ΣY_hat = np.sum(Beta0 + Beta1 * My_X1 + Beta2 * My_X2)
print("\nSum of All Y-hat values = ", ΣY_hat)

print("\nY = {} + {}X1 + {}X2".format(Beta0, Beta1, Beta2))

# Here comes the big league
TSS = np.sum((My_Y - Y_bar) ** 2)
MSS = np.sum((Y_hat - Y_bar) ** 2)
RSS = np.sum((My_Y - Y_hat) ** 2)

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
SE_Beta1 = cmath.sqrt(V_Beta1)
print("\nVariance of Beta1 = ", V_Beta1)
print("Standard Error of Beta1 : SE(B1) = ", SE_Beta1)

# Beta2's secret
V_Beta2 = MSE * ((Σx1_square) / (Σx1_square_Σx2_square - Σx1x2_square))
SE_Beta2 = cmath.sqrt(V_Beta2)
print("\nVariance of Beta2 = ", V_Beta2)
print("Standard Error of Beta2 : SE(B2) = ", SE_Beta2)

# Just some dudes needed for Beta0's top top secret...Ooooooo
F_bar_square = X1_bar ** 2
R_bar_square = X2_bar ** 2
F_bar_R_bar = X1_bar * X2_bar

# Biggest secret of all from Beta0's side
V_Beta0 = MSE * ((1 / n) + ((F_bar_square * Σx2_square + R_bar_square * Σx1_square - 2 * F_bar_R_bar * (Σx1x2)) / (
        Σx1_square_Σx2_square - Σx1x2_square)))
SE_Beta0 = cmath.sqrt(V_Beta0)
print("\nVariance of Beta0 = ", V_Beta0)
print("Standard Error of Beta0 : SE(B0) = ", SE_Beta0)

# Gonna catch em all , come here you all datassss
data_frame = pd.DataFrame(
    {
        "Yield": My_Y
        , "Fertilizer": My_X1
        , "Rainfall": My_X2

    }
)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(My_X1, My_X2, My_Y, c='r', marker='o')

# Title of the graph
ax.set_title('Multiple Linear Regression in Y,X1,X2 \n(Arsalan Ali 2017-ag-3648)')

# Labels for Axis
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


# Regression using Formula , needed for regression line
Reg = ols(formula="My_Y ~ My_X1 + My_X2", data=data_frame)
Fit2 = Reg.fit()


# Parameters to create Shape/Grid using Fertilizer and Rainfall Data
x_surf = My_X1
y_surf = My_X2

# The purpose of meshgrid is to create a rectangular grid out of an array of x and y values
x_surf, y_surf = np.meshgrid(x_surf, y_surf)

# To combine X and Y in order to generate Z for the surface
exog = pd.core.frame.DataFrame({
    "My_X1": x_surf.ravel()
    , "My_X2": y_surf.ravel()
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
plt.show()
print("\n", Fit2.summary())
print("\n", anova_lm(Fit2))

# We all know what this does , right? The End of our Assignment comes here.
plt.show()
