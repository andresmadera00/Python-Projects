import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askfloat
from tkinter.simpledialog import askinteger

def submit():

    bedrooms = askinteger("Imput","Entry number of bedrooms")

    
    bathrooms = askinteger("Imput","Entry number of bathrooms")

    size = askfloat("Imput","Entry size house")
    
    
    data_input = [[
        bedrooms,
        bathrooms,
        size
        ]]
  
    prediction = model.predict(data_input)

    print("Predict Grade: " , round(prediction[0]))
    result.config(text=f"Result predicted is : {round(prediction[0])}$")

    




data = pd.DataFrame ({

'Bedrooms':  [1, 2, 2, 3, 3, 4, 4, 5, 5, 6],
'Bathrooms': [1, 1, 2, 2, 3, 2, 3, 3, 4, 4],
'Size':      [50, 80, 90, 120, 140, 160, 180, 220, 250, 300],
'Price':     [250000, 350000, 400000, 500000, 600000,
                  700000, 800000, 950000, 1100000, 1300000]

})


X = data[['Bedrooms','Bathrooms','Size']]
Y = data['Price']

X_test, X_train, Y_test, Y_train = train_test_split(X,Y,test_size=0.2,random_state=0)

model = LinearRegression()

model.fit(X_train,Y_train)




window = Tk()

window.geometry("450x450")

window.title("House Price Predictor")

Label(
    window,
    text="House Price Prediction System",
    font=("Arial",16,"bold")
).pack(pady=10)

lb_bedrooms = Label(window,text="BedRooms")
lb_bedrooms.pack()


lb_bathrooms = Label(window,text="Batrooms")
lb_bathrooms.pack()

lb_size = Label(window,text="Size")
lb_size.pack()

btn_bedrooms = Button(window,text="Entry Data", command= submit)
btn_bedrooms.pack()

result = Label(window,text="")
result.pack()




window.mainloop()


