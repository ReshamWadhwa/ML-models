**Variance inflation factor (VIF)**
---
is used to detect the severity of multicollinearity in the ordinary least square (OLS) regression analysis.

Variance Inflation Factors (VIFs) measure the correlation among independent variables in least squares regression models. Statisticians refer to this type of correlation as multicollinearity. Excessive multicollinearity can cause problems for regression models.

##Calculating Variance Inflation Factors

VIFs use multiple regression to calculate the degree of multicollinearity. Imagine you have four independent variables: X1, X2, X3, and X4. Of course, the model has a dependent variable (Y), but we don’t need to worry about it for our purposes. When your statistical software calculates VIFs, it uses multiple regression to regress all IVs except one on that final IV. It repeats this process for all IVs, as shown below:

X1 ⇐ X2, X3, X4 

X2 ⇐ X1, X3, X4 

X3 ⇐ X1, X2, X4 

X4 ⇐ X1, X2, X3

To calculate the VIFs, all independent variables become a dependent variable. Each model produces an R-squared value indicating the percentage of the variance in the individual IV that the set of IVs explains. Consequently, higher R-squared values indicate higher degrees of multicollinearity. VIF calculations use these R-squared values. The VIF for an independent variable equals the following:

**VIF formula.**

R-squared = Variance Explained (R2)

It records the proportion of variation in the dependent variable explained by the independent variables. In range [0,1] -- 0 means X doesn't explain any variance in Y and hence has no impact at all, 1 means X explains all variation present in Y

In case of overfit, R2 will still be high if too many independent features are present . Adjusted R2 considers the nummber of features as well.
```
Adjusted R Squared = 1 – [((1 – R2) * (n – 1)) / (n – k – 1)]

n == data points 
k == number of independent feature variables
Now, in VIF, all independent features are modelled against other IFs. R-squared is coefficient of determination of these individual features.
```
If R-sq of X1 =0 , it means that other features do not explain any of its variance.
```
Tolerance of i-th feature = 1- R-squared_i
```
i.e., how much variance is left unexplained when using the given features.

```
VIF of i-th feature = 1/tolerance

VIFi = 1/(1-R2)
```
Higher the explained variance for a coef, lower the tolerance, higher the VIF.

---
---
## The potential solutions include the following:

1. Remove some of the highly correlated independent variables.
2. Linearly combine the independent variables, such as adding them together.
3. Perform an analysis designed for highly correlated variables, such as principal components analysis or partial least squares regression.
4. LASSO and Ridge regression are advanced forms of regression analysis that can handle multicollinearity. 
