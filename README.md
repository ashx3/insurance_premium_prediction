# Health Care Insurance Premium Predicion

![insurance_premium_poster](/images/insurance_premium_poster.jpg)

## Context
Now a days, healthcare firms use personal health data of insurance holders to predict health insurance premium of individuals. The amount of the premium for a health insurance policy depends from person to person, as many factors affect the amount of the premium for a health insurance policy. Let’s say age, a young person is very less likely to have major health problems compared to an older person. Thus, treating an older person will be expensive compared to a young one. That is why an older person is required to pay a high premium compared to a young person. Just like age, many other factors affect the premium for a health insurance policy.

![insurance_premium_context](/images/insurance_premium_context.jpg)

## Content
Here, we have created a system that shows the different techniques that are being used in order to estimate the how much amount of insurance premium is required on the basis of individual health situation. The dataset comprises of 1338 records with 7 attributes. The data is in structured format and stored in a CSV file. 

#### Data Source
KAGGLE - https://www.kaggle.com/datasets/noordeen/insurance-premium-prediction

## Abstract
The main goal of this project to predict the medical bill expenses that can incur a person based on their health conditions. This can assist a person in concentrating on the health side of their life rather than the ineffective part. Five regression models naming Linear Regression, Decision Tree Regression, Random Forest Regression, Gradient Boosting Regression and KNN have been used to compare and contrast the performance of these algorithms. Training dataset was used for training the model and that training model helped to come up with some predictions.Then the predicted amount was compared with actual data to test and verify the model accuracy. Later accuracies of all these models were compared and the best performing model was picked for model deployment.

## __There is rise in demand for Health Care Insurance Premium in the recent years !!__

![rise in demand for insurance premium](/images/rising_demand.jpg)

- According to a study by the Peterson Center on Healthcare and the Kaiser Family Foundation (KFF), __U.S. healthcare spending rose nearly a trillion dollars from 2009 to 2019,__ when adjusted for inflation.
- A recent study reported that __U.S. healthcare spending during 2019 was nearly $3.8 trillion, or $11,582 per person__. By 2028, these costs are expected to climb to $6.2 trillion—roughly $18,000 per person.
- According to the American Medical Association (AMA), __healthcare costs are rising by about 4.5% a year.__

![Investopedia page](/images/rising_cost_insurance.jpg)

## Objective
The main objective of the project is to develop an API to predict the medical expenses for people on the basis of their health information. Machine learning based regression model is used for predicting above mentioned cases on the input data. The solution proposed here will help in estimating the premium of insurance based on people's health data.

## Attribute Information
- age - Insurance holder's age in years
- sex - Gender of the insurance holder (Male or Female)
- bmi - BMI stands for Body Mass Index, the ideal range according to height and weight is 18.5 to 24.9
- children - Number of children
- smoker - Whether the insurance holder is a smoker or not
- region - Residential area of the person
- expenses - Individual medical costs billed by health insurance

## Tasks Performed
### 1. Data exploration: 
Exploring the dataset using pandas, numpy, matplotlib and seaborn libraries.

### 2. Exploratory Data Analysis : 
Plotted different graphs to get more insights about dependent and independent features.

### 3. Feature Engineering : 
There are numerical and categorical features are present. Scaling was performed on numerical data and encoding of categorical data is done.

### 4. Model Building : 
For model building, data was splitted into training and testing set and various algorithms were used to train the model, namely:<br>
- Linear Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- KNN

### 5. Model Selection : 
Tested all the models and using the evaluation metrics i.e. RMSE & R-squared, the best performing model was picked for model deployment.

### 6. Web Application & Deployment : 
Created a web application using streamlit API that takes all the necessary inputs from the user & shows the output. Then deployed project on the Heroku Platform.

## Conclusion
This system shows us that the different techniques that are used in order to estimate the how much amount of premium required on the basis of individual health situation. It shows how a smoker and non-smokers are affecting the amount of premium, also significant differences between male and female expenses. After using different regressors for prediction, Gradient Boosting turned out to be best working model for this problem in terms of the accuracy. Our predictions help user to know how much amount of medical expenses need to be paid if they were to buy an insurance premium and also helps the healthcare organizations to charge insurance premium on basis of their current health situation.

# Helper
In this repository, we have performed the end to end Exploratory Data Analysis and identified the characteristics of the insurance holders, trained the model using different regression models and then picking the model with good accuracy. Later on, we have created a web application using streamlit API that takes all the necessary inputs from the user & shows the output. And then deploying the project on the Heroku Platform.

### 🟢 For EDA, please refer to : Insurance_Premium_Prediction_EDA.ipynb
### 🟢 For Model Building, please refer to : Insurance_Premium_Prediction_Model Building.ipynb
### 🟢 For Model Deployment, please enter this link : https://ashx3-insurance-premium-prediction-app-n2yuu7.streamlit.app/

# How to start and use streamlit?

Simply run the following commands on command line and let it do the magic
```
pip3 install -r requirements.txt
streamlit run app.py
```

__This is how our Streamlit Application looks:__

![streamlitapp page](/images/app_1.jpg)
