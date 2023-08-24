#!/usr/bin/env python
# coding: utf-8

# # Question No. 1:
# What is Estimation Statistics? Explain point estimate and interval estimate.
Estimation statistics is a branch that involves using the data from a sample to make
inferences about the population.
There are two main types of estimates: point estimates and interval estimates.

Point Estimate: A point estimate is a single value that is used to estimate a population parameter. It is obtained by using a sample statistic, such as the sample mean or sample proportion, to estimate the corresponding population parameter.

Interval Estimate: An interval estimate, also called a confidence interval, is a range of values that is likely to contain the true population parameter with a certain level of confidence. It is obtained by using a sample statistic, such as the sample mean or sample proportion, to calculate an interval of values that is likely to contain the true population parameter.
# In[ ]:





# # Question No. 2:
# Write a Python function to estimate the population mean using a sample mean and standard deviation.

# In[2]:


import math

def population_mean(sample_mean, sample_std, sample_size):
    std_error = sample_std / math.sqrt(sample_size)
    z_value = 1.96 # assume a 95% confidence level and use the corresponding z-value
    margin_of_error = z_value * std_error 
    lower_bound = sample_mean - margin_of_error 
    upper_bound = sample_mean + margin_of_error 
    return ((lower_bound + upper_bound) / 2)


# In[3]:


result = population_mean(2,5,20000)

print(f"Population mean: {result}")


# # Question No. 3:
# What is Hypothesis testing? Why is it used? State the importance of Hypothesis testing.
Hypothesis testing is a statistical method used to make decisions or draw conclusions about a population based on a sample of data. It involves comparing a hypothesis or claim about a population parameter (such as a mean or proportion) with the data from a sample, in order to determine if the hypothesis is likely to be true.

Hypothesis testing is used to test the validity of a theory or claim.

For example, in medical research, hypothesis testing can be used to determine if a new drug is effective in treating a disease by comparing its effects to a placebo. In business, hypothesis testing can be used to evaluate whether a new marketing strategy is effective in increasing sales.

The importance of hypothesis testing lies in its ability to provide evidence for or against a theory or claim, and to help researchers make informed decisions based on data. It allows researchers to determine if an observed difference between groups or variables is statistically significant or simply due to chance, and to quantify the level of uncertainty in their findings. This can help researchers to draw conclusions that are based on evidence and minimize the risk of drawing incorrect or unsupported conclusions.
# In[ ]:





# # Question No. 4:
# Create a hypothesis that states whether the average weight of male college students is greater than the average weight of female college students.
# 
# Answer:
# The null hypothesis would be:
# 
# H0: The average weight of male college students is not greater than the average weight of female college students.
# 
# The alternative hypothesis would be:
# 
# H1: The average weight of male college students is greater than the average weight of female college students.

# In[ ]:





# # Question No. 5:
# Write a Python script to conduct a hypothesis test on the difference between two population means, given a sample from each population.

# In[5]:


import numpy as np
from scipy.stats import ttest_ind

# create two random samples
sample1 = np.random.normal(10, 2, 100)
sample2 = np.random.normal(12, 2, 100)

# conduct t-test
t_stat, p_val = ttest_ind(sample1, sample2)

# print results
print("t-statistic: ", t_stat)
print("p-value: ", p_val)

# check if p-value is significant at 5% level
if p_val < 0.05:
    print("Reject null hypothesis")
else:
    print("Fail to reject null hypothesis")


# In[ ]:





# # Question No. 6:
# What is a null and alternative hypothesis? Give some examples.
# 
# Answer:
# The null hypothesis (H0) states that there is no significant difference between two populations or variables. It is often the default or conventional position and is tested against the alternative hypothesis. In other words, it is the claim that researchers aim to reject or fail to reject based on the evidence from the data.
# 
# The alternative hypothesis (H1) is the complement of the null hypothesis and states that there is a significant difference between two populations or variables. It represents the claim that researchers seek to support or prove based on the evidence from the data.
# 
# Examples:
# 
# Null hypothesis: The average IQ scores of two groups of students are equal.
# Alternative hypothesis: The average IQ score of one group of students is significantly different from the other group.
# 
# Null hypothesis: The new drug has no effect on curing a disease.
# Alternative hypothesis: The new drug is significantly more effective in curing the disease than the current drug.

# In[ ]:





# # Question No. 7:
# Write down the steps involved in hypothesis testing.
# 
# Answer:
# The general steps involved in hypothesis testing are:
# 
# State the null and alternative hypotheses: Identify the research question and define the null and alternative hypotheses that represent the possible outcomes.
# Determine the test statistic: Choose an appropriate statistical test (e.g., t-test, ANOVA, chi-square) based on the research question and data type, and calculate the test statistic using the sample data.
# Set the significance level: Determine the level of significance (alpha) to use for the test. This is the probability of rejecting the null hypothesis when it is true and is typically set at 0.05.
# Calculate the p-value: Calculate the probability of observing the test statistic or a more extreme value under the null hypothesis.
# Make a decision: Compare the p-value to the significance level and make a decision whether to reject or fail to reject the null hypothesis. If the p-value is less than or equal to the significance level, reject the null hypothesis; otherwise, fail to reject the null hypothesis.

# In[ ]:




Question No. 8:
Define p-value and explain its significance in hypothesis testing.

Answer:
The p-value in hypothesis testing is the probability of observing a test statistic or a more extreme value, given that the null hypothesis is true. In other words, it is the probability of obtaining the observed data or more extreme data if the null hypothesis is true.
The p-value provides a measure of the strength of evidence against the null hypothesis. A small p-value indicates strong evidence against the null hypothesis, while a large p-value indicates weak evidence against the null hypothesis.

The p-value is a key component of hypothesis testing because it helps researchers make decisions about the null hypothesis. If the p-value is small (e.g., less than or equal to the significance level), it suggests that the observed data is unlikely to have occurred by chance under the null hypothesis, and the null hypothesis is rejected. If the p-value is large (e.g., greater than the significance level), it suggests that the observed data is consistent with the null hypothesis, and the null hypothesis is not rejected.
# In[ ]:





# # Question No. 9:
# Generate a Student's t-distribution plot using Python's matplotlib library, with the degrees of freedom parameter set to 1

# In[6]:


from scipy.stats import t
import matplotlib.pyplot as plt

#generate t distribution with sample size 10000
x = t.rvs(df=10, size=10000)

plt.hist(x, density=True, edgecolor='black', bins=20)


# In[ ]:





# # Question No. 10:
# Write a Python program to calculate the two-sample t-test for independent samples, given two random samples of equal size and a null hypothesis that the population means are equal.

# In[7]:


import numpy as np
from scipy.stats import ttest_ind

sample1 = np.random.normal(10, 2, 100)
sample2 = np.random.normal(12, 2, 100)

#calculate the t-test statistic and p-value
t_statistic, p_value = ttest_ind(sample1, sample2)

print("t-test statistic:", t_statistic)
print("p-value:", p_value)

#compare the p-value to the significance level
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis")


# In[ ]:





# # Question No. 11:
# What is Student’s t distribution? When to use the t-Distribution.
# 
# Answer:
# Student's t distribution is a probability distribution that is used in hypothesis testing when the sample size is small and the population standard deviation is unknown.
# It is similar to the standard normal distribution (z-distribution), but has heavier tails, which means it has more probability in the tails and less in the center compared to the standard normal distribution. The shape of the t-distribution depends on the sample size, with smaller sample sizes resulting in a more spread-out distribution.
# 
# 3The t-distribution is used in situations where the population standard deviation is unknown and must be estimated from the sample data.
# It is also used when the sample size is small (typically less than 30) and the population is normally distributed. The t-distribution allows for greater uncertainty in the estimate of the population standard deviation due to the smaller sample size.

# In[ ]:





# # Question No. 12:
# What is t-statistic? State the formula for t-statistic.
# 
# Answer:
# The t-statistic is a measure of how many standard errors the sample mean is from the hypothesized population mean, under the assumption that the population variance is unknown and must be estimated from the sample data. It is used in hypothesis testing to determine whether the difference between the sample mean and the hypothesized population mean is statistically significant.
# 
# The formula for the t-statistic is:
# t = (x̄ - μ) / (s / √n)
# 
# where:
# x̄ is the sample mean
# μ is the hypothesized population mean
# s is the sample standard deviation
# n is the sample size
# √n is the square root of the sample size

# In[ ]:





# # Question No. 13:
# A coffee shop owner wants to estimate the average daily revenue for their shop. They take a random sample of 50 days and find the sample mean revenue to be 500 dollars with a standard deviation of 50 dollars. Estimate the population mean revenue with a 95% confidence interval.
To estimate the population mean revenue with a 95% confidence interval, we can use the following formula:
    
    
    Confidence Interval = sample mean ± margin of error
    
    where the margin of error is given by:
        
        Margin of Error = critical value * standard error
        
        
        The standard error is the standard deviation of the sample divided by the square root of the sample size:

Standard Error = standard deviation / sqrt(sample size)



Standard Error = 50 / sqrt(50) = 7.07
Margin of Error = 1.96 * 7.07 = 13.85



herefore, the 95% confidence interval for the population mean revenue is:

500 ± 13.85, or (486.15, 513.85)

We can be 95% confident that the true population mean revenue falls within this interval.
# In[ ]:





# # Question No. 14:
# A researcher hypothesizes that a new drug will decrease blood pressure by 10 mmHg. They conduct a clinical trial with 100 patients and find that the sample mean decrease in blood pressure is 8 mmHg with a standard deviation of 3 mmHg. Test the hypothesis with a significance level of 0.05.

# # The following values are given in the question:
# 
# Population Mean = 10
# Sample Size = n = 100
# Sample Mean = 8
# Standard Deviation = 3
# Significance Level = 0.05
# Confidence Interval = 0.95
My null and alternate hypothesis are as follows:

Null Hypothesis = H0 => Population Mean = 10
Alternate Hypothesis = H1 => Population Mean != 10

From utilizing z-table i obgtained values for z-score:

z-score = ± 1.96

I got the following value:

-0.66

As -0.66 lies outside the region ± 1.96, that means it lies in the rejection region.
So my final conclusion was:

Reject the null hypothesis
# In[ ]:




Question No. 15:
An electronics company produces a certain type of product with a mean weight of 5 pounds and a standard deviation of 0.5 pounds. A random sample of 25 products is taken, and the sample mean weight is found to be 4.8 pounds. Test the hypothesis that the true mean weight of the products is less than 5 pounds with a significance level of 0.01.

Answer:
The following values are given in the question:

Population Mean = 5
Sample Size = n = 25
Sample Mean = 4.8
Standard Deviation = 0.5
Significance Level = 0.01
Confidence Interval = 0.99

My null and alternate hypothesis are as follows:

Null Hypothesis = H0 => Population Mean = 5
Alternate Hypothesis = H1 => Population Mean < 5

Then I utilized the follwing z-test formula:
image.png

I got the following value:

-2

From utilizing z-table i obgtained values for z-score of -2:

z-score = 0.02275

Which also becomes my p-value:

p-value = 0.02275

Then i checked whether p-value < significance value

0.02775 < 0.01
False

So my final conclusion was:

Failed to reject null hypothesis
# In[ ]:





# # Question No. 16:
# Two groups of students are given different study materials to prepare for a test. The first group (n1 = 30) has a mean score of 80 with a standard deviation of 10, and the second group (n2 = 40) has a mean score of 75 with a standard deviation of 8. Test the hypothesis that the population means for the two groups are equal with a significance level of 0.01.
# 
# Answer:
# My null and alternate hypothesis are as follows:
# 
# Null Hypothesis = H0 => Population Mean of Group 1 = Population Mean of Group 2
# Alternate Hypothesis = H1 => Population Mean of Group 1 != Population Mean of Group 2
# 
# Then I utilized the follwing two sample T-test formula:

# # I got the value of t as:
# 
# t = 2.37
# 
# Then I utilized t-table to look for the value of t for the following parameters:
# 
# Degrees of Freedom = 68
# Significance Value = 0.01
# 
# I got the following value of t fromt the table:
# 
# t = ± 2.638
# 
# Since 2.37 lies in the region ±2.638 so, the final conclusion was:
# 
# Failed to reject null hypothesis
# Population mean for two groups are equal
#     

# In[ ]:





# # Question No. 17:
# A marketing company wants to estimate the average number of ads watched by viewers during a TV program. They take a random sample of 50 viewers and find that the sample mean is 4 with a standard deviation of 1.5. Estimate the population mean with a 99% confidence interval.
# 
# Answer:
# To estimate the population mean with a 99% confidence interval, we can use the following formula:
# 
# CI = X̄ ± z*(σ/√n)
# 
# Where:
# 
# X̄ = sample mean (4)
# z = z-score corresponding to the confidence level (99%)
# σ = population standard deviation (1.5)
# n = sample size (50)
# 
# To find the z-score, we can use a standard normal distribution table. For a 99% confidence level, the z-score is
# 
# z-score = 2.576.
# 
# Plugging in the values, we get:
# 
# CI = 4 ± 2.576*(1.5/√50)
# CI = 4 ± 0.665
# 
# Therefore, the 99% confidence interval for the population mean of the number of ads watched by viewers during a TV program is (3.335, 4.665). We are 99% confident that the true population mean falls within this interval.

# In[ ]:




