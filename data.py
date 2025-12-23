import pandas as pd

print(pd.__version__)

df = pd.read_csv("Exam_Score_Prediction.csv")

print(df.head()) #Prints the first 5 data
print(df.info()) #Prints all the info about the file

print(df.columns) #Prints all the column header


#mean of study hours
mean_studyhours = df['study_hours'].mean()
print("The average study hours is: ", mean_studyhours)

#Outliers
Q1 = df['study_hours'].quantile(0.25)
Q3 = df['study_hours'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5*IQR
upper_bound = Q3 + 1.5*IQR

outliers = df[(df['study_hours'] < lower_bound) | (df['study_hours'] < upper_bound)]
print('The outliers are in rows: ', outliers)

