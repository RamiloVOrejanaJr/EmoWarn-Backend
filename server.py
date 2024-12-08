from flask import Flask#, jsonify
#from nltk.corpus import stopwords
#import tf_keras
#import re

app = Flask(__name__)


#public IP: 124.106.139.105

@app.route("/data", methods=["GET", "POST"])
def send_data():
    # Example data to return
    #sample_data = {"temperature": "25°C", "humidity": "60%"}

    data = {'fake': 75,
            'real': 25,
            'joy': 25,
            'sadness': 25,
            'anger': 25,
            'fear': 25,
            'surprise': 25
            }

    return data


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=False)
