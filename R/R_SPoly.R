setwd("E:/Documetos (meus)/COVID/R")
library(ggplot2)

dataset <- read.csv("brazil_data.csv")
dataset <- data.frame(
  X = dataset$X,
  NM = dataset$NM)
lregressor = lm(formula = dataset$NM ~ ., data = dataset)
prediction = predict(lregressor, newdata= dataset)

dataset$X2 <- dataset$X^2
dataset$X3 <- dataset$X^3
dataset$X4 <- dataset$X^4
dataset$X5 <- dataset$X^5

poly5regressor = lm(formula = dataset$NM ~ ., data = dataset)
poly5pred = predict(poly5regressor, newdata = dataset)

poly2regressor = lm(formula = dataset$NM ~ dataset$X + dataset$X2, data = dataset)
poly2pred = predict(poly2regressor, newdata = dataset)

poly3regressor = lm(formula = dataset$NM ~ dataset$X + dataset$X2 + dataset$X3, data = dataset)
poly3pred = predict(poly3regressor, newdata = dataset)

poly4regressor = lm(formula = dataset$NM ~ dataset$X + dataset$X2 + dataset$X3 + dataset$X4, data = dataset)
poly4pred = predict(poly4regressor, newdata = dataset)

ggplot()+
  geom_line(aes(dataset$X, dataset$NM, color='data'), size = 1) +
  geom_line(aes(dataset$X, prediction, color='Linear model'), size = 1) +
  geom_line(aes(dataset$X, poly2pred, color='Poly 2 model'), size = 1) +
  geom_line(aes(dataset$X, poly3pred, color='Poly 3 model'), size = 1) +
  geom_line(aes(dataset$X, poly4pred, color='Poly 4 model'), size = 1) +
  geom_line(aes(dataset$X, poly5pred, color='Poly 5 model'), size = 1) +
  ylab( "Novas Mortes") +
  xlab("Dias")
summary(poly5regressor)
summary(poly3regressor)
