import streamlit as st
from st_deta_connection import DetaBaseConnection

# Instantiate DetaBaseConnection
deta_connection = DetaBaseConnection(project_key='your_deta_project_key')

# Use secrets.toml to store your Deta project key 

#Insert data into Deta Base collection
deta_connection.insert(collection_name='your_collection_name', data={'field': 'value'})

# Fetch data from Deta Base collection
data = deta_connection.fetch(collection_name='your_collection_name', query={'field': 'value'})

# Display the fetched data using Streamlit
st.dataframe(data)
