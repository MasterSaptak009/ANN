import numpy as np
import pandas as pd 
import random
marks=[]
for i in range(100):
    subject_marks=[]
    for j in range(10):
        subject_marks.append(random.randrange(5,95))
    marks.append(subject_marks)
print(marks)

df = pd.DataFrame(data=marks, columns=[f"Subject_{i+1}" for i in range(10)])
df.to_csv("student_marks.csv")
print(df)

