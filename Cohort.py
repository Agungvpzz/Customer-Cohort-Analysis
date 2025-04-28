class Cohort:
    def __init__(self, df, col_date, col_order_id, col_customer_id):
        self.df = df        
        self.col_date = col_date        
        self.col_order_id = col_order_id
        self.col_customer_id = col_customer_id
    
    def get_cohort_frame(self, cohort_period, date_period, use_age_period=False):    
        cohort_frame = self.df.copy()
    
        # First date for each unique ID
        cust_date_grouped = cohort_frame.groupby(self.col_customer_id)[self.col_date]
        cohort_frame['Initial Date'] = cust_date_grouped.transform("min")
        cohort_frame['Latest Date'] = cust_date_grouped.transform("max")        
        
        # Get age (recency) for each unique ID
        latest_date = cohort_frame[self.col_date].max()
        cohort_frame['Recency'] = (latest_date-cohort_frame['Latest Date']).dt.days
    
        # Create Date Period and Cohort Period columns
        name_cohort = f'Cohort ({cohort_period})'
        name_period = f'Period ({date_period})'        
        cohort_frame[name_cohort] = cohort_frame['Initial Date'].dt.to_period(cohort_period)
        cohort_frame[name_period] = cohort_frame[self.col_date].dt.to_period(date_period)
        
        # # Age for each unique ID (not really useful)
        # df['ID Age'] = (
        #     df['Period'].astype(int) - 
        #     df['Initial Date'].dt.to_period(date_period).astype(int)
        # )
    
        # Age for each unique Cohort (optional)
        if use_age_period:
            name_cohort_age = f'Cohort Age ({date_period})'
            cohort_frame[name_cohort_age] = (
                cohort_frame[name_period].astype(int) - 
                cohort_frame.groupby(name_cohort)[name_period].transform('min').astype(int)
            )
    
        return cohort_frame    

        
    def get_cohort_summary(self, cohort_frame, col_cohort, col_value):
        ## Grouped by Customers
        cust = cohort_frame.groupby(self.col_customer_id, as_index=False).agg(
            Cohort = (col_cohort, 'first'),
            Total_Value = (col_value, 'sum'),
            Total_Order = (self.col_order_id, 'nunique'),
            Recency = ('Recency', 'first')
        )
    
        ## Grouped by Cohort
        cohort = cust.groupby('Cohort').agg(
            Size = ("Customer ID", "count"),
            Active_in_30_Days = ('Recency', lambda x: sum(x.map(lambda y: True if y <= 30 else False))),
            Total_Value = ('Total_Value', 'sum'),
            Avg_Sales = ('Total_Value', 'mean'),    
            Skew_Sales = ('Total_Value', 'skew'),
            Total_Order = ('Total_Order', 'sum'),
            Avg_Recency = ('Recency', 'mean')    
        )        
        
        total_size = cohort['Size'].sum()
        total_sales = cohort['Total_Value'].sum()
        total_order = cohort['Total_Order'].sum()
        
        cohort['% Size'] = (cohort['Size'] / total_size) * 100
        cohort['% Value'] =  (cohort['Total_Value'] / total_sales) * 100
        cohort['% Order'] = (cohort['Total_Order'] / total_order) * 100
        cohort['% Active in 30 Days'] = (cohort['Active_in_30_Days'] / cohort['Size']) * 100

        cohort.columns = cohort.columns.str.replace("_", " ")
        cohort.columns = cohort.columns.str.replace("Value", col_value.title())
        
        cohort.index.name = col_cohort
        cohort.columns.name = f"{col_value.title()} Summary"
    
        return cohort

        
    def get_cohort_table(self, cohort_frame, col_cohort, col_period, col_value, aggfunc='sum', ratio=True, margin_x=None, margin_y=None):
        """
        date_period: Either 'Period' or 'Cohort Age' column
        margin_x, margin_y = 'mean', 'sum', 'max', 'min', 'medium', 'std', 'var'            
        """            
        
        cohort_table = cohort_frame.groupby([col_cohort, col_period])[col_value].agg(aggfunc)        
        cohort_table = cohort_table.unstack()
        
        cohort_table.index.name = col_cohort
        cohort_table.columns.name = col_period
        
        if ratio:
            cohort_size = cohort_table.T.apply(lambda col: col.dropna().iloc[0])
            cohort_table = cohort_table.divide(cohort_size, axis=0)
    
        if margin_y is not None:
            cohort_table[margin_y] = cohort_table.apply(lambda col: col.dropna().iloc[1:], axis=1).agg(margin_y, axis=1)
            # cohort_table[margin_y] = cohort_table.agg(margin_y, axis=1)
        if margin_x is not None:
            cohort_table.loc[margin_x] = cohort_table.apply(lambda col: col.dropna().iloc[1:-1], axis=1).agg(margin_x, axis=0)
            # cohort_table.loc[margin_x] = cohort_table.agg(margin_x, axis=0)
            
        return cohort_table

    def get_top_contributors(self, cohort_frame, col_cohort, col_value, aggfunc='sum', top_pct=0.2, include_ids=False):
        """
        Return a top contributors from each cohort (not directly from all customers)
        """
        
        df_cust = cohort_frame.groupby(self.col_customer_id).agg({
            col_cohort: 'first', col_value: aggfunc
        })
        df_top = df_cust.groupby([col_cohort]).agg(
            top_size = (col_value, lambda x: int(top_pct*x.size)),
            total_size = (col_value, lambda x: x.size),
            top_value = (col_value, lambda x: sum(x.nlargest(int(top_pct*x.size)))),
            total_value = (col_value, aggfunc)
        )
        df_top = df_top.assign(
            top_size_pct=lambda x: x['top_size']/x['total_size'],
            top_value_pct=lambda x: x['top_value']/x['total_value']
        )

        # Add unique ID column
        if include_ids:
            n_size = df_cust.shape[0]
    
            # Sort values by nlargest method
            df_cust = df_cust.groupby(col_cohort)[col_value].nlargest(n_size).reset_index()
            unique_ids = df_cust.groupby(col_cohort)[self.col_customer_id].unique()
            
            df_top = df_top.merge(unique_ids, left_index=True, right_index=True)

            # Get only the top size
            for idx, val in df_top.iterrows():
                df_top.at[idx, self.col_customer_id] = val[self.col_customer_id][:val['top_size']]

        df_top = df_top.rename({self.col_customer_id:'top_contributors'}, axis=1)

        df_top.columns.name = f'Top {top_pct*100}%'
        
        return df_top

    def get_lost_contributors(self, cohort_frame, col_cohort, col_value, aggfunc='sum', days=90):   
        """
        days: inactive more than n days
        """
        df_cust = cohort_frame.groupby(self.col_customer_id, as_index=False).agg({
            'Recency': 'first', 
            col_cohort: 'first',
            col_value: aggfunc
        })

        # aggregate all data
        df_base = df_cust.groupby(col_cohort).agg(
            total_value = (col_value, aggfunc), 
            total_size = (self.col_customer_id, 'size')
        )

        # aggregate the filtered data (lost customers)
        df_lost = df_cust.query(f'Recency > {days}')
        df_lost = df_lost.groupby(col_cohort).agg(
            lost_size = (self.col_customer_id, 'size'),
            lost_contributors = (self.col_customer_id, 'unique'),
            lost_value = (col_value, aggfunc)
        )

        df_lost = df_base.merge(df_lost, left_index=True, right_index=True)
        df_lost['lost_size_pct'] = df_lost['lost_size']/df_lost['total_size']
        df_lost['lost_value_pct'] = df_lost['lost_value']/df_lost['total_value']
        
        ordered_cols = ['lost_size', 'total_size', 'lost_value', 
                        'total_value', 'lost_size_pct', 'lost_value_pct', 
                        'lost_contributors']

        df_lost.columns.name = f'Lost > {days} days'

        return df_lost[ordered_cols]