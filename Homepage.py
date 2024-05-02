import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title='EDA Dashboard')


st.title('Real-Time Patient  Dashboard')
st.write("This page creates a comprehensive look at what the average patient with osteoporosis might look like. By exploring various demographic factors such as age, gender, ethnicity, and medical history, we wanted to provide insights into the characteristics of individuals diagnosed with osteoporosis. This dashboard allows users to interactively explore the data, visualize key trends, and gain a deeper understanding of the factors associated with osteoporosis.")


# Load the dataset
df = pd.read_csv('osteoporosis_testing.csv')

# function that randomly selecst 50% of the dataset
# we did this to simulate us fetching data from an API

def select_other_50_percent():
    # Randomly select 50% of the rows
    df_other_50_percent = df.sample(frac=0.5, random_state=42)
    return df_other_50_percent


# button to fetch the other 50% of the data
if st.button('Fetch New Patient Data'):
    df = select_other_50_percent()
    st.success('New Patient Data Loaded Successfully')

# filters for the sidebar

age_range = st.sidebar.slider('Select Age Range', min_value=df['Age'].min(), max_value=df['Age'].max(), value=(df['Age'].min(), df['Age'].max()))


other_filters = {
    'Family History': st.sidebar.radio('Family History', ['Yes', 'No']),
    'Race/Ethnicity': st.sidebar.radio('Race/Ethnicity', ['African American', 'Asian', 'Caucasian']),
    'Smoking': st.sidebar.radio('Smoking', ['Yes', 'No'])
}

# creating a filtered dataset
# since we had a lot of categorical variables, onehotencoder made our dataset very large
# so, we had to create a roundabout way of filtering
filtered_df = df[(df['Age'] >= age_range[0]) & (df['Age'] <= age_range[1])]
for filter_name, filter_value in other_filters.items():
    if filter_name == 'Family History':
        filtered_df = filtered_df[filtered_df['Family History_' + filter_value.replace(' ', '_')]]
    elif filter_name == 'Smoking':
        filtered_df = filtered_df[filtered_df['Smoking_' + filter_value.replace(' ', '_')]]
    # Filter by race/ethnicity
    elif filter_name == 'Race/Ethnicity':
        if filter_value == 'African American':
            filtered_df = filtered_df[filtered_df['Race/Ethnicity_African American']]
        elif filter_value == 'Asian':
            filtered_df = filtered_df[filtered_df['Race/Ethnicity_Asian']]
        elif filter_value == 'Caucasian':
            filtered_df = filtered_df[filtered_df['Race/Ethnicity_Caucasian']]

# filtering by osteoporosis for the charts
filtered_df = filtered_df[filtered_df['Osteoporosis'] == 1]

# charts section
#chart showing the gender distribution for patients with osteoporosis

st.subheader("Gender Distribution For Osteoporosis Patients")
gender_counts = filtered_df[['Gender_Female', 'Gender_Male']].sum()
gender_pie_chart = px.pie(values=gender_counts, names=['Female', 'Male'], title="Gender Distribution")
st.plotly_chart(gender_pie_chart)


st.subheader("Distribution by Age and Bodyweight")

# creating 'Age Group' column based on age bins
age_bins = [20, 30, 40, 50, 60, 70, 80, 90, 100]
age_labels = ['20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90-100']
filtered_df['Age Group'] = pd.cut(filtered_df['Age'], bins=age_bins, labels=age_labels, right=False)

# grouping by age group for our second chart
heatmap_data = filtered_df.groupby(['Age Group', 'Body Weight_Normal', 'Body Weight_Underweight']).size().reset_index(name='Count')
heatmap_data['Body Weight Category'] = heatmap_data['Body Weight_Underweight'].apply(lambda x: 'Underweight' if x == 1 else 'Normal')


# grouped bar chart
grouped_bar_chart = px.bar(heatmap_data, x='Age Group', y='Count', color='Body Weight Category', 
                            title="Distribution of Osteoporosis Status by Age Group and Body Weight Category",
                            labels={'Count': 'Count', 'Age Group': 'Age Group'},
                            barmode='group')
st.plotly_chart(grouped_bar_chart)


st.subheader(" Osteoporosis Patient Medical Conditions")

# medical condition distribution chrt
medical_conditions_counts = filtered_df[['Medical Conditions_Hyperthyroidism', 'Medical Conditions_None', 'Medical Conditions_Rheumatoid Arthritis']].sum()
medical_conditions_bar_chart = px.bar(x=medical_conditions_counts.index, y=medical_conditions_counts.values, 
                                      labels={'x': 'Medical Conditions', 'y': 'Count'}, 
                                      title="Medical Conditions Distribution for Patients with Osteoporosis")

medical_conditions_bar_chart.update_xaxes(tickvals=[0, 1, 2], ticktext=['Hyperthyroidism', 'None', 'Rheumatoid Arthritis'])

st.plotly_chart(medical_conditions_bar_chart)

st.subheader("Osteoporosis Patient Nutrient Intake")

# vitamin d and calcium intake for those with osteoporosis
vitamin_d_counts = filtered_df[['Vitamin D Intake_Insufficient', 'Vitamin D Intake_Sufficient']].sum()
vitamin_d_bar_chart = px.bar(x=vitamin_d_counts.index, y=vitamin_d_counts.values, 
                             labels={'x': 'Vitamin D Intake', 'y': 'Count'}, 
                             title="                 Vitamin D Intake",
                             width = 400, height = 350 )  
vitamin_d_bar_chart.update_xaxes(tickvals=[0, 1], ticktext=['Insufficient Intake', 'Sufficient Intake'])


calcium_counts = filtered_df[['Calcium Intake_Adequate', 'Calcium Intake_Low']].sum()

calcium_df = pd.DataFrame({
    'Calcium Intake': ['Adequate', 'Low'],
    'Count': calcium_counts.values
})

calcium_bar_chart = px.bar(calcium_df, x='Calcium Intake', y='Count', 
                            title=" Calcium Intake",
                            labels={'Count': 'Count'},
                            width = 400, height = 350)  

# displaying the columns side by side since they have similar metrics
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(vitamin_d_bar_chart)

with col2:
    st.plotly_chart(calcium_bar_chart)