import streamlit as st
import pandas as pd
import pickle

#Overview and summary of dataset  being used for training and validating your model
st.caption(':red[**IMPORTANT NOTE**: The interactive form exists for users to test the model and serves as a _very brief_ preliminary screening. Users should not take the model prediction as fact, and all individuals who think they may be at risk of having osteoporosis should seek proper medical assistance.]') 

#User Interface Form
df = pd.read_csv('osteoporosis.csv')

st.header('Osteoporosis Risk Form')
st.subheader('Enter patient data here:')


def female_convert(response):
    if response == "Female":
        return True
    else: 
        return False

def male_convert(response):
    if response == "Female":
        return True
    else: 
        return False

def normal_hormonal_convert(response):
    if response == "Normal":
        return True
    else:
        return False
    
def meno_hormonal_convert(response):
    if response == "Postmenopausal":
        return True
    else:
        return False

def history_convert(response):
    if response == "Yes":
        return True
    else:
        return False
    
def no_history_convert(response):
    if response == "No":
        return True
    else:
        return False

def cauc_convert(response):
    if response == "Caucasian":
        return True
    else:
        return False

def asian_convert(response):
    if response == "Asian":
        return True
    else:
        return False

def aa_convert(response):
    if response == "African American":
        return True
    else:
        return False
    
def norm_weight_convert(response):
    if response == "Normal":
        return True
    else:
        return False

def under_weight_convert(response):
    if response == "Underweight":
        return True
    else:
        return False
    
def adeq_calcium_convert(response):
    if response == "Adequate":
        return True
    else:
        return False   

def low_calcium_convert(response):
    if response == "Low":
        return True
    else:
        return False

def suff_d_convert(response):
    if response == "Sufficient":
        return True
    else:
        return False

def insuff_d_convert(response):
    if response == "Insufficient":
        return True
    else:
        return False

def active_convert(response):
    if response == "Active":
        return True
    else:
        return False

def sedentary_convert(response):
    if response == "Sedentary":
        return True
    else:
        return False

def smoker_convert(response):
    if response == "Yes":
        return True
    else:
        return False

def nonsmoker_convert(response):
    if response == "No":
        return True
    else:
        return False

def noalcohol_convert(response):
    if response == "None":
        return True
    else:
        return False

def moderate_convert(response):
    if response == "Moderate":
        return True
    else:
        return False

def arthritis_convert(response):
    if response == "Rheumatoid Arthritis":
        return True
    else:
        return False

def hyperthyroidism_convert(response):
    if response == "Hyperthyroidism":
        return True
    else:
        return False

def nocondition_convert(response):
    if response == "None":
        return True
    else:
        return False

def corticosteroids_convert(response):
    if response == "Corticosteroids":
        return True
    else:
        return False

def nomedication_convert(response):
    if response == "None":
        return True
    else:
        return False

def fracture_convert(response):
    if response == "Yes":
        return True
    else:
        return False

def nofracture_convert(response):
    if response == "No":
        return True
    else:
        return False
    

Age = st.number_input("Enter Age", step=1) 
Gender = st.selectbox("Select Gender", options=["Female", "Male"]) 
Hormonal_Changes = st.selectbox("Select Horomonal Changes Type", options=["Normal", "Postmenopausal"]) 
Family_History = st.selectbox("Select Family History of Osteoporosis", options=["Yes", "No"]) 
Race_Ethnicity = st.selectbox("Select Race/Ethnicity", options=["Caucasian", "Asian", "African American"]) 
Body_Weight = st.selectbox("Select Weight Category", options=["Normal", "Underweight"]) 
Calcium_Intake = st.selectbox("Select Calcium Intake", options=["Adequate", "Low"]) 
Vitamin_D_Intake = st.selectbox("Select Vitamin D Intake", options=["Sufficient", "Insufficient"]) 
Physical_Activity = st.selectbox("Select Physical Activity Level", options=["Active", "Sedentary"]) 
Smoking = st.selectbox("Select Smoking Status", options=["Yes", "No"]) 
Alcohol_Consumption = st.selectbox("Select Alcohol Consumption Level", options=["None", "Moderate"]) 
Medical_Conditions = st.selectbox("Select Medical Condition", options=["Rheumatoid Arthritis", "Hyperthyroidism", "None"])
Medications = st.selectbox("Select Medications", options=["Corticosteroids", "None"])
Prior_Fractures = st.selectbox("Select Prior Fractures Status", options=["Yes", "No"]) 

pipeline = pickle.load(open('pipeline.pkl','rb'))

df = pd.DataFrame([{
    'Age': Age,
    'Gender_Female': female_convert(Gender),
    'Gender_Male': male_convert(Gender),
    'Hormonal Changes_Normal': norm_weight_convert(Hormonal_Changes),
    'Hormonal Changes_Postmenopausal': meno_hormonal_convert(Hormonal_Changes),
    'Family History_No': no_history_convert(Family_History),
    'Family History_Yes': history_convert(Family_History),
    'Race/Ethnicity_African American': aa_convert(Race_Ethnicity),
    'Race/Ethnicity_Asian': asian_convert(Race_Ethnicity),
    'Race/Ethnicity_Caucasian': cauc_convert(Race_Ethnicity),
    'Body Weight_Normal': norm_weight_convert(Body_Weight),
    'Body Weight_Underweight': under_weight_convert(Body_Weight),
    'Calcium Intake_Adequate': adeq_calcium_convert(Calcium_Intake),
    'Calcium Intake_Low': low_calcium_convert(Calcium_Intake),
    'Vitamin D Intake_Insufficient': insuff_d_convert(Vitamin_D_Intake),
    'Vitamin D Intake_Sufficient': suff_d_convert(Vitamin_D_Intake),
    'Physical Activity_Active': active_convert(Physical_Activity),
    'Physical Activity_Sedentary': sedentary_convert(Physical_Activity),
    'Smoking_No': nonsmoker_convert(Smoking),
    'Smoking_Yes': smoker_convert(Smoking),
    'Alcohol Consumption_Moderate': moderate_convert(Alcohol_Consumption),
    'Alcohol Consumption_None': noalcohol_convert(Alcohol_Consumption),
    'Medical Conditions_Hyperthyroidism': hyperthyroidism_convert(Medical_Conditions),
    'Medical Conditions_None': nocondition_convert(Medical_Conditions),
    'Medical Conditions_Rheumatoid Arthritis': arthritis_convert(Medical_Conditions),
    'Medications_Corticosteroids': corticosteroids_convert(Medications),
    'Medications_None': nomedication_convert(Medications),
    'Prior Fractures_No': nofracture_convert(Prior_Fractures),
    'Prior Fractures_Yes': fracture_convert(Prior_Fractures),
}])

if st.button("Predict Presence of Osteoporosis"): 
    Outcome = pipeline.predict(df)
    if Outcome == 1:
        st.warning("Our prediction is that the patient has osteoporosis")
    else:
        st.success("Our prediction is that the patient does not have osteoporosis")

