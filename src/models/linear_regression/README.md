Dataset source - https://www.kaggle.com/mdrazakhan/linear-regression-dataset/version/2


**Ques. What is Linear Regression?**

**Ans .** Linear Regression is the process of modelling a relationship between dependent variable , aka target, and the independendent variables.
I will use the notation X for set of independent variables and Y as the set of all values of target variables.

A linear regression line has an equation of the form 
```
Y = b + wX 
```
where 
    
    X is the explanatory variable and 
    Y is the dependent variable. 
    w is the slope of the line 
    b is the intercept/bias (the value of y when x = 0).

**Ques. Why do we need an intercept term or the bias term ?**

**Ans. ** When bias is absent
```
y = w1x1 + w2x2 + w3x3+ ... + wnxn
```
For situation when x1=x2=x3 = 0 , our y is forced to be 0. This might lead to underfit or bias in model if original data fit doesn;t pass through 0 but we force it to do so. Hence to avoid bias wrt origin, a bias term is added to the equation and the model

**Ques. What are the assumptions about data before fitting a Linear Regressor?**

**Ans. ** 

**1. Data Target variable is continuous.**

Continuous data is a type of numerical data that refers to the unspecified number of possible measurements between two realistic points.For instance, price of houses in a given locality. 
    
_**But why?**_
Because if the target/outcome is not continuous, then we will need to think of a classifier instead of a regressor.

**2. Linear relationship in y and X.**

Relationship between dependent and independent variables is linear. The linearity assumption can be tested using scatter plots. 
    
**_But Why?_** Because Non linear data relationships cannot be captured by sum of scalar matrix multiplications - how LR works

**3. Little or no multi-collinearity.**

Features shouldn't be dependent on each other.

There shouldn't be high correlation between two or more independent variables i.e., X.
    
**_But why_**? 

Because coefficients/weights are reflective of change in that feature only while computing Y. 
Let say , 
 ```
 y = w1a1 + w2a2 + w3a3 + w0 //(bias)
 ```
   and that a1 and a2 are correlated.

Now, model's interpretation of w1 is the change in y caused by a unit change in a1 alone and no other feature, however since a1 and a2 are correlated, this assumption fails. Can be resolved using VIF ( Variance Inflation Factor ) 

**4. Little or no auto-correlation/Independence of observations.**

Autocorrelation is when a variable is related to earlier versions of itself. One example is time series data.
Another example can be before and after measurements. 

_**But why?**_  Because the model attempts to fit the linear equation between y and X and not y with y_i-1. This way, its not that model is wrong but we are missing out one of the known determinants of models i.e, historic values of y .

**5. Homoscedasticity**

Homoscedasticity describes a situation in which the error term (that is, the “noise” or random disturbance in the relationship between the independent variables and the dependent variable) is the same across all values of the independent variables. The variance of the residuals is constant.

**But why ?** 10% change in lower value of x will result in lower error than 10% change in x when it is equal to 1,000,000. This is a case when error will have different variance across different range of features.

Can be solved by using Weighted Least Square Model - This type of regression assigns a weight to each data point based on the variance of its fitted value.

**6. All independent variables are uncorrelated with the error term i.e., absence of endogeniety**
 
Endogeneity broadly refers to situations in which an explanatory variable is correlated with the error term.

_**But why?**_  Let say an independent variable X is positively correlated with  residual -- unexplained error.
It means, as we increase X, error increases. This dissatisfies the homoscedasticity assumption.

**7. The residuals of the model are normally distributed.**

**Ans.** Normality is not necessarily a good assumption in general. 
The normal distribution has very light tails, and this makes the regression estimate quite sensitive to outliers. When working with those hypothesis, squared-erros based regression and maximum likelihood provide you the same solution. You are also capable of getting simple F-tests for coefficient significance, as well as confidence intervals for your predictions.

**_But why?_** the reason why we often choose normal distribution is its properties, which often make things easy. It is also not a very restrictive assumption, as many other types of data will behaive "kind-of-normally"
