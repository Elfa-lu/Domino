library(xgboost)
library(insuranceData) # example dataset https://cran.r-project.org/web/packages/insuranceData/insuranceData.pdf
library(tidyverse) 
library(tidypredict)

# load insurance data (1 row = 1 policy)
data(dataCar)

label_var <- "numclaims" # number of claims during policy
offset_var <- "exposure" # length of exposure (anywhere between 0.001 year and 1.0 year)
feature_vars <- c("veh_value", "veh_body", "veh_age", "gender", "area", "agecat")

mydb <- dataCar %>% select(one_of(c(label_var, offset_var, feature_vars)))

# create dummies from factor variables
myformula <- paste0( "~", paste0( feature_vars, collapse = " + ") ) %>% 
  as.formula()

dummyFier <- caret::dummyVars(myformula, data=mydb, fullRank = TRUE)
dummyVars.df <- predict(dummyFier,newdata = mydb)
mydb_dummy <- cbind(mydb %>% select(one_of(c(label_var, offset_var))), 
                    dummyVars.df)
rm(myformula, dummyFier, dummyVars.df)

# get  list the column names of the db with the dummy variables
feature_vars_dummy <-  mydb_dummy  %>% 
  select(-one_of(c(label_var, offset_var))) %>% 
  colnames()

# create xgb.matrix for xgboost consumption
mydb_xgbmatrix <- xgb.DMatrix(
  data = mydb_dummy %>% select(feature_vars_dummy) %>% as.matrix, 
  label = mydb_dummy %>% pull(label_var),
  missing = "NAN")

#base_margin: apply exposure offset  (more claims are expected if you are insured 1.0 year rather than 0.20 year )
setinfo(mydb_xgbmatrix,"base_margin", 
        mydb %>% pull(offset_var) %>% log() )

params <- data.frame(max_depth = 6,
                           colsample_bytree= 0.8,
                           subsample = 0.8,
                           min_child_weight = 3,
                           eta  = 0.1,
                           gamma = 0,
                     objective = 'count:poisson', 
                     eval_metric = "poisson-nloglik"
                     ) 

model <- xgb.train(mydb_xgbmatrix, params = params, nrounds=100)

mean(mydb_dummy$numclaims) # 0.07275701
mean(predict(model, newdata=mydb_xgbmatrix)) # 0.07525851
