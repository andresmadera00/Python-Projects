import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askfloat
from tkinter.simpledialog import askinteger
from tkinter import ttk


def submit ():

    num_experience = askinteger("input","Entry experience years")
    num_hours = askinteger("input","Entry your work hours")

    selected = box_education.get()

    education = 0

    if selected == "High School":

        education = 1
         
    
    elif selected == "Diploma":
        education = 2
       
    
    elif selected == "Bachelor":
        education = 3
        
    
    elif selected == "Master/PhD":
        education = 4
        
    
    
    

    
    data_input = [[
        num_experience,
        education,
        num_hours
        ]]

    prediction = model.predict(data_input)

    
    result.config(text=f"Your salary will be : $ {round(prediction[0])}")
    print(f"Your salary will be : $ {prediction[0]}")

    


        
    
    
    





data = pd.DataFrame ({

    'Experience': [1,2,3,4,5,6,7,8,9,10],
    'Education':  [1,1,2,2,2,3,3,3,4,4],
    'Hours':       [35,38,40,40,42,45,45,48,50,50],
    'Salary': [
        45000,
        50000,
        58000,
        65000,
        72000,
        80000,
        90000,
        100000,
        115000,
        130000
    ]
})

Education_Title = {
"1" : "High School",
"2" : "Diploma",
"3" : "Bachelor",
"4" : "Master/PhD"}

x = data[["Experience",'Education','Hours']]

y = data['Salary']

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=0)

model = LinearRegression()

model.fit(x_train, y_train)





window = Tk()
window.geometry("450x450")
window.title("Emplorye salary prediction")

Label(window,text="Emplorye salary prediction",font=("Arial",16,"bold")).pack()


Label(window,text="Experience").pack()
Label(window,text="Hours").pack()


Label(window,text="Education").pack()

box_education = ttk.Combobox(window)
box_education['values'] =  (
    "High School",
    "Diploma",
    "Bachelor",
    "Master/PhD"
)

box_education.pack()

btn_entrydata = Button(window,text="Entry data", command=submit)
btn_entrydata.pack()

result =Label(window,text="")
result.pack()


window.mainloop()



