import plotly.express as px


def stacked_bar(
    df,
    col_value,
    col_color='Cohort',
    orientation='v',
    barnorm=None,
    title='',
    reverse_traceorder=True,
    **layout
):
    df = df.copy()
    df['Value'] = 'Cohorts'
    
    fig = px.histogram(
        df,
        x='Value' if orientation == 'v' else col_value,
        y=col_value if orientation == 'v' else 'Value',
        color=col_color,
        template='plotly_white',
        text_auto=True,
        barnorm=barnorm
    )
    
    fig = fig.update_layout(
        legend_traceorder="reversed" if reverse_traceorder else None,
        title=title,
        title_x=0.5,
        xaxis_title=None if orientation == 'v' else col_value,
        yaxis_title=col_value if orientation == 'v' else None
    )
    
    if barnorm == 'percent':
        fig = fig.update_traces(texttemplate='%{value:.2}%')
    
    return fig.update_layout(**layout)
