data=read.table(file.choose(),header=TRUE)
data
library(e1071)
n=dim(data)[1]
index = sample(n, 0.7 * n)
Appren = data[index, ]
Test = data[-index, ]
nb.model <- naiveBayes(playTennis ~ ., data = Appren)
nb.model
Pred=predict(object = nb.model, newdata = Test)
Pred
Test.mod <- cbind(Test, Pred)
head(Test.mod, 5)
Confusion = table(Test.mod$playTennis, Test.mod$Pred)
Confusion
x=c('Rain','Mild','High','Strong')
newdata=as.vector(x)
newdata
Pred=predict(object = nb.model, newdata = t(newdata))
Pred