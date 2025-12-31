"""
FINAL EXAM SCORE PREDICTION MODEL

This program is a simple model that predicts the exam score from four different factors.
The four factors are Study Hours, Sleep Hours, Class Attendance, and Age.
Although, there are a lot of factors that can contribute to the outcome of the score and this program
is only used strictly for educational and entertainment purposes.

This program utilizes Multiple Linear Regression and basic Machine Learning to predict exam scores.
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# This class is used to determine whether the given input is above, below, or equal to the average
def CompareToMean(name, given, mean):
    if given > mean:
        print("\nYour", name, "is above the average -- ", mean)
    elif given == mean:
        print("\nYour", name, "is the same as the average -- ", mean)
    else:
        print("\nYour", name, "is below the average -- ", mean)

#Reads the csv file where all data used is located
df = pd.read_csv("Exam_Score_Prediction.csv")

#Shows a few data points from the data set
print("Source Dataset: ")
print(df.head())

#Disclaimer Message for the user
print("Disclaimer! This program will not guarantee result and is used strictly for educational purposes only." \
"Any predictions given may be taken as a bench mark but not a guaranteed score." \
"Please do not solely rely on this program to predict your score since this program will not give guaranteed results.\n")

#mean of the outcome
mean_examscore = df['exam_score'].mean()

#mean of the predictors
mean_studyhours = round(df['study_hours'].mean(), 2) #study_hours
mean_sleephours = round(df['sleep_hours'].mean(), 2) #sleep_hours
mean_age = round(df['age'].mean(), 2) #age
mean_attendance = round(df['class_attendance'].mean(), 2) #class_attended

#Assigning the predictors and the outcome
X = df[['sleep_hours', 'study_hours', 'class_attendance', 'age']] #Predictors Variable
Y = df['exam_score'] #Outcome Variable

#Uses scikit learn to create multiple regression line
ModelType = LinearRegression() #Type of regression line used
ModelType.fit(X, Y) #creates the regression equation

#calculations for predictions
ModelType.coef_ #calculates the coefficient of each predictors
ModelType.intercept_ #calculates the intercept of the equation (where all balues are zero)

#Save the Trained Model
with open("PredictionModel.pk1", "wb") as f:
    pickle.dump(ModelType, f)

#Open the Trained Model
with open("PredictionModel.pk1", "rb") as f:
    ModelType = pickle.load(f)

#asks user input for each new data
sleep = int(input('How many hours did you sleep? ')) 
study = int(input('\nHow many hours did you study? '))
attend = int(input('\nHow many classes did you attend (whole semester as a percentage [value only])? '))
age = int(input('\nHow old are you? '))

#creates a data frame of the given data
data_given = pd.DataFrame([[sleep, study, attend, age]], columns=["sleep_hours","study_hours", "class_attendance", "age"])

#calculations for the actual prediction
predicted_score = ModelType.predict(data_given) #calculates the predicted score
predicted = round(predicted_score[0], 2) #rounds the predicted score and removes unnecessary brackets around outcome

#prints out the prediction
print('\nYou predicted score according to the data you have given is', predicted, 'percent')

if predicted > 100:
    print("This result may be unrealistic")

#prints comparison with the given data and mean to determine whether they are above, below, or equal to the average
CompareToMean("SLEEP HOURS", sleep, mean_sleephours)
CompareToMean("STUDY HOURS", study, mean_studyhours)
CompareToMean("ATTENDANCE", attend, mean_attendance)
CompareToMean("AGE", age, mean_age)