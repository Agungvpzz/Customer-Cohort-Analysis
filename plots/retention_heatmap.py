import plotly.express as px


def retention_heatmap(
    cohort_period_table,
    name_value='value',
    colorbar_title='Retention %',
    **layouts
):
    fig = px.imshow(
        cohort_period_table * 100,
        labels={'color': name_value},
        color_continuous_scale='viridis',
        text_auto=True,
        zmin=0,
        zmax=100
    )
    
    fig.update_layout(template='plotly_white')
    fig.update_layout(**layouts)
    fig.update_xaxes(side="top")
    fig.update_coloraxes(showscale=True, colorbar_title='Retention %')
    
    fig._data[0]['text'] = fig._data[0]['z'].round(2)
    fig._data[0]['texttemplate'] = "%{text}%"
    fig._data[0]['xgap'] = 1
    fig._data[0]['ygap'] = 1
    fig._data[0]['hoverongaps'] = False
    
    return fig
