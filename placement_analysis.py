import numpy as np
import pandas as pd
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
df = pd.read_csv('placement_readiness.csv')
#NumPy

SKILLS = ["Python_Score","SQL_Score","Aptitude_Score","Communication_Score"]
python_array = df['Python_Score'].to_numpy()
aptitude_array = df['Aptitude_Score'].to_numpy()
comm_above70 = df['Communication_Score'].to_numpy()
comm_above70 = (comm_above70>70).sum()
skills_array = df[SKILLS].to_numpy()
skills_diff = skills_array.max(axis=1) - skills_array.min(axis=1)
print(f"Average Python Score across the batch is {python_array.mean().round(2)}")
print(f"Highest Aptitude Score : {aptitude_array.max()}")
print(f"Lowest Aptitude Score : {aptitude_array.min()}")
print(f"No of Students above 70 in communication : {comm_above70}")
print(f"Average Skill gap is {skills_diff.mean().round(2)}")
print(f"Largest Skill gap is {skills_diff.max()}")

#Pandas
print("\n")
print("Head Of DataFrame")
print(df.head())
print("\n")
print(f"Shape Of DataFrame is {df.shape}")
print("\n")
print("Columns Of DataFrame are")
print(df.columns)
print("\n")
print("Description Of DataFrame is")
print(df.describe())
print("\n")

print("Students Above 75 in python")
print(df.loc[df['Python_Score']>75,'Student_ID'])
print("\n")
print("DataFrame Sorted By Aptitude Scores")
print(df.sort_values(by='Aptitude_Score'))
print("\n")
print("Top 10 students by Python Score")
print(df.sort_values(by='Python_Score',ascending=False).head(10)['Student_ID'])
print("\n")
print("Students Strong in Python but weak in Communication")
print(df.loc[df['Python_Score']>df['Communication_Score'],'Student_ID'])
print("\n")

#Creating Knowledge

df['Total_Score'] = df["Aptitude_Score"]+df["Communication_Score"]+df["Python_Score"]+df['SQL_Score']
df['Average_Score'] = (df["Total_Score"]/4).round(2)
df['Weakest_Skill_Score'] = skills_array.min(axis=1)
df['Readiness_Score'] = (df['Average_Score']+(2*df['Projects_Completed'])+df['Mock_Interviews_Attended']).clip(upper=100)
df['Readiness_Band'] = "Ready"
df.loc[(df['Readiness_Score'].between(60,74)),'Readiness_Band'] = "Almost Ready"
df.loc[df['Readiness_Score']<60,'Readiness_Band'] = "Needs Work"
print("Details Of Students according to Readiness Bands")
print(df["Readiness_Band"].value_counts())
print(df['Branch'].value_counts())

#More-Calculations
readiness = ["Ready","Almost Ready","Needs Work"]
readiness_band = {}
for ready in readiness:
    readiness_band[ready] = (df['Readiness_Band']==ready).sum()
avg_score = {}#Average Score Of Skills

for skill in SKILLS:
    avg_score[skill] = df[skill].mean().round(2)

plt.figure(figsize=(12,6))
plt.bar(avg_score.keys(),avg_score.values(),color=['red','green','blue','orange'])
plt.title("Average Score Of Each Skill")
plt.xlabel("Skills")
plt.ylabel("Average Score")
plt.savefig("./charts/BarGraph1.png")
plt.close()

#Students in Readiness band
plt.figure(figsize=(12,6))
plt.bar(readiness_band.keys(),readiness_band.values(),color=['blue','yellow','red'])
plt.title("No Of Students In Each Readiness Band")
plt.xlabel("Readiness Band")
plt.ylabel("No Of Students")
plt.savefig("./charts/BarGraph2.png")
plt.close()

#Line Graph
branches = ["MECH","IT","CSE","ECE"]
branch_readiness = {}
for branch in branches:
    branch_readiness[branch] = df.loc[df['Branch']==branch, 'Readiness_Score'].mean().round(2)
plt.figure(figsize=(12,6))
plt.plot(branch_readiness.keys(),branch_readiness.values(),marker='o',color='blue')
plt.title("Average readiness by branch")
plt.xlabel("Branch")
plt.ylabel("Average Score")
plt.savefig("./charts/MyLineGraph.png")
plt.close()
