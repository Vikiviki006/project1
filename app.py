import numpy as np
from flask import Flask,render_template,request
import pickle


# from keras import models
file=open('my_model.pkl','rb')
model=pickle.load(file)

#file.close()

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method == 'POST':
        mydict=request.form
        Age=int(mydict['Age'])
        Gender=int(mydict['Gender'])
        Hormonal_Changes=int(mydict['Hormonal_Changes'])
        Family_History=int(mydict['Family_History'])
        Ethnicity=int(mydict['Ethnicity'])
        Body_Weight=int(mydict['Body_Weight'])
        Calcium_Intake=int(mydict['Calcium_Intake'])
        Vitamin_D=int(mydict['Vitamin_D'])
        Physical_Activity=int(mydict['Physical_Activity'])
        Alcohol_Consumption=int(mydict['Alcohol_Consumption'])
        Medical_Conditions=int(mydict['Medical_Conditions'])
        Medications=int(mydict['Medications'])
        
        input_feature=[Age,Gender,Hormonal_Changes,Family_History,Ethnicity,Body_Weight,Calcium_Intake,Vitamin_D,Physical_Activity,Alcohol_Consumption,Medical_Conditions,Medications]
        
        input_feature = np.array(input_feature)

        input_feature = input_feature.astype(np.float).reshape(1,-1)
        predict1 = model.predict(input_feature)
        print(predict1)
        
        
        #predict = model.predict_proba([input_feature])[0][1]

        #infprob = infprob*100
        return render_template('result.html',inf=predict1)
   
    return render_template('index.html')
   
if __name__ == '__main__'  :
    app.run(host='192.168.63.19') 
