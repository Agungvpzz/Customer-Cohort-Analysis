# Customer Cohort Analysis

## 1. Introduction
This report presents an in-depth analysis of customer cohorts. The analysis centers around understanding customer purchasing behavior, retention, and revenue patterns across different cohorts. Key findings shed light on customer trends, highlight high-performing cohorts, and provide actionable insights to enhance sales and customer satisfaction.

## 2. Data Understanding
The dataset can be accessed at the following link: https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci/

The Online Retail II dataset provides detailed insights into the sales activities of an online store from December 1, 2009, to December 9, 2011. This dataset is available on Kaggle. The company specializes in unique giftware suitable for a variety of occasions. A substantial portion of the customer base consists of wholesalers. 

## 3. Business Goals
Customer cohort analysis enables businesses to segment customers based on shared behaviors and analyze these groups over time, aiming to improve retention by identifying churn patterns and enhancing customer experiences.

## 4. Objectives
1. **Pattern Cohort Behaviour Discovery**: Identify and analyze behavioral patterns of different cohorts over time to understand their purchasing habits, frequency, and value.
2. **Enhancing Retention Rates**: Determine which cohorts exhibit lower retention rates and develop targeted strategies to improve retention for these specific groups.
3. **Discover Seasonal Effect**: Identify key periods during the year when customer sales typically decline or stagnate, indicating a potential need for promotional activities.

## 5. Methodology
- We divided our customer cohort based on the month the customers purchased
- We selected only cohorts aged over 12 months.
- We used Python and utilized Python packages, such as Pandas for data analysis and Plotly for data visualization.
- Since December 2011 is not fully recorded in the data, we removed all records from that date

## 6. Hypothesis
- Customers who make frequent purchases in the first few months are more likely to become repeat customers.
- Customers with higher initial purchase amounts tend to have higher retention rates.

## 7. Results and Analysis
### Cohort Member Composition
![image](https://github.com/Agungvpzz/Customer-Cohort-Analysis/assets/48642326/08c59e6c-4f8c-4bd6-bc37-0b772cfc75ad)
<br>As you can see, the first cohort (Dec 2009) has the highest number of members, consistently having twice as many as the other cohorts

### Cohort Sales Composition
![image](https://github.com/Agungvpzz/Customer-Cohort-Analysis/assets/48642326/08312fc4-5c8c-4148-92a0-a119898f312e)
<br>The first cohort (Dec 2009) contributes around 55% of total sales, while the other cohorts each contribute less than 10%

### Customer Retention in each Cohort
With a line chart displaying the first 12 months of each cohort's journey, we can clearly identify which cohorts are valuable for the business and observe common patterns across cohorts. <br>
![image](https://github.com/Agungvpzz/Customer-Cohort-Analysis/assets/48642326/8cb06b45-3fe5-4234-b806-ac7fba581de5)
**The line chart shows that:**
- The first cohort, December 2009, is the most valuable for the business due to its large number of members.
- All cohorts lose over 50% of their customer retention after the first month.
<br>

The heatmap will help us identify patterns across cohorts by comparing the condition of each cohort during the same period (rows) and different periods (columns), both among different cohorts (row comparison) and within each cohort itself (column comparison). <br>
![customer retention](https://github.com/Agungvpzz/Customer-Cohort-Analysis/assets/48642326/ab227baf-133d-4052-a4af-21f23febd893)
**The heatmap shows us:**
- That 9 cohorts had their lowest retention in February 2011, followed by January 2011 with 8 cohorts.
- That 10 cohorts reached their highest customer retention in November 2010, followed by October 2010 with 9 cohorts.

### Sales Retention in each Cohort

![image](https://github.com/Agungvpzz/Customer-Cohort-Analysis/assets/48642326/16ac3eac-d133-4944-92bd-124990342027)
**The line chart shows that:**
- The first cohort, December 2009, has the highest sales compared to other cohorts.
- Almost all cohorts lose over 50% of their sales retention by the second month and tend to stabilize below 50% afterward (except cohort December 2009).
<br>

![sales retention](https://github.com/Agungvpzz/Customer-Cohort-Analysis/assets/48642326/cd91d17b-85e7-4f44-b313-7928b3ca0848)
**The heatmap shows us:**
- 9 cohorts experienced their lowest retention in February 2011, followed by April 2011 with 5 cohorts.
- November 2010 had the highest retention for 9 cohorts, followed by October 2010 with 7 cohorts.

### Inactive Customers Over 6 Months in Each Cohort
![image](https://github.com/Agungvpzz/Customer-Cohort-Analysis/assets/48642326/4ed29afa-e581-481a-8e8f-ff6dff09bb31)
**The bar plot shows us:**
- Overall, 50% of customers have been inactive in the last 6 months.
- The inactive customers contributed around 12% of total sales.
- The first cohort, December 2009, has the lowest number of inactive customers at 34%.

## 8. Conclusion
- The first cohort, December 2009, has made the most significant contribution to sales by over 50% of total sales. This is primarily because it has the largest number of members among all cohorts, making it stand out from the rest.
- Almost all cohorts lose over 50% of their performance, both in sales and customer retention, by the second month from their establishment.
- October and November are the most active months for each cohort. Meanwhile, January, February, and April are the months where cohort performance declines.
- During the last 6 months, over 50% of customers have been inactive, where they have contributed 12% to total sales.

## 9. Recommendation
1. Customer Engagement in Quarter 1. Pay special attention to customer engagement and satisfaction during Quarter 1. Conduct customer surveys, analyze feedback, and identify pain points to enhance the customer experience, particularly in the first quarter of each year.
2. Optimize Sales Strategies. Optimize sales strategies for cohorts with more than 100 members. Larger cohorts naturally contribute significantly to sales. Focus on enhancing customer engagement and satisfaction within these cohorts to maximize their potential.

