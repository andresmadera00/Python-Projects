import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askfloat
def delete():

    entry_hours.delete(0,END)
    entry_percentage.delete(0,END)

def predict():

    # Predict new student
    hours = float(entry_hours.get())
    percentage = float(entry_percentage.get())
    new_student = [[hours,percentage]]   # 5 hours studied, 80% attendance

    prediction = model.predict(new_student)

    print("Predicted Grade:", prediction[0])

    messagebox.showinfo(title="Prediction", message= prediction[0])


    
# Create dataset
data = pd.DataFrame({
    'Hours': [1,2,3,4,5,6,7,8],
    'Attendance': [60,65,70,75,80,85,90,95],
    'Grade': [45,50,55,65,70,75,85,90]
})

# Features (inputs)
X = data[['Hours', 'Attendance']]

# Target (output)
Y = data['Grade']

# Split data
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y,
    test_size=0.2,
    random_state=0
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, Y_train)

# Predict new student
new_student = [[5, 80]]   # 5 hours studied, 80% attendance

prediction = model.predict(new_student)

print("Predicted Grade:", prediction[0])



window = Tk()

window.geometry("450x450")

label1 = Label(window,text="Hours studied:")
label1.pack()
entry_hours = Entry(window)
entry_hours.pack()

label2 = Label(window,text="Porcentage of attendece:")
label2.pack()
entry_percentage = Entry(window)
entry_percentage.pack()

btn_delete = Button(window,text="delete",command=delete)
btn_delete.pack()

btn_predict = Button(window,text="predict",command=predict)
btn_predict.pack()



window.mainloop()
