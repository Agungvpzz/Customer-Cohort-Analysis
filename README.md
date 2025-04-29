> If you encounter an error with the Jupyter Notebook on GitHub, please use this link [nbviewer](https://nbviewer.org/github/Agungvpzz/Customer-Cohort-Analysis/blob/superstore/Cohort%20Analysis%20SuperStore.ipynb)

# Customer Cohort Analysis

## 1. Introduction
This report presents an in-depth analysis of customer cohorts. The analysis centers around understanding customer purchasing behavior, retention, and revenue patterns across different cohorts. Key findings shed light on customer trends, highlight high-performing cohorts, and provide actionable insights to enhance sales and customer satisfaction.

## 2. Business Understanding
**A. Business Goals**
- Customer cohort analysis enables businesses to segment customers based on shared behaviors and analyze these groups over time, aiming to improve retention by identifying churn patterns and enhancing customer experiences.

**B. Objective of this analysis**
- Examine customer purchasing habits over time, focusing on frequency and value, to inform targeted strategies.

**C. Key Questions to Answer**
1. What are the retention rates for each customer group and how do they change over time?
2. Which groups show the highest revenue growth?
3. Are there common trends that help predict future behavior in these groups?

## 3. Data Collection
The dataset can be accessed at the following link: https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting

## 4. Methodology
- Cohort Definition: Cohorts are defined based on the quarter of the customer's first purchase.
- Data Period: Data analyzed spans 4 years from January 2015 to December 2018.
- Cohort Analysis Period: The analysis centers on cohorts from the years 2015 and 2016.
- Main Analysis: Customer retention rates and sales growth over time.

## 5. Results and Analysis
### Cohort Overall Analysis

#### Cohort Overall Summary
<p align="center"><img src="https://github.com/user-attachments/assets/0ebe92e5-79bf-4a86-bd87-d804f0d9a202" alt="Description of image"></p>

- There are 730 customers in total, generating sales of 2,138,526.879 across 4,674 orders.
- The 2015 cohorts account for 80.5% of total customers, 83.9% of total sales, and 83.7% of total orders.
- Additionally, only 24.8% of customers across all cohorts remain active after 30 days.
- The top 20% of customers within each cohort collectively accounted for 46.6% of total sales.
- 41% of customers across all cohorts have been inactive for over 100 days, yet they have contributed up to 35% of total sales.

#### Cohort Overall Behaviour in fixed Period of Time:
<p align="center"><img src="https://github.com/user-attachments/assets/c1db9d2c-26e4-42be-a103-c0e5a957671e" alt="Description of image"></p>

- The first quarter experiences the lowest transaction activity, with 636 orders from 435 customers, accounting for 15% of total sales.
- In contrast, the last quarter sees a significant increase, with 1,761 orders from 664 customers, contributing 39.2% of total sales.

#### Cohort Overall Journey Behaviour:
<p align="center"><img src="https://github.com/user-attachments/assets/8ab17f2e-7f19-4739-8df9-31e6242967ae" alt="Description of image"></p>

- In the first quarter after the cohorts began, order activity declined to 24.1% compared to the initial order, originating from 24% of total customers, with total sales decreasing to 21.3% of the initial sales.
- By the eighth quarter, all metrics show gradual improvement but remain below half of their initial values, maintaining 38.5% order activity, driven by 35.4% of customers, while total sales stabilize at 42.9%.

---
### Cohort Compositions

#### Cohort Member Composition
![image](https://github.com/user-attachments/assets/bd672033-445a-41b3-a819-4772d54ecc88)
<br>As you can see, the cohorts from Q2, Q3, and Q4 of 2015 have the highest number of members, at approximately 20%.

#### Cohort Sales Composition
![image](https://github.com/user-attachments/assets/3db6d1f6-fa01-4c48-82aa-1be78163ab7f)
<br>All cohorts from the first year, 2015, contribute around 17–21% of total sales, accumulating to approximately 80% of the total sales.

---
### Customer Retention for each Cohort
With line charts displaying the cohorts in 2015 and 2016, we can clearly identify which cohorts are valuable for the business and observe common patterns across cohorts. <br>
![image](https://github.com/user-attachments/assets/d41c50de-3dd0-4dc9-8683-70397b90148f)

**The line chart shows that:**
- All the first-year cohorts from 2015 maintain varying customer retention ratios between 20% and 50%, with a mean of only 30–33%.
- All 2015 and 2016 cohorts lose over 50% of their customer retention during the first quarter of their existence.
<br>

The heatmap will help us identify patterns across cohorts by comparing the condition of each cohort during the same period (rows) and different periods (columns), both among different cohorts (row comparison) and within each cohort itself (column comparison). <br>
![image](https://github.com/user-attachments/assets/a1ae0520-d042-4120-92dc-5e20970a493c)
<br>**The heatmap shows us:**
- Almost all cohorts from 2015 and 2016 struggled to retain customers in the first quarter of each year, with an average retention rate of less than 30%.
- Almost all cohorts from 2015 and 2016 achieved their highest customer retention rate in the last quarter of each year, averaging above 30%.

![image](https://github.com/user-attachments/assets/fe1e627a-d81f-4230-98f5-e974ce7ddf17)
<br>**The heatmap shows us:**
- Almost all cohorts from 2015 and 2016 struggled to retain customers in the first quarter of each year, with an average retention rate of less than 30%.
- Almost all cohorts from 2015 and 2016 achieved their highest customer retention rate in the last quarter of each year, averaging above 30%.
---
### Sales Analysis for each Cohort
![image](https://github.com/user-attachments/assets/7b3b1a79-abbd-45e1-aa2b-e5caa0d67c7f)
**The line chart shows that:**
- All cohorts from 2015 had an average quarterly sales contribution three times higher than those from other years
- Almost all cohorts lost over 50% of their sales retention by the second quarter of their existence.
<br>

![image](https://github.com/user-attachments/assets/17c80eef-9014-49f8-bf83-ac185b3898da)
![image](https://github.com/user-attachments/assets/8854a09e-cba1-4388-b351-d37668b9c5e3)

<br>**The heatmap shows us:**
- Just like customer retention, all cohorts struggled to maintain sales in the first quarter of each year.
- Across almost all cohorts, the fourth quarter of each year is the peak period for sales.

## 6. Conclusions
- In the retention rate heatmap, it's evident that most cohort-date groups exhibit varied retention rates ranging from 11.11% to 77.78%. Notably, the cohorts from the first year (2015) stand out, managing to retain customers above the 50% mark by the end of the date (2018Q4).
- According to the cumulative sales line plot, it becomes apparent that cohorts from the first year have made the most significant contribution to sales. This is, of course, due to the fact that each cohort consists of more than 100 members, making them stand out from the rest. Among these cohorts, the one from 2015Q2 emerges as the leader in sales performance.
- From the heatmap, we are able to catch the pattern among cohorts. All cohorts have similar behavior along the specific date. In every Quarter-1, all cohorts make the lower retention and gain back their best retention in Quarter-4.

## 7. Recommendation
- Analyze First-Year Cohorts. Further analyze the behavior of cohorts from the first year (2015) that exhibit a significantly larger number of members. Identify the specific factors or strategies that contribute to their success. Apply successful tactics from these cohorts to other groups with lower retention rates.
- Customer Engagement in Quarter-1. Pay special attention to customer engagement and satisfaction during Quarter-1. Conduct customer surveys, analyze feedback, and identify pain points to enhance the customer experience, particularly in the first quarter of each year.
- Optimize Sales Strategies. Optimize sales strategies for cohorts with more than 100 members. Larger cohorts naturally contribute significantly to sales. Focus on enhancing customer engagement and satisfaction within these cohorts to maximize their potential.

