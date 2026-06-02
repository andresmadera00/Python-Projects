import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askfloat
from tkinter.simpledialog import askinteger
from tkinter import ttk
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def submit():

    experience = askinteger("input","Entry experience years")

    salary = askfloat("input","Entry your salary")

    over_time = askinteger("input","Entry overtiome hours:")

    new_employee = [[experience, salary, over_time]]

    prediction = log_model.predict(new_employee)

    if prediction[0] == 1:

        employee = "Leave"
    else:
        employee= "Stay"

    print(employee)
    print(prediction)


    result.config(text=f"The employe {employee}")


data = pd.DataFrame({
    "Experience":[1,5,2,8],
    "Salary":[45000,80000,50000,120000],
    "Overtime Hours":[15,5,20,2],
    "Left Company":[1,0,1,0]

})


X = data[["Experience","Salary","Overtime Hours"]]
Y = data["Left Company"]

X_train, X_test , Y_train , Y_test = train_test_split(

    X,Y,test_size=0.2, random_state= 0
)


log_model = LogisticRegression()
log_model.fit(X_train,Y_train)





window = Tk()

window.geometry("450x450")

window.title("Employe Attrition Predictor")

Label(window,text="Employe Attrition Predictor",font=("Arial",16,"bold")).pack()


Label(window,text="Experience").pack()
Label(window,text="Salary").pack()
Label(window,text="Overtime Hours").pack()

btn_entrydata = Button(window,text="Entry Data",command=submit)
btn_entrydata.pack()

result = Label(window,text="")
result.pack()

window.mainloop()