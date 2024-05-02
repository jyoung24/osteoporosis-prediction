import streamlit as st
import pandas as pd
import seaborn as sns

st.title('Historical Patient Information Dashboard')
df = pd.read_csv('osteoporosis_processed_train_val.csv')

# Define function for the main page
def main():
    
    def group_age(age):
        if age <= 25:
            return "0-25"
        elif age <= 50:
            return "26-50"
        elif age <= 75:
            return "51-75"
        else:
            return "76-100"
            
    df['Age Group'] = df['Age'].apply(group_age)
    agg_data = df.groupby('Age Group')['Osteoporosis'].count().reset_index()
    st.title('Osteoporosis Cases by Age Group')
    st.bar_chart(agg_data.set_index('Age Group'))

    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.subheader('Proportion of Osteoporosis Cases by Gender')
    gender_counts = df.groupby('Osteoporosis')[['Gender_Female', 'Gender_Male']].sum().reset_index()
    gender_counts = pd.melt(gender_counts, id_vars='Osteoporosis', var_name='Gender', value_name='Count')
    sns.barplot(data=gender_counts, x='Osteoporosis', y='Count', hue='Gender')
    st.pyplot()

    st.subheader('Relationship between Osteoporosis and Body Weight')
    body_weight_counts = df.groupby('Osteoporosis')[['Body Weight_Normal', 'Body Weight_Underweight']].sum().reset_index()
    body_weight_counts = pd.melt(body_weight_counts, id_vars='Osteoporosis', var_name='Body Weight', value_name='Count')
    sns.barplot(data=body_weight_counts, x='Osteoporosis', y='Count', hue='Body Weight')
    st.pyplot()

    race_counts1 = df.groupby('Race/Ethnicity_Caucasian')['Osteoporosis'].sum().reset_index()
    race_counts2 = df.groupby('Race/Ethnicity_African American')['Osteoporosis'].sum().reset_index()
    race_counts3 = df.groupby('Race/Ethnicity_Asian')['Osteoporosis'].sum().reset_index()
    st.header("Race and Osteoperosis")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Caucasian with Osteoperosis")
        st.bar_chart(race_counts1, x="Race/Ethnicity_Caucasian", y="Osteoporosis")
    with col2:
        st.subheader("African American with Osteoperosis")
        st.bar_chart(race_counts2, x="Race/Ethnicity_African American", y="Osteoporosis")
    with col3:
        st.subheader("Asian with Osteoperosis")
        st.bar_chart(race_counts3, x="Race/Ethnicity_Asian", y="Osteoporosis")

if __name__ == "__main__":
    main()
