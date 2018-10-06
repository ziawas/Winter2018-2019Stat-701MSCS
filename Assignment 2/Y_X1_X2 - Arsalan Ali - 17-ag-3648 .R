#########################################
### Assignment 2 : MS(CS) - Stats 701 : Y | X1 | X2 : Part 2
###Student name: Arsalan Ali , Registration no. 2017-ag-3648 , Degree and Session : MS(CS) 2017-2019
#########################################

#Installing packages for 3D-graph
install.packages("scatterplot3d") 
library("scatterplot3d") 

#########################################
###			ITS OUR DATA
#########################################

My_X1 = c(0,0,10,10,20,20)   
My_X2= c(0,0,100,100,400,400)  
My_Y = c(5,7,15,17,9,11) 

#Combining all the Data into a Data-frame
df = data.frame(My_X1,My_X2,My_Y)

#########################################
###			3D GRAPH CODE
#########################################

# Code for the 3D-plot and Regression line, it looks complex but it's alright
data(df)
head(df)
scatterplot3d(x=My_X1, y=My_X2, z=My_Y)
s3d <- scatterplot3d(df, type = "p", color = "blue",
    angle=55, pch =16,grid=TRUE, box=FALSE,


              main="Multiple Linear Regression \n By Arsalan Ali \n 2017-ag-3648",
              xlab = "X1",
              ylab = "X2",
              zlab = "Y")

# Using Pre-defined MLR function for the 3D-graph
my.lm <- lm(My_Y~My_X1+My_X2)
#s3d$plane3d(my.lm)

# To highlight the Regression Line/Shape
s3d$plane3d(my.lm, lty.box = "solid",  draw_polygon = TRUE)


#############################################
###				THE MAIN FUNCTION
#############################################

#This is the Custom MLR function
MLR<- function( X1, X2, Y )
{

	# Size of the input, can even take X too
	n = length(Y)

	# Mean of X1, X2 and Y
	mean.X1 = mean(X1)
	mean.X2 = mean(X2)
	mean.Y = mean(Y)

	# Let's deviate from the mean mood please
	x1 = X1 - mean.X1
	x2 = X2 - mean.X2
	y = Y - mean.Y
	
	# Summing up our deviations gets us nowhere, you know that right?
	Sum_x1 = sum(x1)
	Sum_x2 = sum(x2)
	Sum_y = sum(y)

	# Doubling and them summing up the deviations , now we're talking
	x1_square = sum((x1)^2)
	x2_square = sum((x2)^2)
	y_square = sum((y)^2)

	# Just some formulas in order to get all the Betas
	Sum_x1y = sum((x1*y))
	Sum_x1_square = sum((x1)^2)
	Sum_x2_square = sum((x2)^2)
	Sum_x2y = sum((x2*y))
	Sum_x1x2 = sum((x1*x2))

	Sum_x1y_Sum_x2_square = Sum_x1y*Sum_x2_square
	Sum_x2y_Sum_x1x2 = Sum_x2y*Sum_x1x2
	Sum_x1_square_Sum_x2_square = Sum_x1_square*Sum_x2_square
	Sum_x1x2_square = (Sum_x1x2)^2

	Beta1 = (Sum_x1y_Sum_x2_square - Sum_x2y_Sum_x1x2) / (Sum_x1_square_Sum_x2_square - Sum_x1x2_square)

	Beta2 = ((Sum_x2y*Sum_x1_square) - (Sum_x1y*Sum_x1x2)) / (Sum_x1_square_Sum_x2_square - Sum_x1x2_square)

	Beta0 = mean.Y - (Beta1*mean.X1) - (Beta2*mean.X2)

	# Number of parameters e.g, All the Betas
	k = 3	

	# Our dearly Y wearing a Hat. The Y-predicted
	Y_hat = Beta0 + Beta1*X1 + Beta2*X2
	Sum_Y_hat = sum(Beta0 + Beta1*X1 + Beta2*X2)

	# Here comes the big league
	TSS = sum((Y - Y_hat)^2)
	MSS = sum((Y_hat - mean.Y)^2)
	RSS = sum((Y - Y_hat)^2)

	# The one and only Regression Co-efficient
	R_square = MSS / TSS

	# Mean Square Error coming through.....clear the wayyyyy
	MSE = RSS / n - k

	# Beta1's secret
	V_Beta1 = MSE*((Sum_x2_square) / (Sum_x1_square_Sum_x2_square - Sum_x1x2_square))
	SE_Beta1 = sqrt(V_Beta1)

	# Beta2's secret
	V_Beta2 = MSE*((Sum_x1_square) / (Sum_x1_square_Sum_x2_square - Sum_x1x2_square))
	SE_Beta2 = sqrt(V_Beta2)

	# Just some dudes needed for Beta0's top top secret...Ooooooo
	mean.X1_square = mean.X1^2
	mean.X2_square = mean.X2^2
	mean.X1_mean.X2 = mean.X1*mean.X2

	# Biggest secret of all from Beta0's side
	V_Beta0 = MSE*((1 / n) + ((mean.X1_square*Sum_x2_square + mean.X2_square*Sum_x1_square - 2*mean.X1_mean.X2*(Sum_x1x2)) / (Sum_x1_square_Sum_x2_square - Sum_x1x2_square)))
	SE_Beta0 = sqrt(V_Beta0)

	# These are all the Outputs that will appear in Console

	cat("Mean of X1 = ", mean.X1, "\n")
	cat("Mean of X2 = ", mean.X2, "\n")
	cat("Mean of Y = ", mean.Y, "\n")
	cat("\n")
	cat("Sum of Deviations of X1 = " ,Sum_x1, "\n")
	cat("Sum of Deviations of X2 = " ,Sum_x2, "\n")
	cat("Sum of Deviations of Y = " ,Sum_y, "\n")
	cat("\n")
	cat("Sum of Square of X1 : Sum_x1 = " ,x1_square, "\n")
	cat("Sum of Square of X2 : Sum_x2 = " ,x2_square, "\n")
	cat("Sum of Square of Y : Sum_y = " ,y_square, "\n")
	cat("\n")
	cat("Beta1  = " ,Beta1, "\n")
	cat("Beta2  = " ,Beta2, "\n")
	cat("Beta0  = " ,Beta0, "\n")
	cat("\n")
	cat("Sum of Y-hat = ", Sum_Y_hat , "\n")
	cat("\n")
	cat("Total Sum of Squares : TSS = ", TSS , "\n")
	cat("Model Sum of Squares : MSS = ", MSS , "\n")	
	cat("Residual Sum of Squares : RSS = ", RSS , "\n")
	cat("\n")
	cat("Regression Co-efficient : R^2 = ", R_square, "\n")
	cat("\n")
	cat("Mean Square Error : MSE = ",MSE,"\n")
	cat("\n")
	cat("Variance of Beta1 = ",V_Beta1, "\n")
	cat("Standard Error of Beta1 = ",SE_Beta1, "\n")
	cat("\n")
	cat("Variance of Beta2 = ",V_Beta2,"\n")
	cat("Standard Error of Beta2 = ",SE_Beta2, "\n")
	cat("\n")
	cat("Variance of Beta0 = ",V_Beta0,"\n")
	cat("Standard Error of Beta0 = ",SE_Beta0, "\n")

	df2 = data.frame(X1,X2,Y)

	# Since i can't do Anova etc manually so here's the pre-defined ones
	fit <- lm(Y ~ X1 + X2, data=df2)
	summary(fit)

	}

# Combines the Data-set of My_X1, My_X2 and My_Y
Exp.data = cbind(My_X1, My_X2, My_Y)

# Creates columns that we can display for our Data-set
colnames(Exp.data) = c('My_X1' , 'My_X2' , 'My_Y')

# Calls the Table-Data function to generate Table
Exp.data

# This will load the entire Regression-Calculation process

Exp.regression<- MLR( My_X1, My_X2, My_Y)

# Executes the above function
Exp.regression

