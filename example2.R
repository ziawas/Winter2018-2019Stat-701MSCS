install.packages("scatterplot3d") 
library("scatterplot3d") 


X1 = c(0,0,10,10,20,20)   
X2= c(0,0,100,100,400,400)  
Y = c(5,7,15,17,9,11) 

df = data.frame(X1,X2,Y)


data(df)
head(df)
scatterplot3d(x=X1, y=X2, z=Y)
s3d <- scatterplot3d(df, type = "p", color = "blue",
    angle=55, pch =16,grid=TRUE, box=FALSE,


              main="Multiple Linear Regression",
              xlab = "X1",
              ylab = "X2",
              zlab = "Y")


my.lm <- lm(Y~X1+X2)



s3d$plane3d(my.lm, lty.box = "solid",  draw_polygon = TRUE)

MLR<- function( X1, X2, Y )
{

	
	n = length(Y)

	
	mean.X1 = mean(X1)
	mean.X2 = mean(X2)
	mean.Y = mean(Y)

	
	x1 = X1 - mean.X1
	x2 = X2 - mean.X2
	y = Y - mean.Y
	
	
	Sum_x1 = sum(x1)
	Sum_x2 = sum(x2)
	Sum_y = sum(y)

	
	x1_sq = sum((x1)^2)
	x2_sq = sum((x2)^2)
	y_sq = sum((y)^2)

	
	Sum_x1y = sum((x1*y))
	Sum_x1_sq = sum((x1)^2)
	Sum_x2_sq = sum((x2)^2)
	Sum_x2y = sum((x2*y))
	Sum_x1x2 = sum((x1*x2))

	Sum_x1y_Sum_x2_sq = Sum_x1y*Sum_x2_sq
	Sum_x2y_Sum_x1x2 = Sum_x2y*Sum_x1x2
	Sum_x1_sq_Sum_x2_sq = Sum_x1_sq*Sum_x2_sq
	Sum_x1x2_sq = (Sum_x1x2)^2

	B1 = (Sum_x1y_Sum_x2_sq - Sum_x2y_Sum_x1x2) / (Sum_x1_sq_Sum_x2_sq - Sum_x1x2_sq)

	B2 = ((Sum_x2y*Sum_x1_sq) - (Sum_x1y*Sum_x1x2)) / (Sum_x1_sq_Sum_x2_sq - Sum_x1x2_sq)

	B0 = mean.Y - (B1*mean.X1) - (B2*mean.X2)

	
	k = 3	

	
	Y_hat = B0 + B1*X1 + B2*X2
	Sum_Y_hat = sum(B0 + B1*X1 + B2*X2)

	TSS = sum((Y - mean.Y)^2)
	MSS = sum((Y_hat - mean.Y)^2)
	RSS = sum((Y - Y_hat)^2)

	R_sq = MSS / TSS

	
	MSE = RSS / (n - k)

	
	V_B1 = MSE*((Sum_x2_sq) / (Sum_x1_sq_Sum_x2_sq - Sum_x1x2_sq))
	SE_B1 = sqrt(V_B1)

	
	V_B2 = MSE*((Sum_x1_sq) / (Sum_x1_sq_Sum_x2_sq - Sum_x1x2_sq))
	SE_B2 = sqrt(V_B2)

	mean.X1_sq = mean.X1^2
	mean.X2_sq = mean.X2^2
	mean.X1_mean.X2 = mean.X1*mean.X2

	V_B0 = MSE*((1 / n) + ((mean.X1_sq*Sum_x2_sq + mean.X2_sq*Sum_x1_sq - 2*mean.X1_mean.X2*(Sum_x1x2)) / (Sum_x1_sq_Sum_x2_sq - Sum_x1x2_sq)))
	SE_B0 = sqrt(V_B0)

	cat("Mean of X1 = ", mean.X1, "\n")
	cat("Mean of X2 = ", mean.X2, "\n")
	cat("Mean of Y = ", mean.Y, "\n")
	cat("\n")
	cat("Sum of Deviations of X1 = " ,Sum_x1, "\n")
	cat("Sum of Deviations of X2 = " ,Sum_x2, "\n")
	cat("Sum of Deviations of Y = " ,Sum_y, "\n")
	cat("\n")
	cat("Sum of Square of X1 : Sum_x1 = " ,x1_sq, "\n")
	cat("Sum of Square of X2 : Sum_x2 = " ,x2_sq, "\n")
	cat("Sum of Square of Y : Sum_y = " ,y_sq, "\n")
	cat("\n")
	cat("Beta1  = " ,B1, "\n")
	cat("Beta2  = " ,B2, "\n")
	cat("Beta0  = " ,B0, "\n")
	cat("\n")
	cat("Sum of Y-hat = ", Sum_Y_hat , "\n")
	cat("\n")
	cat("Total Sum of Squares : TSS = ", TSS , "\n")
	cat("Model Sum of Squares : MSS = ", MSS , "\n")	
	cat("Residual Sum of Squares : RSS = ", RSS , "\n")
	cat("\n")
	cat("Regression Co-efficient : R^2 = ", R_sq, "\n")
	cat("\n")
	cat("Mean Square Error : MSE = ",MSE,"\n")
	cat("\n")
	cat("Variance of Beta1 = ",V_B1, "\n")
	cat("Standard Error of Beta1 = ",SE_B1, "\n")
	cat("\n")
	cat("Variance of Beta2 = ",V_B2,"\n")
	cat("Standard Error of Beta2 = ",SE_B2, "\n")
	cat("\n")
	cat("Variance of Beta0 = ",V_B0,"\n")
	cat("Standard Error of Beta0 = ",SE_B0, "\n")

	df2 = data.frame(X1,X2,Y)

	fit <- lm(Y ~ X1 + X2, data=df2)
	summary(fit)

	}


Exp.data = cbind(X1, X2, Y)

colnames(Exp.data) = c('X1' , 'X2' , 'Y')

Exp.data

Exp.regression<- MLR( X1, X2, Y)


Exp.regression