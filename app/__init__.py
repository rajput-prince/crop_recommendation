from flask import Flask
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load models and scalers
model = pickle.load(open('model.pkl', 'rb'))
sc = pickle.load(open('standscaler.pkl', 'rb'))
ms = pickle.load(open('minmaxscaler.pkl', 'rb'))

from app import routes  # Import routes to register them with the app
# tiuuyit