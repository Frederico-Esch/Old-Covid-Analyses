setwd("E:/Documetos (meus)/COVID/R")
library(ggplot2)

dataset <- read.csv("brazil_data.csv")
dataset <- dataset[1:4]
lregressor = lm(formula = dataset$NM ~ ., data = dataset)
prediction = predict(lregressor, newdata= dataset)

dataset$X2 <- dataset$X^2
dataset$X3 <- dataset$X^3
#dataset$X4 <- dataset$X^4
#dataset$X5 <- dataset$X^5

dataset$NC2 <- dataset$NC^2
dataset$NC3 <- dataset$NC^3
#dataset$NC4 <- dataset$NC^4
#dataset$NC5 <- dataset$NC^5

dataset$C2 <- dataset$C^2
dataset$C3 <- dataset$C^3
#dataset$C4 <- dataset$C^4
#dataset$C5 <- dataset$C^5

polyregressor = lm(formula = dataset$NM ~., data = dataset)
polypred = predict(polyregressor, newdata = dataset)

ggplot()+
  geom_line(aes(dataset$X, dataset$NM, color='data'), size = 1) +
  geom_line(aes(dataset$X, polypred, color='Poly model'), size = 1) +
  ylab( "Novas Mortes") +
  xlab("Dias")
summary(polyregressor) #third degree is the best right now
