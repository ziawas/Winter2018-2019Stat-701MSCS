x1<-c(100,200,300,400,500,600,700)
x2<-c(10,20,10,30,20,20,30)
y<-c(40,50,50,70,65,65,80)

mean(x1)
mean(x2)
mean(y)

hist(x1)
hist(x2)

summary(x1)
summary(x2)

relation<-lm(y~x1+x2)

print(summary(relation))


