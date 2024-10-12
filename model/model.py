import pickle
from sklearn.preprocessing import MinMaxScaler
import numpy as np
with open('model/cancer_model.pkl', 'rb') as f :
    model = pickle.load(f)

with open('model/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)


def prediction_cancer(features):
    # features_array = np.array(features).reshape(1, -1)
    # features_scaled = scaler.transform(features_array)
    # predictions = model.predict(user_input_scaled)
    predictions = model.predict([features])
    return predictions[0]