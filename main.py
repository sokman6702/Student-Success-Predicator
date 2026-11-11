import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# the file contain 100 students data 
df=pd.read_csv("archive/student_performance_100.csv")
print("first five rows")
print(df.head())

# decoding using label encoder
le=LabelEncoder()
df['internet']=le.fit_transform(df["internet"])
df['passed']=le.fit_transform(df["passed"])
print("After encoding")
print(df.head())

# separating features and targets 
features=['study hours','attendance','past score','sleep hours']
scaler=StandardScaler()
df_scaled=df.copy()
df_scaled[features]=scaler.fit_transform(df[features])

X=df_scaled[features]    
y=df_scaled['passed']


X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    random_state=42,
    test_size=0.2,
     stratify=y
)


model=LogisticRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)



print("classification Report")
print(classification_report(y_test,y_pred))



# making the graph for the data 
conf_matrix = confusion_matrix(y_test,y_pred,labels=[0,1])
plt.figure(figsize=(6,4))
sns.heatmap(conf_matrix,annot=True,fmt="d",cmap="Blues",xticklabels=["Fail","Pass"],yticklabels=["Fail","Pass"])
plt.xlabel("Predicted")
plt.ylabel("actual")
plt.title("Confusion Matrix")
plt.tight_layout()
plt.show()


# taking input from the user for predicition based on input and Data trained by the model
print("\n===========================================================")
print("\n-------------------Student Success Predictor---------------")
print("\n===========================================================")


try:
    study_hours=float(input("Enter Your Study Hours : "))
    attendance=int(input("Enter Your Attendance : "))
    past_score=int(input("Enter Your  Past Score : "))
    sleep_hours=float(input("Enter Your Sleep Hours : "))
    

    user_input_df=pd.DataFrame([{
        'study hours' : study_hours,
        'attendance'  : attendance,
        'past score'  : past_score,
        'sleep hours' : sleep_hours
    }])

    user_input_scaled=scaler.transform(user_input_df)
    predicition=model.predict(user_input_df)[0]
    result="Pass" if predicition == 1 else "Fail"
    print(f"Prediction based on input : {result}")

except Exception as e:
    print("an error occured",e)
