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

# # Number of restaurants in each state:
# fig_bar = px.bar(df.groupby('state').size().reset_index(name='State counts'), x='state', y='State counts', title='Number of Restaurants in Each State')
# st.plotly_chart(fig_bar)

# # Number of restaurants in each city:
# fig_bar = px.bar(df.groupby('city').size().reset_index(name='City counts'), x='city', y='City counts', title='Number of Restaurants in Each City')
# st.plotly_chart(fig_bar)

# # Sort users in descending order by rating or number of fans:
# options = ['Average Stars', 'Number Of Fans']
# selected_option = st.selectbox('Select sorting option:', options)

# if selected_option == 'Average Stars':
#     fig_bar = px.bar(df.sort_values('user_average_stars', ascending=False), x='user_name', y='user_average_stars', title='Top Users by Average Stars')
#     st.plotly_chart(fig_bar)
# elif selected_option == 'Number Of Fans':
#     fig_bar = px.bar(df.sort_values('user_fans', ascending=False), x='user_name', y='user_fans', title='Top Users by Number of Fans')
#     st.plotly_chart(fig_bar)
# else:
#     st.write('Please select at least one option.')

# # Top rating restaurants in selected state or US:
# selected_states = st.multiselect('Select states:', df['state'].unique())

# if selected_states:
#     filtered_df = df[df['state'].isin(selected_states)]
#     fig_bar = px.bar(filtered_df.sort_values('stars', ascending=False), x='name', y='stars', title='Top-Rated Restaurants in Selected States')
#     st.plotly_chart(fig_bar)
# else:
#     fig_bar = px.bar(df.sort_values('stars', ascending=False), x='name', y='stars', title='Top-Rated Restaurants in the US')
#     st.plotly_chart(fig_bar)

# # Top rating restaurants by selected cuisine:
# selected_cuisines = st.multiselect('Select cuisines:', df['category'].unique())

# if selected_cuisines:
#     filtered_df = df[df['category'].isin(selected_cuisines)]
#     fig_bar = px.bar(filtered_df.sort_values('stars', ascending=False), x='name', y='stars', title='Top-Rated Restaurants by Selected Cuisines')
#     st.plotly_chart(fig_bar)
# else:
#     st.write('Please select at least one cuisine.')

# # Latest review of selected restaurant:
# selected_id = st.text_input('Enter the business ID:')

# if selected_id:
#     if selected_id in df['rev_business_id'].values:
#         latest_review = df[df['rev_business_id'] == selected_id].sort_values('rev_date', ascending=False).iloc[0]
#         st.write(f"Latest review for business ID {selected_id}:")
#         st.write(f"User ID: {latest_review['rev_user_id']}")
#         st.write(f"Stars: {latest_review['rev_stars']}")
#         st.write(f"Date: {latest_review['rev_date']}")
#         st.write(f"Review text: {latest_review['rev_text']}")
#         st.write(f"Useful: {latest_review['rev_useful']}, Funny: {latest_review['rev_funny']}, Cool: {latest_review['rev_cool']}")
#     else:
#         st.write('Invalid business ID')
# else:
#     st.write('Please enter a business ID.')

# # Elite vs regular
# elite_count = df[df['user_elite'] != ''].shape[0]
# regular_count = df[df['user_elite'] == ''].shape[0]

# df_counts = pd.DataFrame({'User_Type': ['Elite Users', 'Regular Users'], 'Count': [elite_count, regular_count]})

# fig_pie = px.pie(df_counts, values='Count', names='User_Type', title='Elite Users vs Regular Users')
# st.plotly_chart(fig_pie)

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
