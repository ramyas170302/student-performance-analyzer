import pandas as pd

df=pd.read_excel("Final_Marks_Data.xlsx")
print(df)

print(df.head(4))
print(df.tail(3))
print(df.isnull().sum())

df.info()
print(df.describe())


df["Internals_internals"]=df["Internal Test 1 (out of 40)"]+df["Internal Test 2 (out of 40)"]
df["Total_score"]=df["Internals_internals"]+df["Assignment Score (out of 10)"]+df["Final Exam Marks (out of 100)"]
df["Performance"]=df["Final Exam Marks (out of 100)"].apply(
    lambda x: "High" if x>75 else ("Medium" if (x>=50 and x<=75) else "Low")
)
avg_total=(df.groupby("Performance")["Final Exam Marks (out of 100)"].mean())
avg_att=df.groupby("Performance")["Attendance (%)"].mean()
avg_hr=df.groupby("Performance")["Daily Study Hours"].mean()
avg_ass=df.groupby("Performance")["Assignment Score (out of 10)"].mean()
print(round(avg_att,2))
print("\n")

print(round(avg_hr,2))
print("\n")
print(avg_ass.idxmax())
print("\n")
high_performance=df[df["Performance"]=="High"]
print(high_performance)
print("\n")
print(df.columns)
risk=df.query('`Attendance (%)`<60 and `Final Exam Marks (out of 100)`<50')
print(risk["Student_ID"])
ml=df.query("`Daily Study Hours`>4 and `Final Exam Marks (out of 100)`<80")
print(ml)

final=df.sort_values(by="Total_score",ascending=False)
print(df.head(10))
df.sort_values(by="Attendance (%)",ascending=True)
print(df.tail(5))

df.sort_values(by="Final Exam Marks (out of 100)",ascending=False)
print("Top 10 students:")
print(df.head(10))


print("\n")
print("Summary:\n")
print("Total number of students:",len(df))
print("Total average Final marks:",round(df["Final Exam Marks (out of 100)"].mean(),2))
print("Overall Attendence average:",round(df["Attendance (%)"].mean(),2))
print("Overall Average Daily study hours:",round(df["Daily Study Hours"].mean(),2))
print("Count of High, Medium, Low performers:",df.groupby("Performance")["Student_ID"].count())
print("At Risk:",risk["Student_ID"].count(),"Students")

top=final.iloc[0]
print("topper:",top["Student_ID"],"(",top["Final Exam Marks (out of 100)"],")")
low=final.iloc[-1]

print("Lowest:",low["Student_ID"],"(",low["Final Exam Marks (out of 100)"],")")


