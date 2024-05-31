class Cohort:
    def __init__(self, df, col_customer_id, col_order_date, col_order_id):
        self.df = df
        self.col_customer_id = col_customer_id
        self.col_order_date = col_order_date
        self.col_order_id = col_order_id
    
    def get_cohort_agg(
        self, col_value=None, period_date='M', aggfunc=None, aggs=None
    ):
        """
        Do aggregation based on cohort

        Parameters:
        - col_value (str): The column to aggregate.
        - period_date (str): The period for grouping dates (default is 'M' for monthly).
        - aggfunc (str): The aggregation function to apply (default is None).
        = aggs (dict): Do more than one aggregation

        Returns:
        - DataFrame: A dataframe
        """
        
        df = self.df.copy()
        
        df['Period Date'] = df[self.col_order_date].dt.to_period(period_date)
        df['Cohort'] = df.groupby(
            self.col_customer_id
        )[self.col_order_date].transform('min').dt.to_period(period_date)
        
        df_cohort_data = df.groupby(['Cohort', 'Period Date'], as_index=False)
        
        if aggs:
            df_cohort_data = df_cohort_data.agg(aggs)
        else:
            df_cohort_data = df_cohort_data.agg({col_value: aggfunc})
        
        return df_cohort_data
    
    def get_cohort_features(self, period_date='M', period_date_step=None):
        """
        Adds cohort features to the dataframe.

        Parameters:
        - period_date (str): The period for cohort grouping (default is 'M' for monthly).
        - period_date_step (str): The period to extract from the transaction date (optional).

        Returns:
        - DataFrame: A copy of the original dataframe with added cohort features.
        """
        
        df = self.df.copy()
        
        # Get member cohort data based on the specified period date
        df_cohort_data = self.get_cohort_agg(
            self.col_customer_id, period_date, 'unique'
        )
        df_cohort_data = df_cohort_data.sort_values(['Cohort', 'Period Date'])
        df_cohort_members = df_cohort_data.groupby('Cohort').agg(
            {self.col_customer_id: 'first'}
        )
        
        # Create a mapping from customer ID to cohort
        maps_cohort = dict()
        for cohort in df_cohort_members.index:
            for member in df_cohort_members.loc[cohort, self.col_customer_id]:
                maps_cohort[member] = cohort
        
        # Add cohort information to the dataframe
        df['Cohort'] = df[self.col_customer_id].map(maps_cohort)
        
        # Optionally add period date step information
        if period_date_step:
            df['Period Date Step'] = df[self.col_order_date
                                       ].dt.to_period(period_date_step)
        
        return df
    
    def get_cohort_summary(self, col_value, period_date='M'):
        df = self.df.copy()
        
        name_period = f"Date Period ({period_date})"
        name_age_cohort = "age"
        
        cohort_map = df.groupby(self.col_customer_id)[self.col_order_date].min()
        cohort_map = cohort_map.dt.to_period(period_date)
        df['Cohort'] = df[self.col_customer_id].map(cohort_map.to_dict())
        df[name_period] = df[self.col_order_date].dt.to_period(period_date)
        
        # Aggregating customer data
        df_agg_cust = df.groupby(
            ['Cohort', self.col_customer_id], as_index=False
        )
        df_agg_cust = df_agg_cust.agg(
            sum_cust_value=(col_value, 'sum'),
            num_transactions=(self.col_order_id, 'nunique'),
            cohort_members=(self.col_customer_id, 'first')
        )
        
        # Grouping by cohort date and calculating summary metrics
        df_agg_cust = df_agg_cust.groupby('Cohort').agg(
            mean_cust_value=('sum_cust_value', 'mean'),
            skew_cust_value=('sum_cust_value', 'skew'),
            total_transactions=('num_transactions', 'sum'),
            mean_cust_transactions=('num_transactions', 'mean'),
            size=(self.col_customer_id, 'count'),
            members=('cohort_members', 'unique')
        )
        
        # Date Aggregating
        df_agg_date = df.groupby(['Cohort', name_period], as_index=False)
        df_agg_date = df_agg_date.agg(
            sum_date_value=(col_value, 'sum'),
            num_transactions=(self.col_order_id, 'nunique')
        )
        
        # Grouping by cohort date and calculating date summary metrics
        df_agg_date = df_agg_date.groupby('Cohort').agg(
            mean_date_transactions=('num_transactions', 'mean'),
            mean_date_value=('sum_date_value', 'mean'),
            skew_date_value=('sum_date_value', 'skew'),
            total_value=('sum_date_value', 'sum'),
            age_cohort=(name_period, 'size')
        )
        df_agg_date = df_agg_date.rename(
            {'age_cohort': name_age_cohort}, axis=1
        )
        
        # Merging customer and date aggregations
        df_summary = df_agg_cust.merge(df_agg_date, on='Cohort')
        df_summary.columns = df_summary.columns.map(
            lambda x: x.replace('value', col_value.lower())
        )
        COLS = list(
            map(
                lambda x: x.replace('value', col_value.lower()), [
                    name_age_cohort, 'size', 'members', 'total_transactions',
                    'mean_cust_transactions', 'mean_date_transactions',
                    'total_value', 'mean_cust_value', 'skew_cust_value',
                    'mean_date_value', 'skew_date_value'
                ]
            )
        )
        
        return df_summary[COLS]
    
    def get_top_contributors(
        self,
        col_value,
        period_date='M',
        aggfunc_cust='sum',
        aggfunc_cohort='sum',
        top_n=5,
        percentage=False
    ):
        df = self.get_cohort_features(period_date)
        df_group_cohort_cust = df.groupby(
            ['Cohort', self.col_customer_id], as_index=False
        )
        
        # Aggregate for each cohort and customer
        df_agg_cohort_cust = df_group_cohort_cust.agg(
            value=(col_value, aggfunc_cust),
            n_transactions=(self.col_order_id, 'nunique'),
            customers=(self.col_customer_id, 'first')
        )
        col_name_value = f"{col_value} ({aggfunc_cust})"
        df_agg_cohort_cust = df_agg_cohort_cust.rename(
            {'value': col_name_value}, axis=1
        )
        df_agg_cohort_cust = df_agg_cohort_cust.sort_values(
            ['Cohort', col_name_value], ascending=False
        )
        
        # Aggregate for each cohort
        df_group_cohort = df_agg_cohort_cust.groupby('Cohort')
        df_agg_cohort = df_group_cohort.agg(
            cohort_value=(col_name_value, aggfunc_cohort),
            n_transactions=('n_transactions', 'sum'),
            n_customers=('customers', 'nunique')
        )
        col_name_value_cohort = f"{col_name_value} ({aggfunc_cohort})"
        df_agg_cohort = df_agg_cohort.rename(
            {'cohort_value': col_name_value_cohort}, axis=1
        )
        
        if percentage:
            top_n_formula = lambda x: x.head(
                int(round(top_n * (x.shape[0] / 100)))
            )
            df_group_cohort_top_n = df_group_cohort.apply(top_n_formula)
            df_group_cohort_top_n = df_group_cohort_top_n.reset_index(
                drop=True
            ).groupby('Cohort')
            col_name = f"top_{top_n}%"
        else:
            df_group_cohort_top_n = df_group_cohort.head(top_n
                                                        ).groupby('Cohort')
            col_name = f"top_{top_n}"
        
        df_agg_cohort_top_n = df_group_cohort_top_n.agg(
            sum_value=(col_name_value, 'sum'),
            n_transactions=('n_transactions', 'sum'),
            n_customers=('customers', 'nunique'),
            customers=('customers', 'unique')
        )
        
        df_agg_cohort_top_n['pctg_sum_value'] = (
            df_agg_cohort_top_n['sum_value'] /
            df_agg_cohort[col_name_value_cohort]
        ) * 100
        df_agg_cohort_top_n['pctg_transactions'] = (
            df_agg_cohort_top_n['n_transactions'] /
            df_agg_cohort['n_transactions']
        ) * 100
        df_agg_cohort_top_n['pctg_customers'] = (
            df_agg_cohort_top_n['n_customers'] / df_agg_cohort['n_customers']
        ) * 100
        
        df_agg_cohort_top_n = df_agg_cohort_top_n.rename(
            {
                'sum_value': f'sum_value_{col_name}',
                'n_transactions': f'n_transactions_{col_name}',
                'n_customers': f'n_customers_{col_name}',
                'customers': f'customers_{col_name}'
            },
            axis=1
        )
        
        return df_agg_cohort.merge(
            df_agg_cohort_top_n, left_index=True, right_index=True
        )
