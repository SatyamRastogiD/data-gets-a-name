#Simulate Linear regression for n VAriables and N observations


simulate_linear_regression <- function(N_row =10,N_var=2) {

    df <- as.data.frame(matrix(rnorm(N_row*N_var) , ncol = N_var, nrow = N_row))
    print("--------------DataFrame Created----------------")
    print(df)
    print("--------------Summary of the Data--------------")
    print(summary(df))
    print("--------------Graphs - check the plot window----")
    for (i in (1:ncol(df))){
      par(mfrow=c(2,1))
      boxplot(df[,i], main = paste("Boxplot of", names(df)[i]), 
              ylab = names(df)[i], col = "maroon", border = "grey5",
              horizontal = T)
      hist(df[,i], main = paste("Histogram of", names(df)[i]), 
           xlab = names(df)[i], ylab = "Values of the variable", col = "red", border=F)
      
    }
    print("---------------Correlation among the variables--------")
    res <- cor(df)
    print(round(res, 2))

    #correlation plot
    library(ggcorrplot)
    ggcorrplot(res, hc.order = TRUE, type = "lower",
               lab = TRUE)
    
    # Simple/Multiple Linear Regression
    y <- names(df[ncol(df)])
    z = paste(y,paste('~',paste(colnames(df)[1:ncol(df)-1], collapse=" + ")))
    model <- lm(formula = z, df)
    print("---------------Linear Regression Summary---------")
    print(summary(model))
} 

simulate_linear_regression(10,4)
