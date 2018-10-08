x1<-c(0,0,10,10,20,20)
x2<-c(0,0,100,100,400,400)
y<-c(5,7,15,17,9,11)

mean(x1)
mean(x2)
mean(y)

hist(x1)
hist(x2)

summary(x1)
summary(x2)

relation<-lm(y~x1+x2)

print(summary(relation))




