import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
from dbConnection import run_query

# Load CSV files
distribution_file = 'dataset/Distribution_of_franchizes.csv'

# Read CSV files into DataFrames
df_distribution = pd.read_csv(distribution_file)

# Streamlit setup
st.set_page_config(page_title='Yelp Data Analysis')
st.header('Yelp Data Analysis Dashboard')

# Display dataframes or use other visualization components as needed
st.subheader('Distribution of Franchises')
st.write(df_distribution)

# Plot pie chart for distribution of franchises
fig_pie = px.pie(df_distribution, names='Business Name', values='counts', title='Distribution of Franchises')
st.plotly_chart(fig_pie)

# Add any other visualizations or components as needed

# Run the Streamlit app
if __name__ == "__main__":
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.radio("Choose a page", ["Home", "Analysis", "About"])

    if app_mode == "Home":
        st.title("Welcome to Yelp Data Analysis")
        # Add content for the home page

    elif app_mode == "Analysis":
        st.title("Yelp Data Analysis")
        # Add content for the analysis page

    elif app_mode == "About":
        st.title("About")
        # Add content for the about page

query = run_query("SELECT name, stars FROM restaurant WHERE review_count >= 100 LIMIT 10")
restaurants_per_state= run_query("SELECT state, COUNT(state) AS `State counts` FROM restaurant GROUP BY state ORDER BY `State counts` DESC;")

#
# df = pd.DataFrame(query)
# st.write("Query Result Table:")
# st.dataframe(df)
# st.write("Bar Chart:")
# st.bar_chart(df.set_index('name'))
#
#
#
# df = pd.DataFrame(restaurants_per_state)
# st.write("REstaurants per state: ")
