import streamlit as st

image = "osteo.jpg"  # Path to your image file
st.image(image, use_column_width=True)

def main():
    st.title("Osteoporosis Prediction Application")
    st.write("Welcome to our Osteoporosis Prediction Dashboard. This app provides insights into osteoporosis prediction based on demographic and health-related factors.")

    st.header("Features:")
    st.write("1. **Dashboard Overview:** Explore visualizations and summaries derived from a dataset containing information on osteoporosis cases, demographic attributes, medical history, and lifestyle factors.")
    st.write("2. **Data Visualization:** Interactive charts and graphs visualize key insights related to osteoporosis prevalence, distribution by age group, gender, race/ethnicity, body weight, and more.")
    st.write("3. **Model Description:** Access information about the predictive models used in the application, including dataset details, model development process, initial model performance, hyperparameter tuning, and final model selection.")
    st.write("4. **User Interaction:** Adjust filters such as age range, family history, race/ethnicity, and smoking status to explore how different factors impact osteoporosis prevalence.")
    st.write("5. **Performance Metrics:** View accuracy scores and F1 scores for the predictive models, providing insights into model performance and reliability.")

    st.header("Objective:")
    st.write("The primary objective of our application is to empower users, including healthcare professionals, researchers, and individuals concerned about osteoporosis, to gain valuable insights into the factors influencing osteoporosis prevalence. By visualizing data and model performance metrics, users can better understand the disease dynamics and make informed decisions regarding prevention, diagnosis, and treatment strategies.")

if __name__ == "__main__":
    main()


st.title('Model Summary')

st.subheader('Information on how we trained our model can be read below.')

st.write('The dataset used to develop this model originally had 1,958 observations of 16 different variables. After removing an identifier variable, 15 of them remained. First, the dataset was split into 20% testing data and 80% training/validation data. The training/validation data was then split into 70% training data and 30% validation data.')

st.write('Three initial models were created: a Logistic Regression Model (LR), a Random Forest Classification Model (RF), and a Decision Tree Classification Model (DT). The preliminary accuracy scores are as follows: Accuracy (LR): 0.5073059360730593, Accuracy (RF): 0.4999916977999169, Accuracy (DT): 0.5026857617268575. These accuracy scores are relatively low. A Grid Search method was then used to find the optimum hyperparameters for the Random Forest Classification Model (RF) and the Decision Tree Classification Model (DT); there were no hyperparameters to tune for the Logistic Regression Model (LR). From here, new models were created using the hyperparameters obtained from the Grid Search.')

st.write('The accuracy scores of the new models are as follows: Accuracy (RF2): 0.8567413864674138, Accuracy (DT2): 0.8886550435865503. The F-1 scores are as follows: F-1 Score (RF2): 0.8378918844953693, F-1 Score (DT2): 0.877713768115942. Because the new Decision Tree Model has both the highest accuracy and F1 scores, this was the model chosen for the pipeline. In other words, the Decision Tree Model had the highest performance, so it was chosen to be the model for this application.')
