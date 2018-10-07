install.packages("scatterplot3d") 
library("scatterplot3d") 

Fertilizer = c(100, 200, 300, 400, 500, 600, 700)  
Rainfall = c(10, 20, 10, 30, 20, 20, 30)  
Yield = c(40, 50, 50, 70, 65, 65, 80) 

df = data.frame(Fertilizer,Rainfall,Yield)

data(df)
head(df)

s3d <- scatterplot3d(df, type = "h", color = "blue",
    angle=55, pch = 16,grid=TRUE, box=FALSE,


              main="Multiple Linear Regression",
              xlab = "Fertilizer (Pound)",
              ylab = "Rainfall (Inches)",
              zlab = "Yield (Bushel)")


my.lm <- lm(Yield~Fertilizer+Rainfall)
s3d$plane3d(my.lm)


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

	
	Y_hat = B0 + B1*Fertilizer + B2*Rainfall
	Sum_Y_hat = sum(B0 + B1*Fertilizer + B2*Rainfall)

	
	TSS = sum((Yield - mean.Y)^2)
	MSS = sum((Y_hat - mean.Y)^2)
	RSS = sum((Yield - Y_hat)^2)

	
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


Exp.data = cbind(Fertilizer , Rainfall , Yield)


colnames(Exp.data) = c('Fertilizer' , 'Rainfall' , 'Yield')


Exp.data


Exp.regression<- MLR( Fertilizer, Rainfall, Yield )


Exp.regression