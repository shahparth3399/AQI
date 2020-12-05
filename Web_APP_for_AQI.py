import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

Web_APP_for_AQI = Flask(__name__)
model = pickle.load(open('AQI_model1.pkl', 'rb'))

@Web_APP_for_AQI.route('/')
def home():
    return render_template('index.html')

@Web_APP_for_AQI.route('/AQI',methods=['POST'])
def AQI():
    '''
    For rendering results on HTML GUI
    '''
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    
    if(0<output<=50):
        cate="Good";
    elif(51<output<=100):
        cate="Satisfactory";
    elif(101<output<=200):
        cate="Moderately Polluted";
    elif(201<output<=300):
        cate="Poor";
    elif(301<output<=400):
        cate="Very Poor";
    elif(401<output<=500):
        cate="Severe";
    
        

    return render_template('index.html', prediction_text='AQI with given values of data can be {0} which is {1}'.format(output,cate))


if __name__ == "__main__":
    Web_APP_for_AQI.run(debug=True)
