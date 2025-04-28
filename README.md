> If you encounter an error with the Jupyter Notebook on GitHub, please use this link [nbviewer](https://nbviewer.org/github/Agungvpzz/Customer-Cohort-Analysis/blob/superstore/Cohort%20Analysis%20SuperStore.ipynb)

# Customer Cohort Analysis

## 1. Introduction
This report presents an in-depth analysis of customer cohorts. The analysis centers around understanding customer purchasing behavior, retention, and revenue patterns across different cohorts. Key findings shed light on customer trends, highlight high-performing cohorts, and provide actionable insights to enhance sales and customer satisfaction.

## 2. Business Understanding
A. Business Goals
Customer cohort analysis enables businesses to segment customers based on shared behaviors and analyze these groups over time, aiming to improve retention by identifying churn patterns and enhancing customer experiences.

B. Objective of this analysis
Examine customer purchasing habits over time, focusing on frequency and value, to inform targeted strategies.

C. Key Questions to Answer
1. What are the retention rates for each customer group and how do they change over time?
2. Which groups show the highest revenue growth?
3. Are there common trends that help predict future behavior in these groups?

## 3. Data Collection
The dataset can be accessed at the following link: https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting

## 4. Methodology
- Cohort Definition: Cohorts are defined based on the quarter of the customer's first purchase.
- Metrics: The analysis includes customer retention rates, cohort composition, and revenue growth over time.
- Data Period: Data analyzed spans 4 years from January 2015 to December 2018.

## 5. Results and Analysis
### Cohort Member Composition
![image](https://github.com/user-attachments/assets/e73dac3b-9c8a-4699-a517-020941f30e8a)
<br>As you can see, the cohorts from Q2, Q3, and Q4 of 2015 have the highest number of members, at approximately 20%.

### Cohort Sales Composition
![image](https://github.com/user-attachments/assets/77fc9776-60a1-4cd0-8963-6d3d114e7a00)
<br>All cohorts from the first year, 2015, contribute around 17–21% of total sales, accumulating to approximately 80% of the total sales.

### Customer Retention in each Cohort
With line charts displaying the cohorts in 2015 and 2016, we can clearly identify which cohorts are valuable for the business and observe common patterns across cohorts. <br>
![image](https://github.com/user-attachments/assets/3680760d-d02a-4977-8626-d0daaa48bb21)

**The line chart shows that:**
- All the first-year cohorts from 2015 maintain varying customer retention ratios between 20% and 50%, with a mean of only 30–33%.
- All 2015 and 2016 cohorts lose over 50% of their customer retention during the first quarter of their existence.
<br>

The heatmap will help us identify patterns across cohorts by comparing the condition of each cohort during the same period (rows) and different periods (columns), both among different cohorts (row comparison) and within each cohort itself (column comparison). <br>
![image](https://github.com/user-attachments/assets/827a2719-c766-42f7-a9de-26f55d878b15)

**The heatmap shows us:**
- That 9 cohorts had their lowest retention in February 2011, followed by January 2011 with 8 cohorts.
- That 10 cohorts reached their highest customer retention in November 2010, followed by October 2010 with 9 cohorts.

### Sales Retention in each Cohort

![image](https://github.com/Agungvpzz/Customer-Cohort-Analysis/assets/48642326/16ac3eac-d133-4944-92bd-124990342027)
**The line chart shows that:**
- The first cohort, December 2009, has the highest sales compared to other cohorts.
- Almost all cohorts lose over 50% of their sales retention by the second month and tend to stabilize below 50% afterward (except cohort December 2009).
<br>

![image](https://github.com/user-attachments/assets/d3359c4d-0ee2-426a-b176-5eac12ad0548)
**The heatmap shows us:**
- 9 cohorts experienced their lowest retention in February 2011, followed by April 2011 with 5 cohorts.
- November 2010 had the highest retention for 9 cohorts, followed by October 2010 with 7 cohorts.

### Inactive Customers Over 6 Months in Each Cohort
![image](https://github.com/Agungvpzz/Customer-Cohort-Analysis/assets/48642326/4ed29afa-e581-481a-8e8f-ff6dff09bb31)
**The bar plot shows us:**
- Overall, 50% of customers have been inactive in the last 6 months.
- The inactive customers contributed around 12% of total sales.
- The first cohort, December 2009, has the lowest number of inactive customers at 34%.

## 7. Insights
- In the retention rate heatmap, it's evident that most cohort-date groups exhibit varied retention rates ranging from 11.11% to 77.78%. Notably, the cohorts from the first year (2015) stand out, managing to retain customers above the 50% mark by the end of the date (2018Q4).
- According to the cumulative sales line plot, it becomes apparent that cohorts from the first year have made the most significant contribution to sales. This is, of course, due to the fact that each cohort consists of more than 100 members, making them stand out from the rest. Among these cohorts, the one from 2015Q2 emerges as the leader in sales performance.
- From the heatmap, we are able to catch the pattern among cohorts. All cohorts have similar behavior along the specific date. In every Quarter-1, all cohorts make the lower retention and gain back their best retention in Quarter-4.

## 8. Recommendation
- Analyze First-Year Cohorts. Further analyze the behavior of cohorts from the first year (2015) that exhibit a significantly larger number of members. Identify the specific factors or strategies that contribute to their success. Apply successful tactics from these cohorts to other groups with lower retention rates.
- Customer Engagement in Quarter-1. Pay special attention to customer engagement and satisfaction during Quarter-1. Conduct customer surveys, analyze feedback, and identify pain points to enhance the customer experience, particularly in the first quarter of each year.
- Optimize Sales Strategies. Optimize sales strategies for cohorts with more than 100 members. Larger cohorts naturally contribute significantly to sales. Focus on enhancing customer engagement and satisfaction within these cohorts to maximize their potential.

