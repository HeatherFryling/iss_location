# Heather Fryling
# 2/15/2021
# Practice project from Python Programmer for getting familiar with
# pandas, Plotly, and APIs.

import pandas as pd
import plotly.express as px

# url for the ISS location
url = 'http://api.open-notify.org/iss-now.json'
# Use Pandas to create a data frame from the json.
data_frame = pd.read_json(url)
# Pull latitude and longitude out of iss_position and give them their
# own dictionary entries in the data frame.
data_frame['latitude'] = data_frame.loc['latitude', 'iss_position']
data_frame['longitude'] = data_frame.loc['longitude', 'iss_position']
# Remove the unneccessary message data.
data_frame = data_frame.drop(['message'], axis = 1)
# Plot and display the location using Plotly.
fig = px.scatter_geo(data_frame, lat = 'latitude', lon = 'longitude')
fig.show()