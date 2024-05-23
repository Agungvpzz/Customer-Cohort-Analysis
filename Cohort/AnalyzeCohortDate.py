import pandas as pd
from collections import Counter

from .CohortDate import CohortDate


class AnalyzeCohortDate(CohortDate):
    def get_active_customers(self, period_date='M', latest_active_period=0):
        """
        return dict[Counter]                
        """
        df = self.get_table(
            self.col_customer_id, period_date, 'unique', ratio=False
        )
        
        active_customers = dict()
        
        for cohort in df.index:
            active_customers.update({cohort: Counter()})
            for _, val in df.loc[
                cohort,
                df.columns != cohort].dropna()[-latest_active_period:].items():
                if not isinstance(
                    val, float
                ):  # np.nan is detected as float type
                    active_customers[cohort].update(val)
        
        return active_customers
    
    def get_inactive_customers(
        self,
        col_value,
        period_date='M',
        latest_active_period=0,
        drop_younger_period=True,
        show_contributions=False
    ):
        
        df = self.get_table(
            self.col_customer_id, period_date, 'unique', ratio=False
        )
        
        active_customers = self.get_active_customers(
            period_date, latest_active_period
        )
        
        reports = dict()
        for cohort, values in active_customers.items():
            base = df.loc[cohort, cohort]
            active = active_customers[cohort].keys()
            inactive = set(base).difference(active)
            
            reports[cohort] = {
                'initial': len(base),
                'inactive_n': len(inactive),
                'inactive_pctg': len(inactive) / len(base),
                'inactive': inactive,
            }
        
        df_report = pd.DataFrame(reports).T
        df_report.index.name = 'Cohort'
        period_dates = {
            'M': 'Months',
            'Q': 'Quarters',
            'Y': 'Years',
            'W': 'Weeks',
            'D': 'Days'
        }
        period_name = period_dates[period_date]
        period_name = period_name[:-1
                                 ] if latest_active_period == 1 else period_name
        df_report.columns.name = f'Last {latest_active_period} {period_name}'
        
        if drop_younger_period:
            df_report = df_report.iloc[:-latest_active_period, :]
        
        if show_contributions:
            df = self.df
            df_report['sum_sales'] = 0.0
            for idx, val in df_report.iterrows():
                val['inactive']
                mask = df[self.col_customer_id].isin(val['inactive'])
                df_report.loc[idx, 'sum_sales'] = df.loc[mask, col_value].sum()
        
        return df_report
