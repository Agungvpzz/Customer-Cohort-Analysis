from .Cohort import Cohort


class CohortDate(Cohort):
    def get_table(
        self,
        col_value,
        period_date='M',
        aggfunc='sum',
        margin_row=None,
        margin_col=None,
        ratio=True
    ):
        df = self.get_cohort_agg(col_value, period_date, aggfunc)
        
        df_pivot = df.pivot_table(
            index='Cohort', columns='Period Date', aggfunc={col_value: 'first'}
        )
        df_pivot = df_pivot.droplevel(0, axis=1)
        
        df_pivot.index.name = f"Cohort ({period_date})"
        df_pivot.columns.name = f"Period ({period_date})"
        
        if ratio:
            cohort_size = [
                df_pivot.iloc[i, i] for i in range(df_pivot.shape[0])
            ]
            df_pivot = df_pivot.divide(cohort_size, axis=0)
        
        if margin_col is not None:
            df_pivot[margin_col] = df_pivot.agg(margin_col, axis=1)
        if margin_row is not None:
            df_pivot.loc[margin_row] = df_pivot.agg(margin_row, axis=0)
        
        return df_pivot
    
    def get_pivot(
        self,
        col_value,
        period_date='M',
        period_date_step='M',
        aggfunc='sum',
        margin_row=None,
        margin_col=None,
        ratio=True
    ):
        df = self.get_cohort_features(period_date, period_date_step)
        
        df_pivot = df.pivot_table(
            index='Cohort',
            columns='Period Date Step',
            aggfunc={col_value: aggfunc}
        )
        df_pivot = df_pivot.droplevel(0, axis=1)
        
        df_pivot.index.name = f'Cohort ({period_date})'
        df_pivot.columns.name = f'Period ({period_date_step})'
        
        if ratio:
            cohort_size = [
                df_pivot.iloc[i, :].dropna().iloc[0]
                for i in range(df_pivot.shape[0])
            ]
            df_pivot = df_pivot.divide(cohort_size, axis=0)
        
        if margin_col is not None:
            df_pivot[margin_col] = df_pivot.agg(margin_col, axis=1)
        if margin_row is not None:
            df_pivot.loc[margin_row] = df_pivot.agg(margin_row, axis=0)
        
        return df_pivot
