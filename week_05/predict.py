import pickle
from flask import Flask
from flask import request
from flask import jsonify

model_file = 'model_C=1.0.bin'

with open(model_file, 'rb') as f_in: 
    (dv, model) = pickle.load(f_in)

app = Flask('churn')

@app.route('/predict', methods=['POST']) # post because we need to send info about customer and it is not easy using GET method
def predict():
    customer = request.get_json()
    # separate the core logic in another function
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5

    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn) # turns numpy boolean into python boolean to avoid error 500
    }
    return jsonify(result)

if __name__ == "__main__": # python main method
    app.run(debug=True, host='0.0.0.0', port=9696)

# request will be sent using JSON file format.
# like python dictionary but with double quotes
# 404 not found
# 405 method no allowed
# cannot send a POST request from browser easily