import requests
import pandas as pd
import plotly.express as px

# Make API request
url = 'https://api.census.gov/data/2019/pep/population'
params = {'get': 'POP,NAME', 'for': 'state:*'}
response = requests.get(url, params=params)

# Convert response to pandas dataframe
df = pd.DataFrame(response.json()[1:], columns=response.json()[0])

# Clean and manipulate data
df['POP'] = pd.to_numeric(df['POP'])
df['NAME'] = df['NAME'].str.replace('United States - ', '')
df = df.sort_values('POP', ascending=True)


# Create dashboard
fig = px.bar(df, x='NAME', y='POP', color='NAME')
fig.update_layout(title='Population by State')
fig.show()
