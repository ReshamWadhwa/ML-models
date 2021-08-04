
**Ques. What is Logistic Regression?** 

**Ans.** Logistic regression is a classification algorithm. It is used to predict a binary outcome based on a set of independent variables.

---
---
---

**Ques. What are the assumptions of a Logistic Regressor?**

**Ans.** Logistic Regression's assumptions about data are listed below along with their reasons.


**1. The Response Variable is Binary**

Logistic Regression is a classification problem typically for binary outcomes.

**But why?** If the target/dependendent/response variable is non binary or continuous, then Logistic Regression won't give meaningful results as the sigmoid function + loss function test the predictions wrt dichotomy of classes

**2. Observations are independent of each other**

The observations should not come from repeated measurements of the same individual or be related to each other in any way.The dataset should not contain duplicate or repeated values.
That is that the data-points should not be from any dependent samples design,
e.g., before-after measurements, or matched pairings

**But Why?** 
 Because Logistic Regression uses Maximum Likelihood Estimation for minimising loss function. Property of MLE is that it works on binomial distribution with independent data samples.

**3. There is No Multicollinearity Among Explanatory Variables**

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


**4. Large sample size**

**But why?** Because maximum likelihood estimates are less powerful than ordinary least squares (e.g., simple linear regression, multiple linear regression); whilst OLS needs 5 cases per independent variable in the analysis, ML needs at least 10 cases per independent variable, some statisticians recommend at least 30 cases for each parameter to be estimated.


**5. Linear relationship between observations and their logits**
```
 Logit(p)  = log(p / (1-p))
```
 where p is the probability of success
 
 also known as a log-odds function

**But why?** 
The linear part of the model (the weighted sum of the inputs == wx+b ) calculates the log-odds of a successful event, specifically, the log-odds that a sample belongs to class 1. Logistic Regression then proceeds to calculate loss function on the basis of this logit.

**6. There are No Extreme Outliers in the data.**

---
---
---
**Question. What is the equation for Logistic Regression?**

**Ans.** 

 Feature Vector : x = [x_1, x_2, …., x_n]

 Response vector : y = [y_1, y_2, …., y_n] where all y = 0 or 1
 
    h( x ) = sigmoid(w * x + b  )
    
   b = bias -- needed

   x represents the feature vector
   
   w represents the weight vector.


```
sigmoid(z) = 1/(1+e^-z)
```


There are two common ways to optimize weights in Modeling :

1. Least Squares Optimization (iteratively reweighted least squares).
2. Maximum Likelihood Estimation.

Logistic Regression uses MLE

---
---
---
**Ques. Why is the bias term added ? bias term = b**

**Ans**. For situation when x1=x2=x3 = 0 , our y is forced to be 0.5 (sigmoid of 0 = 0.5) . This might lead to underfit or bias in model if original data fit doesn;t pass through 0 but we force it to do so. Hence to avoid bias wrt the stagnant point 0.5, a bias term is added to the equation and the model

---
---
---
**Quess. What is the log odds process to wrt Logistic Regression?**

**Ans.**  The linear part of the model (the weighted sum of the inputs == wx+b ) calculates the **log-odds** of a successful event, specifically, the log-odds that a sample belongs to class 1.

```
log-odds = w0+w1x1 + w2x2+....
```
Odds = Probability of success/probability of failure

In Binomial distribution (Two possible outcomes: true or false, success or failure, yes or no), probability of failure = 1- probability of success for one event.

hence, 

```
odds = p/(1-p)
```

Log odds is log of this value == Logit == Logistic Unit

```
log-odd = log(p/(1-p))
```

Now, this is the linear part of the Logistic Regression classification . 

Hence, 
```
log ( p/(1-p) ) = w0+w1x1 + w2x2+....+ wnxn
```

What we eventually want is p and that can be obtained by taking exponents of log odds. 

```
odds = p/(1-p) = exp ( w0 + w1x1 + w2x2... + wnxn)
```

Now, odds can be converted into probability as follows 
```
odds = p/(1-p)

odds(1-p) = p
odds - p*odds = p 
odds = p+p*odds
odds = p(1+odds)
Hence, 
p = odds/(1+odds)


p = exp( log_odds ) / ( 1 + exp(log_odds))

p = (1/exp(-log_odds)) / (1+ 1/exp(-log_odds)

Let log_odds = l

p = (1/e(-l) ) / (1+ 1/e(-l) )
```

Taking 1/e(-l) commom in both numerator and denominator and cancelling, 
```
p = 1/ ( 1+e(-log_odds))

``` 

---
---
---
**Quess. What is the Maximum Likelihood Estimation wrt Logistic Regression?**

**Ans.** MLE is a probabilistic framework for estimating the parameters of a model. We wish to maximize the conditional probability of observing the data (X) given a specific probability distribution and its parameters (W), stated formally as:

P(X ; W)

i.e., what is the probability of finding X ( combination of all input features values) with W weights. MLE works to maximize this. 

the joint probability distribution of all observations from the problem domain from 1 to n.
```
P ( x1, x2 , x3... | W). == likelihood of observing this data point given a set of weights == conditional probability = L ( X | W)
```
```
Joint probability = P ( x1,x2,x3...) = P(x1).P(x2)...
```
But multiplying small values can be unstable (Probabilities are <1)

Hence log is applied. Log fits because it is monotonous like the likelihood functions hence peaks for both shall be same. Also , log of multiplying factors converts to sum which is much easier to interpret. 

``` 
𝑙𝑜𝑔(𝑥^𝑝 . 𝑥^𝑞)=𝑝 𝑙𝑜𝑔(𝑥)+𝑞 𝑙𝑜𝑔(𝑥)
```
Hence log likelihood is calculated. 

```
Log Likelihood = sum i to n log(P(xi ; W))
```

However , this is still in terms of maximizing the likelihood. Most training models prefer to minimise a cost function. Hence negative of log likelihood is used.
```
minimize -sum i to n log(P(xi ; W))
```

The process of finding parameters such that log likelihood is maximum is called Maximum Likelihood Estimation or MLE.

In terms of Machine Learning Models, we used this concept to find the hypotheses h and set of model parameters ( w0,w1..., b) such that it best explains the input features X.


Hence, we find the modeling hypothesis that maximizes the likelihood function 
```
maximize sum i to n log(P(xi ; W))
```
Supervised learning like Logistic Regression learning can be considered as 
predicting output given the input i.e., P ( y | x) 

Hence, in logistic regression we aim to 
```
maximize sum i to n log(P(yi|xi ; h))
```
Now, hypothesis h is our Logistic Model. hence

In order to use maximum likelihood, we need to assume a probability distribution. In the case of logistic regression, a Binomial probability distribution is assumed for the data sample, where each example is one outcome of a Bernoulli trial. The Bernoulli distribution has a single parameter: the probability of a successful outcome (p).
```
P(y=1) = p
P(y=0) = 1 – p
```

The expected value (mean) of the Bernoulli distribution can be calculated as follows:
```
mean = P(y=1) * 1 + P(y=0) * 0
```
or given p as success
```
mean = p * 1 + (1 – p) * 0
```
Hence,
```
likelihood = y' * y + (1 – y') * (1 – y)
```
---
---
---
**Ques. What is the loss function in Logistic Regression using MLE?**

**Ans.** We need a loss function that expresses, for an observation x, how close the classifier output ``` (ˆy = σ(w· x+b)) ``` is to the correct output (y, which is 0 or 1). 

We’ll call this:
L(yˆ, y) = How much ˆy differs from the true y

We do this via a loss function that prefers the correct class labels of the training examples to be more likely. This is called **conditional maximum likelihood estimation**: we choose the parameters w,b that maximize the log probability of the true y labels in the training data given the observations x. The resulting loss function is the negative log likelihood loss, generally called the **cross-entropy loss**.

Derivation :

Since there are just two outputs, we can express the conditional probability of y given x as

```
p(y|x) = y' ^y . (1−y')^(1−y). 

i.e 

predicted_y to the power of actual y multiplied by 1-predicted y to the poower of (1-actual y)
```
If y = 0, then p(0|x) = (1-y) 

If y = 1, then p(1|x) = y

Now, taking log both sides - 

```
log likelihood = log (py|x) = y log y' + (1-y) log (1-y') 

```
This function will always return a large probability when the model is close to the matching class value, and a small value when it is far away, for both y=0 and y=1 cases.

Finally, we can sum the likelihood function across all examples in the dataset to maximize the likelihood:
```
maximize sum i to n log(y'_i) * y_i + log(1 – y'_i) * (1 – y_i)
```

or minimise negative likelihood function or the Cross Entropy Loss, LCE
```
LCE(yˆ, y) = −[y log σ(w· x+b) + (1−y)log(1−σ(w· x+b))]


```
---
---
---
**Ques. Applying gradient descent on minimising Loss function and obtaining parameters in Logistic regression.**

**Ans.** We have defined our loss function in the previous question. 

```
LCE(yˆ, y) = −[y log σ(w· x+b) + (1−y)log(1−σ(w· x+b))]
```

We know, gradient descent starts with finding the direction of most descent and moves in that direction. Step size in the direction is determined by the learning rate.  Gradient descent is a method that finds a minimum of a function by figuring out in which direction (in the space of the parameters W) the function’s slope is rising the most steeply,
and moving in the opposite direction

For logistic regression, LCE is a convex function i.e., just one minima. 

The gradient of a function of many variables is a vector pointing in the direction of the greatest increase in a function

The gradient is just such a vector; it expresses the directional components of the sharpest slope along each of those N dimensions

```
Change in parameter, w = dW = del (LCE)/ del W

```

Which turns out to be
```
∂LCE(yˆ, y)/∂w_j = [σ(w· x+b)−y]x_j
```
---
---
---