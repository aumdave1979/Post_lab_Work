import pandas as pd
import plotly.express as px

# Creating a Sample Dataset
data = {
    'Product': ['A', 'B', 'C', 'D', 'E'],
    'Sales': [100, 200, 150, 300, 250],
    'Profit': [30, 70, 50, 120, 90]
}

df = pd.DataFrame(data)
fig = px.bar(
    df,
    x='Product',
    y='Sales',
    title='Sales by Product',
    color='Profit',   # Color bars based on Profit value
    text='Sales'      # Display Sales value on each bar
)
fig.update_layout(
    xaxis_title='Product',
    yaxis_title='Sales',
    legend_title='Profit',
    template='plotly_dark'  # Dark theme
)
fig.write_html('sales_by_product.html')
fig.write_image('sales_by_product.png')
fig.show()


